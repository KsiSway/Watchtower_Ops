import os

source_file = "D:\\Watchtower_Ops\\bigaistudio.md"
dest_file = "D:\\Watchtower_Ops\\watchtower_react_gui\\server.ts"

with open(source_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

file_content = "".join(lines[9494:10034]) # assuming ~10034 is the end

with open(dest_file, 'w', encoding='utf-8') as f:
    f.write(file_content)
    
print("Extracted server.ts")
