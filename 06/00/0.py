import itertools
import operator
for i in itertools.accumulate([1,2,3,4,5]): print(i)
for i in itertools.accumulate([1,2,3,4,5], operator.mul): print(i)
