#!/usr/bin/env python3
"""Warn or fail when source files exceed configured line limits."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


DEFAULT_EXTENSIONS = {
    ".c",
    ".cc",
    ".cpp",
    ".css",
    ".go",
    ".h",
    ".hpp",
    ".js",
    ".jsx",
    ".mjs",
    ".py",
    ".rs",
    ".sol",
    ".ts",
    ".tsx",
}

DEFAULT_EXCLUDES = {
    ".agents",
    ".claude",
    ".codex",
    ".git",
    ".next",
    ".turbo",
    "_pagefind",
    "build",
    "coverage",
    "dist",
    "generated",
    "node_modules",
    "out",
    "target",
    "typechain-types",
    "vendor",
}


def should_skip(path: Path, root: Path, extensions: set[str], excludes: set[str]) -> bool:
    rel = path.relative_to(root)
    if any(part in excludes for part in rel.parts):
        return True
    if path.suffix not in extensions:
        return True
    return False


def count_lines(path: Path) -> int:
    with path.open("rb") as handle:
        return sum(1 for _ in handle)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check source file line limits.")
    parser.add_argument("root", nargs="?", default=".", help="Project root to scan.")
    parser.add_argument("--warn-lines", type=int, default=200, help="Warning threshold per source file.")
    parser.add_argument("--max-lines", type=int, default=300, help="Failing threshold per source file.")
    parser.add_argument("--fail-on-warn", action="store_true", help="Return failure when files exceed warn-lines.")
    parser.add_argument(
        "--extensions",
        default=",".join(sorted(DEFAULT_EXTENSIONS)),
        help="Comma-separated extensions to scan.",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Directory name to exclude. Can be passed multiple times.",
    )
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    if not root.exists():
        print(f"error: path does not exist: {root}", file=sys.stderr)
        return 2

    extensions = {item if item.startswith(".") else f".{item}" for item in args.extensions.split(",") if item}
    excludes = DEFAULT_EXCLUDES | set(args.exclude)
    warnings = []
    violations = []

    for path in root.rglob("*"):
        if not path.is_file() or should_skip(path, root, extensions, excludes):
            continue
        lines = count_lines(path)
        if lines > args.max_lines:
            violations.append((lines, path.relative_to(root)))
        elif lines > args.warn_lines:
            warnings.append((lines, path.relative_to(root)))

    if not warnings and not violations:
        print(f"ok: no source files exceed warning threshold {args.warn_lines} lines")
        return 0

    if warnings:
        print(f"file length warnings: target {args.warn_lines} lines")
        for lines, rel in sorted(warnings, reverse=True):
            print(f"{lines:>5}  {rel}")

    if violations:
        print(f"file length violations: max {args.max_lines} lines")
        for lines, rel in sorted(violations, reverse=True):
            print(f"{lines:>5}  {rel}")
        return 1

    return 1 if args.fail_on_warn else 0


if __name__ == "__main__":
    raise SystemExit(main())
