import fnmatch
import glob
import os

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.py'):
        print(file)

print(fnmatch.fnmatchcase('0.py','*.py'))
print(fnmatch.filter(['0.py','1.py'], '*.py'))

import re
regex = fnmatch.translate('*.txt')
print(regex)
reobj = re.compile(regex)
print(reobj.match('foobar.txt'))

