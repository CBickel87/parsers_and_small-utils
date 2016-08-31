import glob
import os
import time
import csv
import re


with open("modifiedexcel.csv", "w", newline='') as f:
        for filename in glob.iglob(r'**', recursive=True):
            if re.search('\.((xlsx)|(xlsm)|(xls)|(xlm)|(csv))', filename):
                print(filename)
                listed_data = [(time.strftime("%m\%d\%y", (time.localtime(os.stat(filename).st_mtime)))),
                               (time.strftime("%H:%M", (time.localtime(os.stat(filename).st_mtime)))),
                               filename]
                writer = csv.writer(f)
                writer.writerow(listed_data)
