import re
import sys
from pathlib import Path

path = Path(__file__).parent / "NotebookLM - 2026-06-11.md"
try:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print(f"ERROR: File not found: {path}")
    sys.exit(1)
except IOError as e:
    print(f"ERROR: Cannot read file {path}: {e}")
    sys.exit(1)

content = re.sub(r'^\* \* \*$', '---', content, flags=re.MULTILINE)
content = re.sub(r'^([-*+]|\d+\.)\s{3,}', r'\1 ', content, flags=re.MULTILINE)
content = re.sub(r'^```\s*$', '```text', content, flags=re.MULTILINE)
content = re.sub(r'(?<!<)(https?://[^\s>"\']+(\(\w+\))*[^\s>"\']*?)(?!>)', r'<\1>', content)

try:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Markdown scrub complete.')
except IOError as e:
    print(f"ERROR: Cannot write to file {path}: {e}")
    sys.exit(1)
