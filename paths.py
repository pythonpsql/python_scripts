source: https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

# Bad Code Example:

'''
data_folder = "source_data/text_files/"
file_to_open = data_folder + "raw_data.txt"
f = open(file_to_open)
print(f.read())
'''

# Reason: Windows uses forward slash for file paths, so hard-coding paths is inappropriate

# Old Solution:
import os.path

data_folder = os.path.join("source_data", "text_files")
file_to_open = os.path.join(data_folder, "raw_data.txt")
f = open(file_to_open)
print(f.read())

# Problem: Remembering the syntax


# Correct Solution
from pathlib import Path

data_folder = Path("source_data/text_files/")
file_to_open = data_folder / "raw_data.txt"


# Additional benefits of pathlib
from pathlib import Path

data_folder = Path("source_data/text_files/")
file_to_open = data_folder / "raw_data.txt"
print(file_to_open.read_text())

# Reason: No need to worry about closing the file

# Other file operations with pathlib
from pathlib import Path

filename = Path("source_data/text_files/raw_data.txt")
print(filename.name)
# prints "raw_data.txt"

print(filename.suffix)
# prints "txt"

print(filename.stem)
# prints "raw_data"

if not filename.exists():
        print("Oops, file doesn't exist!")
    else:
        print("Yay, the file exists!")

# All Details
https://docs.python.org/3/library/pathlib.html
