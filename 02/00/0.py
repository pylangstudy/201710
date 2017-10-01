import fractions
import decimal
import math
print(fractions.Fraction(1,2))
print(fractions.Fraction(0.5))
print(fractions.Fraction(decimal.Decimal(0.125)))
print(fractions.Fraction('-1/5'))
print(fractions.Fraction(fractions.Fraction('-1/6')))
print(fractions.Fraction('1.414213 \t\n'))
print(fractions.Fraction('-.125'))

f = fractions.Fraction('-1/2')
print(f.numerator)
print(f.denominator)
print(f.from_float(0.25))
print(f.from_decimal(decimal.Decimal(0.125)))

print(fractions.Fraction('3.1415926535897932').limit_denominator(1000))
print(fractions.Fraction(math.cos(math.pi/3)))
print(fractions.Fraction(math.cos(math.pi/3)).limit_denominator())
print(fractions.Fraction(1.1).limit_denominator())
print(math.floor(fractions.Fraction(355, 113)))

print(f.__ceil__())
print(f.__round__())
print(f.__round__(7))
print(fractions.gcd(35,49))
