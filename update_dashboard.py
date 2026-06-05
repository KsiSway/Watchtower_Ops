import re
import os

filepath = r'C:\Users\Lance\Watchtower_Ops\watchtower_gui.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

def replacer(match):
    indent = match.group(1)
    original_body = match.group(2)
    # Don't replace if it's already using trace_id
    if 'trace_id' in original_body or 'pass' in original_body or 'continue' in original_body:
        return match.group(0)
    
    # We preserve the original exception handling line
    new_body = f"{indent}except Exception as e:\n{indent}    trace_id = f\"REQ-{{str(uuid.uuid4())[:8].upper()}}\"\n{indent}    error_doc = generate_rfc9457_error_sync(\"dashboard-exception\", str(e), trace_id)\n{indent}    logger.error(\"dashboard_failure\", **error_doc)\n{indent}    {original_body.strip()}"
    return new_body

# Match simple single-line bodies
new_content = re.sub(r'(^[ \t]+)except Exception as e:\n[ \t]+([^\n]+)', replacer, content, flags=re.MULTILINE)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Replaced exception blocks')