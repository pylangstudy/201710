import os
from pathlib import *
p = PurePath('/usr/bin/python3')
print(p.parts)

p = PureWindowsPath('c:/Program Files/PSF')
print(p.parts)
