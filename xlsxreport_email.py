import glob
import os
import time
import re
import subprocess
from datetime import datetime


paths = [r'c:\Folder1\Folder2\**', r'c:\Folder1\Folder2\**', r'c:\Folder1\Folder2\**']
count = 0

with open(r"\\server\folder\outdated_reports.txt", "w", newline='') as f:
    f.write("Reports older than midnight on \\\\server\\c$\\folder\n\n")
    for path in paths:
        for filename in glob.iglob(path, recursive=True):
            if re.search('^((?!pricing|consignment|daily sales).)*$', filename, flags=re.IGNORECASE):
                if re.search('\.((xlsx)|(xlsm)|(xls)|(xlm)|(csv))', filename):
                    seconds_since_midnight = (datetime.now() - datetime.now().replace
                    (hour=0, minute=0, second=0, microsecond=0)).total_seconds()
                    modified_date = os.path.getmtime(filename)
                    total = (time.time() - modified_date)
                    if round(total) >= round(seconds_since_midnight):
                        count += 1
                        print(
                            time.strftime("%m\%d\%y - %H:%M", time.localtime(modified_date)) + " | " + filename + "\n")
                        f.write(
                            time.strftime("%m\%d\%y - %H:%M", time.localtime(modified_date)) + " | " + filename + "\n")

if count > 0:
    p = subprocess.Popen(['powershell.exe', '-ExecutionPolicy', 'ByPass', r'C:\Scripts\SendEmail.ps1'])
    p.communicate()

