import itertools
for c in itertools.count(10):
    print(c)
    if c == 20: break
for c in itertools.cycle('CDEFGAB'):
    print(c)
    if c == 'B': break
for c in itertools.repeat(10, 3): print(c)
    

