import random
random.seed()
s = random.getstate()
print(s)
random.setstate(s)
print(random.getrandbits(100))

