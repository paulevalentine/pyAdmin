import re
from pathlib import Path
p = Path("../")

files = []
for p in p.iterdir():
    if p.is_file():
        files.append(p.name)

print(files)

