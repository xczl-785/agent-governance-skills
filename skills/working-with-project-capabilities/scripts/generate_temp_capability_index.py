#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

QUICK_READ_PATTERN = re.compile(r'^##\s+Quick Read\s*$', re.MULTILINE)
BULLET_PATTERN = re.compile(r'^-\s+\*\*(?P<key>[^*]+)\*\*:\s*(?P<value>.*)$')
SECTION_BULLET_PATTERN = re.compile(r'^\s*-\s+(.*)$')

FIELDS = ["id", "name", "summary", "entry_points", "shared_with", "path"]


def extract_quick_read(text: str) -> dict[str, str]:
    match = QUICK_READ_PATTERN.search(text)
    if not match:
        return {}

    lines = text[match.end():].splitlines()
    data: dict[str, str] = {}
    current_key: str | None = None
    current_items: list[str] = []

    def flush() -> None:
        nonlocal current_key, current_items
        if current_key is None:
            return
        if current_items:
            data[current_key] = '; '.join(current_items)
        current_key = None
        current_items = []

    for raw_line in lines:
        line = raw_line.rstrip()
        if line.startswith('---') or line.startswith('## '):
            break

        bullet = BULLET_PATTERN.match(line)
        if bullet:
            flush()
            key = bullet.group('key').strip().lower()
            value = bullet.group('value').strip()
            if value:
                data[key] = value
            else:
                current_key = key
            continue

        section_item = SECTION_BULLET_PATTERN.match(line)
        if section_item and current_key:
            current_items.append(section_item.group(1).strip())

    flush()
    return data


def scan_docs(root: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted(root.rglob('*.md')):
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            text = path.read_text(encoding='utf-8-sig')
        quick = extract_quick_read(text)
        if not quick:
            continue
        row = {field: quick.get(field, 'none') for field in FIELDS if field != 'path'}
        capability_id = row.get('id', 'none')
        if capability_id == 'none' or '{' in capability_id or '}' in capability_id:
            continue
        row['path'] = str(path)
        rows.append(row)
    return rows


def to_markdown(rows: list[dict[str, str]]) -> str:
    lines = [
        '# Temporary Capability Index',
        '',
        '| id | name | summary | entry_points | shared_with | path |',
        '| --- | --- | --- | --- | --- | --- |',
    ]
    for row in rows:
        vals = [row.get(field, 'none').replace('|', '\\|') for field in FIELDS]
        lines.append('| ' + ' | '.join(vals) + ' |')
    return '\n'.join(lines) + '\n'


def main() -> None:
    parser = argparse.ArgumentParser(description='Generate a temporary capability index from capability docs.')
    parser.add_argument('directory', help='Directory to scan')
    args = parser.parse_args()

    root = Path(args.directory)
    rows = scan_docs(root)
    print(to_markdown(rows), end='')


if __name__ == '__main__':
    main()
