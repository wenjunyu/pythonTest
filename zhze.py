import re

line = '/src/linux.c'
regex_str = '\/.*\.c$'

if re.match(regex_str,line):
    print('yes')
else:
    print('no')
    