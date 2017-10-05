#from itertools import *
import itertools
for c in itertools.accumulate([1,2,3,4,5]): print(c)
for c in itertools.chain('ABC', 'DEF'): print(c)
for c in itertools.chain.from_iterable(['ABC', 'DEF']): print(c)
for c in itertools.compress('ABCDEF', [1,0,1,0,1,1]): print(c)
for c in itertools.dropwhile(lambda x: x<5, [1,4,6,4,1]): print(c)
for c in itertools.filterfalse(lambda x: x%2, range(10)): print(c)
for c in itertools.groupby([1,2,3,4,5], lambda x: x%2): print(c)
for c in itertools.islice('ABCDEFG', 2, None): print(c)
for c in itertools.starmap(pow, [(2,5), (3,2), (10,3)]): print(c)
for c in itertools.takewhile(lambda x: x<5, [1,4,6,4,1]): print(c)
for c in itertools.tee([1,2,3,4,5], 2): print(c)
for c in itertools.zip_longest('ABCD', 'xy', fillvalue='-'): print(c)
