import sys
from pathlib import Path

def consolidate_and_chunk(source_dir: str, output_prefix: str, word_limit: int = 490000) -> None:
    target_path = Path(source_dir)
    output_dir = Path(output_prefix).parent
    base_name = Path(output_prefix).stem
    
    current_chunk = 1
    current_word_count = 0
    
    # Initialize the primary payload buffer
    out_file = output_dir / f"{base_name}_{current_chunk:02d}.md"
    master_file = out_file.open('w', encoding='utf-8')
    print(f"Targeting active payload chunk: {out_file.name}")
    
    for ext in ('*.md', '*.txt'):
        for file_path in target_path.rglob(ext):
            # Prevent recursive ingestion of our own output files
            if base_name in file_path.name:
                continue
            
            try:
                content = file_path.read_text(encoding='utf-8', errors='replace')
                file_words = len(content.split())
                
                # Payload weight evaluation and chunk rotation
                if current_word_count + file_words > word_limit:
                    master_file.close()
                    current_chunk += 1
                    current_word_count = 0
                    
                    out_file = output_dir / f"{base_name}_{current_chunk:02d}.md"
                    master_file = out_file.open('w', encoding='utf-8')
                    print(f"Threshold reached. Rotating buffer to: {out_file.name}")
                
                master_file.write(f"\n\n# --- SOURCE ORIGIN: {file_path.name} --- \n\n")
                master_file.write(content)
                current_word_count += file_words
                
            except Exception as e:
                master_file.write(f"\n[ERROR READING FILE: {e}]\n")
                
    master_file.close()
    print("Intelligence consolidation complete. All payloads optimized for ingestion.")

if __name__ == "__main__":
    DIR_PATH = r"D:\Watchtower_Ops"
    OUT_PREFIX = r"D:\Watchtower_Ops\WATCHTOWER_MASTER_CACHE.md"
    
    consolidate_and_chunk(DIR_PATH, OUT_PREFIX)
