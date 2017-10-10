from pathlib import Path
p = Path('.')
print([x for x in p.iterdir() if x.is_dir()])
print(list(p.glob('**/*.py')))

p = Path('/etc')
q = p / 'init.d' / 'reboot'
print(q)
print(q.resolve())

print(q.exists())
print(q.is_dir())
with q.open() as f: f.readline()
