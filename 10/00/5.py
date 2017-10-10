import os
from pathlib import *
p = PurePath('/etc')
print(str(p))
p = PureWindowsPath('c:/Program Files')
print(str(p))
print(bytes(p))
