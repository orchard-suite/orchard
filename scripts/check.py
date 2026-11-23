#!/usr/bin/env python3
"""Check this repository's documents: python3 scripts/check.py.

Fails, naming each problem, on:
- an em-dash or en-dash in a document, a skill, or the diagram source;
- a decision number used twice or skipped;
- a roadmap row that names no decision and no build order step;
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


def files() -> list[str]:
    out = []
    for folder, dirs, names in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in names:
            if name.endswith(TEXT):
                out.append(os.path.join(folder, name))
    return sorted(out)


def rel(path: str) -> str:
    return os.path.relpath(path, ROOT)


def dashes(path: str, text: str) -> list[str]:
    if path == os.path.abspath(__file__):
        return []
    return [f"{rel(path)}:{n}: an em-dash or en-dash" for n, line in enumerate(text.splitlines(), 1)
            if "—" in line or "–" in line]


def decisions() -> list[str]:
    folder = os.path.join(ROOT, "docs", "decisions")
    numbers = sorted(int(m.group(1)) for name in os.listdir(folder) if (m := re.match(r"(\d{4})-", name)))
    problems = [f"docs/decisions: number {n:04d} is used twice" for n in sorted(set(numbers)) if numbers.count(n) > 1]
    want = list(range(1, len(set(numbers)) + 1))
    if sorted(set(numbers)) != want:
        problems.append(f"docs/decisions: numbers are not 0001 to {len(set(numbers)):04d} with none skipped")
    return problems


def roadmap() -> list[str]:
    path = os.path.join(ROOT, "docs", "roadmap.md")
    if not os.path.exists(path):
        return ["docs/roadmap.md is missing"]
    problems = []
    known = {name[:4] for name in os.listdir(os.path.join(ROOT, "docs", "decisions"))}
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) != 6 or not cells[0].isdigit():
                continue
            source = cells[3]
            numbers = re.findall(r"\b\d{4}\b", source)
            if not numbers and "Build order" not in source:
                problems.append(f"docs/roadmap.md:{n}: row {cells[0]} names no decision and no build order step")
            problems += [f"docs/roadmap.md:{n}: row {cells[0]} names decision {d}, which does not exist"
                         for d in numbers if d not in known]
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
    problems = decisions() + roadmap()
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
