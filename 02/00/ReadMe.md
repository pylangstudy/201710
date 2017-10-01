# [9.5. fractions — 有理数](https://docs.python.jp/3/library/fractions.html#module-fractions)

< [9.4. decimal — 十進固定及び浮動小数点数の算術演算](https://docs.python.jp/3/library/decimal.html#module-decimal) < [9. 数値と数学モジュール](https://docs.python.jp/3/library/numeric.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/fractions.py](https://github.com/python/cpython/tree/3.6/Lib/fractions.py)

> fractions モジュールは有理数計算のサポートを提供します。

> Fraction インスタンスは一対の整数、他の有理数、または文字列から生成されます。

* class fractions.Fraction(numerator=0, denominator=1)
* class fractions.Fraction(other_fraction)
* class fractions.Fraction(float)
* class fractions.Fraction(decimal)
* class fractions.Fraction(string)

属性|説明
----|----
numerator|有理数を既約分数で表したときの分子。
denominator|有理数を既約分数で表したときの分母。
from_float(flt)|このクラスメソッドは float である flt の正確な値を表す Fraction を構築します。 Fraction.from_float(0.3) と Fraction(3, 10) の値は同じでないことに注意してください 。
__floor__()|最大の int <= self を返します。このメソッドは math.floor() 関数からでもアクセスできます:
__ceil__()|最小の int >= self を返します。このメソッドは math.ceil() 関数からでもアクセスできます。
__round__(), __round__(ndigits)|第一のバージョンは、 self に最も近い int を偶数丸めで返します。第二のバージョンは、このメソッドは self に最も近い Fraction(1, 10**ndigits) の倍数 (論理的に、 ndigits が負なら) を、これも偶数丸めで丸めます。 round() 関数からでもアクセスできます。
fractions.gcd(a, b)|整数 a と b の最大公約数を返します。a も b もゼロでないとすると、gcd(a, b) の絶対値は a と b の両方を割り切る最も大きな整数です。gcd(a, b) は b がゼロでなければ b と同じ符号になります。そうでなければ a の符号を取ります。gcd(0, 0) は 0 を返します。

> 参考

> numbers モジュール

>    数値の塔を作り上げる抽象基底クラス。

```python
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
```
```sh
$ python 0.py 
1/2
1/2
1/8
-1/5
-1/6
1414213/1000000
-1/8
-1
2
1/4
1/8
355/113
4503599627370497/9007199254740992
1/2
11/10
3
0
0
-1/2
7
```

