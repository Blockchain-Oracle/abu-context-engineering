#!/usr/bin/env python3
"""Detect common project stack signals for a quality profile."""

from __future__ import annotations

import json
import sys
from pathlib import Path


SIGNALS = {
    "node": ["package.json"],
    "pnpm": ["pnpm-lock.yaml", "pnpm-workspace.yaml"],
    "npm": ["package-lock.json"],
    "yarn": ["yarn.lock"],
    "bun": ["bun.lock", "bun.lockb"],
    "typescript": ["tsconfig.json"],
    "nextjs": ["next.config.js", "next.config.mjs", "next.config.ts"],
    "vite": ["vite.config.js", "vite.config.ts", "vite.config.mjs"],
    "biome": ["biome.json", "biome.jsonc"],
    "eslint": [".eslintrc", ".eslintrc.js", ".eslintrc.cjs", "eslint.config.js", "eslint.config.mjs"],
    "python": ["pyproject.toml", "requirements.txt", "uv.lock", "Pipfile"],
    "ruff": ["ruff.toml"],
    "rust": ["Cargo.toml"],
    "go": ["go.mod"],
    "foundry": ["foundry.toml"],
    "hardhat": ["hardhat.config.js", "hardhat.config.ts"],
    "github-actions": [".github/workflows"],
    "commitlint": ["commitlint.config.js", "commitlint.config.cjs", "commitlint.config.mjs"],
}

EXCLUDED_PARTS = {
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
    "node_modules",
    "out",
    "target",
    "typechain-types",
    "vendor",
}


def exists(root: Path, rel: str) -> bool:
    path = root / rel
    return path.exists()


def is_excluded(path: Path) -> bool:
    return any(part in EXCLUDED_PARTS for part in path.parts)


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").expanduser().resolve()
    if not root.exists():
        print(json.dumps({"error": f"path does not exist: {root}"}, indent=2))
        return 2

    detected = {}
    for name, paths in SIGNALS.items():
        matches = [rel for rel in paths if exists(root, rel)]
        if matches:
            detected[name] = matches

    source_files = []
    for pattern in ("*.ts", "*.tsx", "*.js", "*.jsx", "*.py", "*.rs", "*.go", "*.sol"):
        source_files.extend(str(path.relative_to(root)) for path in root.rglob(pattern) if not is_excluded(path))

    result = {
        "root": str(root),
        "signals": detected,
        "source_file_count": len(source_files),
        "sample_source_files": sorted(source_files)[:50],
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
