# Return a dictionary in which the keys are the names of files
# in that directory, and the values are the file sizes. You can use os.listdir or glob.glob to get the files, but because only regular files have sizes, you’ll want to filter the results using methods from os.path. To determine the file size, you can use os.stat or (if you prefer) just check the length of the string resulting from reading the file.

import os
from os import listdir
import glob

dir = "./example_dir"

# Option 1: with listdir
file_sizes = {
    os.path.join(dir, file): os.stat(os.path.join(dir, file)).st_size
    for file in listdir(dir)
    if os.path.isfile
}

print(file_sizes)

# Option 2: with glob.glob
file_sizes = {file: os.stat(file).st_size for file in glob.glob("./example_dir/*")}
