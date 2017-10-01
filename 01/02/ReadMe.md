# [9.4.7. 浮動小数点数に関する注意](https://docs.python.jp/3/library/decimal.html#floating-point-notes)

< [9.4. decimal — 十進固定及び浮動小数点数の算術演算](https://docs.python.jp/3/library/decimal.html#module-decimal) < [9. 数値と数学モジュール](https://docs.python.jp/3/library/numeric.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/decimal.py](https://github.com/python/cpython/tree/3.6/Lib/decimal.py)

## [9.4.7.1. 精度を上げて丸め誤差を抑制する](https://docs.python.jp/3/library/decimal.html#mitigating-round-off-error-with-increased-precision)

> 十進浮動小数点数を使うと、十進数表現による誤差を抑制できます (0.1 を正確に表現できるようになります); しかし、ゼロでない桁が一定の精度を越えている場合には、演算によっては依然として値丸めによる誤差を引き起こします。

> 値丸めによる誤差の影響は、桁落ちを生じるような、ほとんど相殺される量での加算や減算によって増幅されます。Knuth は、十分でない計算精度の下で値丸めを伴う浮動小数点演算を行った結果、加算の結合則や分配則における恒等性が崩れてしまう例を二つ示しています:

```python
from decimal import Decimal, getcontext
getcontext().prec = 8

u, v, w = Decimal(11111113), Decimal(-11111111), Decimal('7.51111111')
print((u + v) + w)
print(u + (v + w))

u, v, w = Decimal(20000), Decimal(-6), Decimal('6.0000003')
print((u*v) + (u*w))
print(u * (v+w))
```
```sh
$ python 0.py 
9.5111111
10
0.01
0.0060000
```

## [9.4.7.2. 特殊値](https://docs.python.jp/3/library/decimal.html#special-values)

> decimal モジュールの数体系では、 NaN, sNaN, -Infinity, Infinity, および二つのゼロ、 +0 と -0 といった特殊な値を提供しています。

> 無限大 (Infinity) は Decimal('Infinity') で直接構築できます。また、 DivisionByZero をトラップせずにゼロで除算を行った場合にも出てきます。同様に、 Overflow シグナルをトラップしなければ、表現可能な最大の数値の制限を越えた値を丸めたときに出てきます。

> 無限大には符号があり (アフィン: affine であり)、算術演算に使用でき、非常に巨大で不確定の(indeterminate)値として扱われます。例えば、無限大に何らかの定数を加算すると、演算結果は別の無限大になります。

> 演算によっては結果が不確定になるものがあり、 NaN を返します。ただし、 InvalidOperation シグナルをトラップするようになっていれば例外を送出します。例えば、 0/0 は NaN を返します。 NaN は「非数値 (not a number)」を表します。このような NaN は暗黙のうちに生成され、一度生成されるとそれを他の計算にも流れてゆき、関係する個々の演算全てが個別の NaN を返すようになります。この挙動は、たまに入力値が欠けるような状況で一連の計算を行う際に便利です — 特定の計算に対しては無効な結果を示すフラグを立てつつ計算を進められるからです。

> 一方、 NaN の変種である sNaN は関係する全ての演算で演算後にシグナルを送出します。 sNaN は、無効な演算結果に対して特別な処理を行うために計算を停止する必要がある場合に便利です。

> Python の比較演算は NaN が関わってくると少し驚くようなことがあります。等価性のテストの一方の対象が無言または発信 NaN である場合いつでも False を返し(たとえ Decimal('NaN')==Decimal('NaN') でも)、一方で不等価をテストするといつでも True を返します。二つの Decimal を <, <=, > または >= を使って比較する試みは一方が NaN である場合には InvalidOperation シグナルを送出し、このシグナルをトラップしなければ結果は False に終わります。汎用十進演算仕様は直接の比較の振る舞いについて定めていないことに注意しておきましょう。ここでの NaN が関係する比較ルールは IEEE 854 標準から持ってきました (section 5.7 の Table 3 を見て下さい)。厳格に標準遵守を貫くなら、 compare() および compare-signal() メソッドを代わりに使いましょう。

> アンダフローの起きた計算は、符号付きのゼロ (signed zero) を返すことがあります。符号は、より高い精度で計算を行った結果の符号と同じになります。符号付きゼロの大きさはやはりゼロなので、正のゼロと負のゼロは等しいとみなされ、符号は単なる参考にすぎません。

> 二つの符号付きゼロが区別されているのに等価であることに加えて、異なる精度におけるゼロの表現はまちまちなのに、値は等価とみなされるということがあります。これに慣れるには多少時間がかかります。正規化浮動小数点表現に目が慣れてしまうと、以下の計算でゼロに等しい値が返っているとは即座に分かりません:

```python
print(1 / Decimal('Infinity'))
```

