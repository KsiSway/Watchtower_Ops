# DEPLOYMENT: Watchtower_Ops/osint_notebooklm_bridge.py
# Aggregation Bridge for Google NotebookLM (Pam Records)

import os
import glob
import sys
import json
import pyperclip

SOURCE_DIR = r"C:\Users\Lance\pam_archive\data\processed_for_notebooklm"
MASTER_FILE = r"C:\Users\Lance\pam_archive\data\Pam_Records_Master.md"

def compile_dossier():
    """Aggregates all individual scraped text files into a single NotebookLM-optimized dossier."""
    files = glob.glob(os.path.join(SOURCE_DIR, "*.txt"))
    if not files:
        return {"status": "error", "message": "No processed text files found in the archive directory."}
    
    dossier_content = f"# Pam Records - Master Dossier\n\n"
    dossier_content += "Compiled from Watchtower OSINT Scrapers\n"
    dossier_content += "=" * 50 + "\n\n"
    
    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            dossier_content += f"## Document Source: {os.path.basename(file_path)}\n\n"
            dossier_content += f"{content}\n\n"
            dossier_content += "=" * 50 + "\n\n"
            
    # Write to master file
    with open(MASTER_FILE, "w", encoding="utf-8") as f:
        f.write(dossier_content)
        
    # Copy to clipboard for instant paste into NotebookLM
    try:
        pyperclip.copy(dossier_content)
        clipboard_status = "True - Ready for immediate Ctrl+V into NotebookLM 'Copied Text' source."
    except Exception as e:
        clipboard_status = f"False - Clipboard access failed: {e}"
    
    return {
        "status": "success",
        "analysis": f"Aggregated {len(files)} files into single dossier.",
        "master_file": MASTER_FILE,
        "clipboard": clipboard_status
    }

if __name__ == "__main__":
    result = compile_dossier()
    print(json.dumps(result, indent=2))
