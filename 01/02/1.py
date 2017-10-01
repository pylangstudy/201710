from decimal import Decimal, getcontext

getcontext().prec = 20
u, v, w = Decimal(11111113), Decimal(-11111111), Decimal('7.51111111')
print((u + v) + w)
print(u + (v + w))

u, v, w = Decimal(20000), Decimal(-6), Decimal('6.0000003')
print((u*v) + (u*w))
print(u * (v+w))

