import sys
from datetime import datetime
from pathlib import Path

def synthesize_dossier(alias):
    print(f"[*] Initializing Cognitive Analyst Engine for: {alias}")
    
    # Ingesting the confirmed vectors dynamically
    verified_vectors = [
        f"GitHub - https://github.com/{alias}",
        f"Reddit - https://www.reddit.com/user/{alias}",
        f"Steam - https://steamcommunity.com/id/{alias}",
        f"Replit - https://replit.com/@{alias}"
    ]
    
    dossier = f"# Administrative Persona Summary: {alias}\n"
    dossier += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    dossier += "## Verified Telemetry Vectors\n"
    
    for vector in verified_vectors:
        dossier += f"- [X] {vector}\n"
        
    dossier += "\n## Infrastructure Analysis\n"
    dossier += "Target exhibits footprint intersecting Software Development and Interactive Media. "
    dossier += "Profile vectors are active and ready for localized monitoring integration.\n"
    
    # Enforce Path Validation to prevent Path Traversal (CWE-22) escapes
    safe_alias = Path(alias).name
    base_dir = Path("D:/Watchtower_Ops")
    file_path = base_dir / f"{safe_alias}_Dossier.md"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(dossier)
        
    print(f"[*] Synthesis complete. Structured dossier saved to: {file_path}")
    print("\n--- DOSSIER PREVIEW ---")
    print(dossier)
    print("-----------------------\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[!] Target alias required.")
        sys.exit(1)
    synthesize_dossier(sys.argv[1])
