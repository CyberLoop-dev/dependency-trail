#!/usr/bin/env python3
"""Inspect direct dependencies declared in a Python pyproject.toml."""

import argparse
import json
import sys
import tomllib
from pathlib import Path


def read_dependencies(path: Path) -> list[str]:
    with path.open("rb") as stream:
        data = tomllib.load(stream)
    project = data.get("project", {})
    dependencies = project.get("dependencies", [])
    return sorted(set(str(item) for item in dependencies))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="Path to pyproject.toml")
    parser.add_argument("--json", action="store_true", help="Print JSON")
    args = parser.parse_args()

    try:
        dependencies = read_dependencies(args.file)
    except (OSError, tomllib.TOMLDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(dependencies, indent=2))
    else:
        print(f"Direct dependencies ({len(dependencies)}):")
        for dependency in dependencies:
            print(f"- {dependency}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
