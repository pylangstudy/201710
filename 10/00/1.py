#from pathlib import Path
from pathlib import *

print(PurePath('setup.py'))
print(PurePath('foo', 'some/path', 'bar'))
print(PurePath(Path('foo'), Path('bar')))
print(PurePath())
print(PurePath('/etc', '/usr', 'lib64'))

print(PureWindowsPath('c:/Windows', 'd:bar'))
print(PureWindowsPath('c:/Windows', '/Program Files'))
print(PurePath('foo//bar'))
print(PurePath('foo/./bar'))
print(PurePath('foo/../bar'))

