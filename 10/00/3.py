from pathlib import *
p = PurePath('/etc')
print(p)
print(p / 'init.d' / 'apache2')
q = PurePath('bin')
print('/usr' / q)

