import os
from pathlib import *
p = PurePath('/etc')
print(os.fspath(p))
