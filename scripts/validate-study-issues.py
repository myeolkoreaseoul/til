#!/usr/bin/env python3
"""Validate public study issues against the repo quality gate."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys


REQUIRED_SECTIONS = [
    "## 출처",
    "## Issue Metadata",
    "## TL;DR",
    "## 학습 질문",
    "## 문제의식",
    "## 구조 분해",
    "## 근거",
    "## 비판적 분석",
    "## 분석 관점",
    "## 적용 가능 요소",
    "## 보류할 요소",
    "## 관련 이슈",
    "## Action Items",
]

FORBIDDEN = [
    "copy",
    "copied",
    "copying",
    "카피",
    "베끼",
    "imitation",
    "흡수",
    "훔치",
    "판정: 공개",
    "게시 위치",
    "public-approved",
    "private-required",
    "공개/비공개",
    "Discord source",
    "discord.com/channels",
    "/home/elite",
    "vault",
    "Vault",
    "셀레네",
    "케이퍼",
]


def gh_json(args: list[str]) -> object:
    return json.loads(subprocess.check_output(["gh", *args], text=True))


def contains_forbidden(text: str, needle: str) -> bool:
    if needle.isascii():
        return needle.lower() in text.lower()
    return needle in text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default="myeolkoreaseoul/til")
    parser.add_argument("--min-body", type=int, default=3500)
    parser.add_argument("--min-comment", type=int, default=900)
    parser.add_argument("--limit", type=int, default=100)
    args = parser.parse_args()

    issues = gh_json(
        [
            "issue",
            "list",
            "-R",
            args.repo,
            "--limit",
            str(args.limit),
            "--json",
            "number,title,body",
        ]
    )

    errors: list[str] = []
    for issue in sorted(issues, key=lambda item: item["number"]):
        number = issue["number"]
        body = issue.get("body") or ""
        comments = gh_json(
            [
                "api",
                f"repos/{args.repo}/issues/{number}/comments",
                "--paginate",
            ]
        )
        comment_text = "\n".join(comment.get("body") or "" for comment in comments)
        full_text = f"{issue.get('title') or ''}\n{body}\n{comment_text}"

        if not body.startswith("## 출처"):
            errors.append(f"#{number}: body must start with ## 출처")

        if len(body) < args.min_body:
            errors.append(f"#{number}: body too short ({len(body)} < {args.min_body})")

        if len(comment_text) < args.min_comment:
            errors.append(
                f"#{number}: comments too short ({len(comment_text)} < {args.min_comment})"
            )

        for section in REQUIRED_SECTIONS:
            if section not in body:
                errors.append(f"#{number}: missing section {section}")

        for forbidden in FORBIDDEN:
            if contains_forbidden(full_text, forbidden):
                errors.append(f"#{number}: forbidden term {forbidden}")

    if errors:
        print("\n".join(errors))
        return 1

    print(f"ok: checked {len(issues)} issues")
    return 0


if __name__ == "__main__":
    sys.exit(main())
