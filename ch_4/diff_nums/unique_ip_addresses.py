import os, sys

path = "/var/log/"
dirs = os.listdir(path)


for file in dirs:
    print(file)


for file in dirs:
    print(os.path.splitext(file)[-1])
