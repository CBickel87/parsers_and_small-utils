import glob
import os, time

with open("named_file.txt", "w") as f:
    for filename in glob.glob('*.xlsx'):
        f.write(time.asctime(time.localtime(os.stat(filename).st_mtime)) + "|" + filename + "\n")
