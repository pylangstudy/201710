import os
from pathlib import *
print(PureWindowsPath('c:/Program Files/').drive)
print(PureWindowsPath('/Program Files/').drive)
print(PurePosixPath('/etc').drive)
print(PureWindowsPath('//host/share/foo.txt').drive)

print(PureWindowsPath('c:/Program Files/').root)
print(PureWindowsPath('c:Program Files/').root)
print(PurePosixPath('/etc').root)
print(PureWindowsPath('//host/share').root)

print(PureWindowsPath('c:/Program Files/').anchor)
print(PureWindowsPath('c:Program Files/').anchor)
print(PurePosixPath('/etc').anchor)
print(PureWindowsPath('//host/share').anchor)

p = PureWindowsPath('c:/foo/bar/setup.py')
print(p.parents[0])
print(p.parents[1])
print(p.parents[2])

p = PurePosixPath('/a/b/c/d')
print(p.parent)

p = PurePosixPath('/')
print(p.parent)
p = PurePosixPath('.')
print(p.parent)

p = PurePosixPath('foo/..')
print(p.parent)

print(PurePosixPath('my/library/setup.py').name)
print(PureWindowsPath('//some/share/setup.py').name)
print(PureWindowsPath('//some/share').name)

print(PurePosixPath('my/library/setup.py').suffix)
print(PurePosixPath('my/library.tar.gz').suffix)
print(PurePosixPath('my/library').suffix)

print(PurePosixPath('my/library.tar.gar').suffixes)
print(PurePosixPath('my/library.tar.gz').suffixes)
print(PurePosixPath('my/library').suffixes)

print(PurePosixPath('my/library.tar.gz').stem)
print(PurePosixPath('my/library.tar').stem)
print(PurePosixPath('my/library').stem)

p = PureWindowsPath('c:\\windows')
print(str(p))
print(p.as_posix())

p = PurePosixPath('/etc/passwd')
print(p.as_uri())
p = PureWindowsPath('c:/Windows')
print(p.as_uri())


print(PurePosixPath('/a/b').is_absolute())
print(PurePosixPath('a/b').is_absolute())

print(PureWindowsPath('c:/a/b').is_absolute())
print(PureWindowsPath('/a/b').is_absolute())
print(PureWindowsPath('c:').is_absolute())
print(PureWindowsPath('//some/share').is_absolute())

print(PureWindowsPath('nul').is_reserved())
print(PurePosixPath('nul').is_reserved())

print(PurePosixPath('/etc').joinpath('passwd'))
print(PurePosixPath('/etc').joinpath(PurePosixPath('passwd')))
print(PurePosixPath('/etc').joinpath('init.d', 'apache2'))
print(PureWindowsPath('c:').joinpath('/Program Files'))

print(PurePath('a/b.py').match('*.py'))
print(PurePath('/a/b/c.py').match('b/*.py'))
print(PurePath('/a/b/c.py').match('a/*.py'))

print(PurePath('/a.py').match('/*.py'))
print(PurePath('a/b.py').match('/*.py'))

print(PureWindowsPath('b.py').match('*.PY'))

p = PurePosixPath('/etc/passwd')
print(p.relative_to('/'))
print(p.relative_to('/etc'))
#p.relative_to('/usr')

p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
print(p.with_name('setup.py'))
p = PureWindowsPath('c:/')
#print(p.with_name('setup.py'))

p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
print(p.with_suffix('.bz2'))
p = PureWindowsPath('README')
print(p.with_suffix('.txt'))


