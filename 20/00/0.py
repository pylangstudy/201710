import shutil
fnma = 'a.txt'
fnmb = 'b.txt'
with open(fnma) as a:
    with open(fnmb, 'w') as b:
        shutil.copyfileobj(a, b)

#shutil.copyfile(fnma, fnma)#shutil.SameFileError: 'a.txt' and 'a.txt' are the same file
shutil.copyfile(fnma, fnmb)
shutil.copymode(fnma, fnmb)
shutil.copystat(fnma, fnmb)

shutil.copy(fnma, fnmb)
shutil.copy2(fnma, fnmb)

p = shutil.ignore_patterns('*.txt')
print(p)
#shutil.copytree('a', 'b', ignore=p)
#shutil.rmtree('b')
print(shutil.rmtree.avoids_symlink_attacks)
#shutil.move(src, dst)
print(shutil.disk_usage('.'))
shutil.chown('a.txt', 'mint')
print(shutil.which('python'))

import logging
def _logpath(path, names):
    logging.info('Working in %s', path)
    return []   # nothing will be ignored
#shutil.copytree('a', 'b', ignore=_logpath)
#shutil.rmtree('b')

import os, stat
def remove_readonly(func, path, _):
    "Clear the readonly bit and reattempt the removal"
    os.chmod(path, stat.S_IWRITE)
    func(path)
shutil.rmtree('c', onerror=remove_readonly)


