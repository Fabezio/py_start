import os
import glob

filenames = glob.glob("*.txt")
# print (filenames, )
for file in filenames:
    print("")
    print (f"{file}, {os.path.getsize(file)} octets")
    with open(file, "r") as f:
        print(f.read())

