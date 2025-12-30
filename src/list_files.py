import re
from pathlib import Path

""" Function to list the file in folders based on date naming """
path = Path("/Users/paulvalentine/Library/CloudStorage/Dropbox/Structensor/Jobs/Rowland Homes/6504 Roseacre/02 Internal Documents/02 Issued")
output_file = Path("files.txt")

# get a list of the directories in the designated path
dirs = [p for p in path.iterdir() if p.is_dir()]

# ensure that sort is based on the date reference
def get_sort_key(folder_path):
    match = re.search(r'(\d{8})', folder_path.name)
    return match.group(1) if match else folder_path.name

sorted_dirs = sorted(dirs, key=get_sort_key)

with open(output_file, "w") as f:
    for folder in sorted_dirs:
        if folder.is_dir():
            f.write(f"\nThe documents in {folder.name}:\n")
            sub_path = path / folder.name
            for sub_folder in sub_path.iterdir():
                if sub_folder.is_dir() and sub_folder.name != ".DS_Store":
                    f.write(f"\t{sub_folder.name}\n")
                    for file in sub_folder.iterdir():
                        f.write(f"\t \t{file.name}\n")
            for file in folder.iterdir():
                if file.is_file() and file.name != ".DS_Store":
                    f.write(f"\t{file.name}\n")

