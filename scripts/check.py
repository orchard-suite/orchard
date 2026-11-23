#!/usr/bin/env python3
"""Check this repository's documents: python3 scripts/check.py.

Fails, naming each problem, on:
- an em-dash or en-dash in a document, a skill, or the pointer;
- a records folder, a roadmap file, or a diagram file back in the repository;
- a vantage.yaml that is missing, lacks a key the skills read, or names a hub;
- a relative link to a file that is not there.

An estate's names are hedge's to find: the Makefile runs it beside this.
"""

from __future__ import annotations

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEXT = (".md", ".yaml", ".yml", ".json", ".py")
SKIP_DIRS = {".git", "node_modules"}


def files(suffixes: tuple[str, ...] = TEXT) -> list[str]:
    out = []
    for folder, dirs, names in os.walk(ROOT):
        # A folder holding .git is another checkout, such as a worktree, and
        # not this repository's documents.
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS
                   and not os.path.exists(os.path.join(folder, d, ".git"))]
        for name in names:
            if name.endswith(suffixes):
                out.append(os.path.join(folder, name))
    return sorted(out)


def rel(path: str) -> str:
    return os.path.relpath(path, ROOT)


def dashes(path: str, text: str) -> list[str]:
    if path == os.path.abspath(__file__):
        return []
    return [f"{rel(path)}:{n}: an em-dash or en-dash" for n, line in enumerate(text.splitlines(), 1)
            if "—" in line or "–" in line]


# The records, the roadmap, and the pictures live in a hub, and this
# repository only points to them (decision ORC-0027).
GONE = ["docs/decisions", "docs/adr", "adr", "docs/roadmap.md", "docs/diagrams"]
POINTER_KEYS = ("document", "decisions", "roadmap", "watch")


def pointer() -> list[str]:
    problems = [f"{p} is back; the suite keeps it in the hub, not here" for p in GONE
                if os.path.exists(os.path.join(ROOT, p))]
    problems += [f"{rel(p)}: a diagram file is back; the suite's pictures live in the hub"
                 for p in files((".vantage.yaml",))]
    path = os.path.join(ROOT, "vantage.yaml")
    if not os.path.exists(path):
        return problems + ["vantage.yaml is missing: it names the suite's document, registry, and roadmap"]
    keys = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = re.match(r"([a-z]+):\s*(.*?)\s*$", line)
            if m:
                keys[m.group(1)] = m.group(2)
    problems += [f"vantage.yaml has no {k}" for k in POINTER_KEYS if not keys.get(k)]
    problems += [f"vantage.yaml names a {k}; an estate maps this repository to its own"
                 for k in ("hub", "workspace") if k in keys]
    return problems


LINK = re.compile(r"\]\(([^)#\s]+)(#[^)]*)?\)")


def links(path: str, text: str) -> list[str]:
    if not path.endswith(".md"):
        return []
    problems = []
    for n, line in enumerate(text.splitlines(), 1):
        for target, _ in LINK.findall(line):
            if re.match(r"[a-z][a-z0-9+.-]*:", target):
                continue
            if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(path), target))):
                problems.append(f"{rel(path)}:{n}: links to {target}, which is not there")
    return problems


def main() -> None:
    problems = pointer()
    for path in files():
        with open(path, encoding="utf-8") as f:
            text = f.read()
        problems += dashes(path, text) + links(path, text)
    for p in problems:
        print(p)
    if problems:
        sys.exit(f"{len(problems)} problem(s)")
    print("ok")


if __name__ == "__main__":
    main()
