#!/usr/bin/env python3
"""Publish one public study issue through the required preflight gate."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate-study-issues.py"


def run(args: list[str]) -> str:
    result = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if result.returncode:
        if result.stdout:
            print(result.stdout, end="")
        raise SystemExit(result.returncode)
    return result.stdout


def run_checked(args: list[str]) -> None:
    output = run(args)
    if output:
        print(output, end="")


def issue_number_from_url(url: str) -> str:
    match = re.search(r"/issues/(\d+)", url)
    if not match:
        raise ValueError(f"cannot parse issue number from gh output: {url.strip()}")
    return match.group(1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default="myeolkoreaseoul/til")
    parser.add_argument("--title", required=True)
    parser.add_argument("--body-file", required=True)
    parser.add_argument("--comment-file", required=True)
    parser.add_argument("--label", action="append", default=[])
    parser.add_argument(
        "--approved-by-user",
        action="store_true",
        help="Set only after the user explicitly approves this exact title/body/comment packet.",
    )
    parser.add_argument("--limit", type=int, default=100)
    args = parser.parse_args()

    if not args.approved_by_user:
        print("refusing to publish: missing --approved-by-user", file=sys.stderr)
        return 2

    body_file = Path(args.body_file)
    comment_file = Path(args.comment_file)
    if not body_file.exists():
        print(f"body file not found: {body_file}", file=sys.stderr)
        return 2
    if not comment_file.exists():
        print(f"comment file not found: {comment_file}", file=sys.stderr)
        return 2

    run_checked(
        [
            str(VALIDATOR),
            "--title",
            args.title,
            "--body-file",
            str(body_file),
            "--comment-file",
            str(comment_file),
        ]
    )

    command = [
        "gh",
        "issue",
        "create",
        "--repo",
        args.repo,
        "--title",
        args.title,
        "--body-file",
        str(body_file),
    ]
    for label in args.label:
        command.extend(["--label", label])

    issue_url = run(command).strip()
    issue_number = issue_number_from_url(issue_url)

    run_checked(
        [
            "gh",
            "issue",
            "comment",
            issue_number,
            "--repo",
            args.repo,
            "--body-file",
            str(comment_file),
        ]
    )

    run_checked(
        [
            str(VALIDATOR),
            "--repo",
            args.repo,
            "--limit",
            str(args.limit),
        ]
    )

    print(issue_url)
    return 0


if __name__ == "__main__":
    sys.exit(main())
