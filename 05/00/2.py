#from itertools import *
import itertools
for c in itertools.product([1,2,3,4,5],[1,2,3,4,5]): print(c)
for c in itertools.permutations([1,2,3,4,5],3): print(c)#順列?
for c in itertools.combinations([1,2,3,4,5],4): print(c)#組合せ?
for c in itertools.combinations_with_replacement([1,2,3,4,5],3): print(c)
for c in itertools.product('ABCD', repeat=2): print(c)
for c in itertools.permutations('ABCD', 2): print(c)
for c in itertools.combinations('ABCD', 2): print(c)
for c in itertools.combinations_with_replacement('ABCD', 2): print(c)
