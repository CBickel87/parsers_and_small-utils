import re

fname = 'tables.txt'

with open(fname, 'rt') as f:
    with open('out.txt', 'w') as f1:
        for line in f:
            match = re.findall(r'Table: (\w+)', line)
            exact_match = 'Redacted SQL code({})s Redacted SQL code ' \
                          'Redacted SQL code >> Redacted SQL code'.format(*match)
            f1.write(exact_match + '\n')
