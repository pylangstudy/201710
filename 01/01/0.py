from decimal import *
#from decimal import localcontext
with localcontext() as ctx:
    ctx.prec = 3   # Perform a high precision calculation
    s = Decimal(10000.12345)
    print(s)
#s = +s
print(s)

