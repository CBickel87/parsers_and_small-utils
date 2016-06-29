import re
import glob
import time


def readfiles(filenames):
    for file in filenames:
        with open(file, 'r') as f:
            for line in f:
                searchit(line, file)


def searchit(lines, file):
    tablesearch = re.compile(r'table (\w+)')  # Find word 'table' then grab 1 word after
    tables = tablesearch.findall(lines)
    dumpsearch = re.compile(r'Dumped (\d+)|Loaded (\d+)')  # Find word Dumped or Loaded and grab 1 word after
    dumps = dumpsearch.findall(lines)

    logfile = time.strftime("%m-%d-%y_%H" + file +'.txt')  # Naming convention for output file

    if tables:  # If tables search was not blank then write to output file
        print('{} | '.format(*tables))
        with open(logfile, 'a')as f:
            f.write('{} | '.format(*tables))
    elif dumps:  # If dumps search was not blank then write to output file
        clean = [x for x in dumps[0] if x != '']  # Comprehension to clean Nonetype elements
        print('{} \n'.format(*clean))
        with open(logfile, 'a')as f:
            f.write('{} \n'.format(*clean))


def main():
    print('Starting Parsing')
    filenames = glob.glob('*.out')  # Get file names of all relative .out files
    readfiles(filenames)


main()
