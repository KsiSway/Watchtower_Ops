import re

path = r'd:\Watchtower_Ops\NotebookLM - 2026-06-11.md'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'^\* \* \*$', '---', content, flags=re.MULTILINE)
content = re.sub(r'^(\s*[-*+\d+\.])   ', r'\1 ', content, flags=re.MULTILINE)
content = re.sub(r'^```\s*$', '```text', content, flags=re.MULTILINE)
content = re.sub(r'(?<!<)(https?://[^\s>\"\']+)(?!>)', r'<\1>', content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Markdown scrub complete.')
