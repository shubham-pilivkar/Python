import os
oldFile = "Sample3.txt"
newFile = "Renamed_by_Python"

with open(oldFile) as f:
    content = f.read()
with open(newFile, "w") as f:
    f.write(content)

os.remove(oldFile)