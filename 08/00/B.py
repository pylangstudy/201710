from functools import singledispatch
import decimal
@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)
@fun.register(int)
def _(arg, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)
@fun.register(list)
def _(arg, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)

def nothing(arg, verbose=False):
    print("Nothing.")
fun.register(type(None), nothing)

@fun.register(float)
@fun.register(decimal.Decimal)
def fun_num(arg, verbose=False):
    if verbose:
        print("Half of your number:", end=" ")
    print(arg / 2)

print(fun.dispatch(float))
print(fun.dispatch(dict))

print(fun.registry.keys())
print(fun.registry[float])
print(fun.registry[object])

