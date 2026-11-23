"""Standard-library static checks. Does not execute notebooks or download data."""
import ast
import base64
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []
COUNTS = {"notebooks": 0, "code_cells": 0, "attachment_refs": 0, "local_links": 0}


def check_links(text, base, label, attachments=None):
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    text = re.sub(r'`[^`\n]*`', '', text)
    # Math such as STA[s^2](t,x) is not a Markdown link.
    text = re.sub(r'\$\$.*?\$\$', '', text, flags=re.S)
    text = re.sub(r'\$[^$\n]*\$', '', text)
    for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
        target = target.split(' "', 1)[0].strip('<>')
        if target.startswith("attachment:"):
            COUNTS['attachment_refs'] += 1
            name = unquote(target[len('attachment:'):])
            if attachments is None or name not in attachments:
                ERRORS.append(f"{label}: missing attachment {name}")
            continue
        if re.match(r"(?:https?:|mailto:|data:|#)", target):
            continue
        path = unquote(target.split('#', 1)[0])
        if not path:
            continue
        COUNTS['local_links'] += 1
        if not (base / path).exists():
            ERRORS.append(f"{label}: missing local target {path}")


for path in sorted(ROOT.rglob('*.md')):
    check_links(path.read_text(encoding='utf-8'), path.parent, str(path.relative_to(ROOT)))

for path in sorted((ROOT / 'tutorials' / 'xdas').glob('*.ipynb')):
    COUNTS['notebooks'] += 1
    notebook = json.loads(path.read_text(encoding='utf-8'))
    if notebook.get('nbformat') != 4:
        ERRORS.append(f'{path.name}: expected nbformat 4')
    ids = []
    for index, cell in enumerate(notebook.get('cells', [])):
        label = f'{path.name} cell {index}'
        if 'id' in cell:
            ids.append(cell['id'])
        source = ''.join(cell.get('source', []))
        if cell.get('cell_type') == 'code':
            COUNTS['code_cells'] += 1
            try:
                ast.parse(source, filename=label)
            except SyntaxError as exc:
                ERRORS.append(f'{label}: {exc}')
        elif cell.get('cell_type') == 'markdown':
            attachments = cell.get('attachments', {})
            check_links(source, path.parent, label, attachments)
            for name, bundle in attachments.items():
                for mime, value in bundle.items():
                    if mime.startswith('image/') and mime != 'image/svg+xml':
                        try:
                            raw = base64.b64decode(''.join(value) if isinstance(value, list) else value, validate=True)
                            if mime == 'image/png' and not raw.startswith(b'\x89PNG\r\n\x1a\n'):
                                ERRORS.append(f'{label}: invalid PNG {name}')
                        except Exception as exc:
                            ERRORS.append(f'{label}: invalid attachment {name}: {exc}')
    if len(ids) != len(set(ids)):
        ERRORS.append(f'{path.name}: duplicate cell ids')

if COUNTS['notebooks'] != 7:
    ERRORS.append(f"expected 7 notebooks, found {COUNTS['notebooks']}")

print(json.dumps({'counts': COUNTS, 'errors': ERRORS}, ensure_ascii=False, indent=2))
print('Static checks only: no dependency installation, scientific execution or rendering verification.')
sys.exit(bool(ERRORS))
