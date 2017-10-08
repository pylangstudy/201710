import functools
#from functools import *
"""
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
"""
functools.reduce(lambda x,y: print(x,y), [1,2,3])
