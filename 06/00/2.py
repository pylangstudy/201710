import itertools
for c in itertools.product([1,2,3,4,5],[1,2,3,4,5]): print(c)
for c in itertools.permutations([1,2,3,4,5],3): print(c)#順列?
for c in itertools.combinations([1,2,3,4,5],4): print(c)#組合せ?
for c in itertools.combinations_with_replacement([1,2,3,4,5],3): print(c)
for c in itertools.product('ABCD', repeat=2): print(c)
for c in itertools.permutations('ABCD', 2): print(c)
for c in itertools.combinations('ABCD', 2): print(c)
for c in itertools.combinations_with_replacement('ABCD', 2): print(c)
for c in itertools.compress('ABCDEF', [1,0,1,0,1,1]): print(c)
for c in itertools.count(10):
    print(c)
    if c == 20: break
for c in itertools.count(2.5, 0.5):
    print(c)
    if c == 5: break
for c in itertools.cycle('ABCD'):
    print(c)
    if c == 'D': break
for c in itertools.dropwhile(lambda x: x<5, [1,4,6,4,1]): print(c)
for c in itertools.filterfalse(lambda x: x%2, range(10)): print(c)
print([k for k, g in itertools.groupby('AAAABBBCCDAABBB')])
print([list(g) for k, g in itertools.groupby('AAAABBBCCD')])
for c in itertools.islice('ABCDEFG', 2): print(c)
for c in itertools.islice('ABCDEFG', 2, 4): print(c)
for c in itertools.islice('ABCDEFG', 2, None): print(c)
for c in itertools.islice('ABCDEFG', 0, None, 2): print(c)
for c in itertools.permutations('ABCD', 2): print(c)
for c in itertools.permutations(range(3)): print(c)
for c in itertools.product('ABCD', 'xy'): print(c)
for c in itertools.product(range(2), repeat=3): print(c)
for c in itertools.repeat(10, 3): print(c)
print(list(map(pow, range(10), itertools.repeat(2))))
for c in itertools.starmap(pow, [(2,5), (3,2), (10,3)]): print(c)
for c in itertools.takewhile(lambda x: x<5, [1,4,6,4,1]): print(c)
for c in itertools.tee([1,2,3,4,5]): print(c)
for c in itertools.zip_longest('ABCD', 'xy', fillvalue='-'): print(c)
