import os

source_file = "D:\\Watchtower_Ops\\bigaistudio.md"
dest_dir = "D:\\Watchtower_Ops\\watchtower_react_gui\\src"

files_to_extract = [
    {"name": "components/FileAnalyzer.tsx", "start": 1, "end": 1295},
    {"name": "components/FileList.tsx", "start": 1297, "end": 2043},
    {"name": "components/GoogleConnection.tsx", "start": 2045, "end": 2286},
    {"name": "components/SystemActivityLog.tsx", "start": 2288, "end": 2463},
    {"name": "components/WatchtowerDashboard.tsx", "start": 2465, "end": 3899},
    {"name": "data/mockWorkspace.ts", "start": 3901, "end": 4140},
    {"name": "index.css", "start": 4142, "end": 4457},
    {"name": "main.tsx", "start": 4459, "end": 4468},
    {"name": "types.ts", "start": 4470, "end": 4526}
]

with open(source_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for file_info in files_to_extract:
    start_idx = file_info["start"] - 1
    end_idx = file_info["end"]
    
    file_content = "".join(lines[start_idx:end_idx])
    
    file_path = os.path.join(dest_dir, file_info["name"])
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(file_content)
        
    print(f"Extracted {file_info['name']}")
