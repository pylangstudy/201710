import operator
a = 100
b = 1
print('a=',a)
print('b=',b)
print(operator.iadd(a, b))
print('a=',a)
print('b=',b)
print(operator.add(a, b))
print('a=',a)
print('b=',b)

s = ['h', 'e', 'l', 'l', 'o']
print('s=',s)
operator.iadd(s, [' ', 'w', 'o', 'r', 'l', 'd'])
print('s=',s)

