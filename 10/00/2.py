from pathlib import *
print(PurePosixPath('foo') == PurePosixPath('FOO'))
print(PureWindowsPath('foo') == PureWindowsPath('FOO'))
print(PureWindowsPath('FOO') in { PureWindowsPath('foo') })
print(PureWindowsPath('C:') < PureWindowsPath('d:'))
print(PureWindowsPath('foo') == PurePosixPath('foo'))
print(PureWindowsPath('foo') < PurePosixPath('foo'))

