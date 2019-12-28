# Show all of the files in the directory, as well as how long ago the directory was modified.
import os

directory = "./books"

for files in os.listdir(directory):
    print(files)
    if os.path.isdir(directory):
        file_with_path = os.path.join(directory, files)
        mtime = os.stat(file_with_path).st_mtime
