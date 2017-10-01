# [9.4.8. スレッドを使った処理](https://docs.python.jp/3/library/decimal.html#working-with-threads)

< [9.4. decimal — 十進固定及び浮動小数点数の算術演算](https://docs.python.jp/3/library/decimal.html#module-decimal) < [9. 数値と数学モジュール](https://docs.python.jp/3/library/numeric.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/decimal.py](https://github.com/python/cpython/tree/3.6/Lib/decimal.py)

> 関数 getcontext() は、スレッド毎に別々の Context オブジェクトにアクセスします。別のスレッドコンテキストを持つということは、複数のスレッドが互いに影響を及ぼさずに (getcontext().prec=10 のような) 変更を適用できるということです。

> 同様に、setcontext() 関数は自動的に引数のコンテキストを現在のスレッドのコンテキストに設定します。

> getcontext() を呼び出す前に setcontext() が呼び出されていなければ、現在のスレッドで使うための新たなコンテキストを生成するために getcontext() が自動的に呼び出されます。

> 新たなコンテキストは、DefaultContext と呼ばれる雛形からコピーされます。アプリケーションを通じて全てのスレッドに同じ値を使うようにデフォルトを設定したければ、DefaultContext オブジェクトを直接変更します。 getcontext() を呼び出すスレッド間で競合条件が生じないようにするため、DefaultContext への変更はいかなるスレッドを開始するよりも 前に 行わなければなりません。以下に例を示します:

```python
DefaultContext.prec = 12
DefaultContext.rounding = ROUND_DOWN
DefaultContext.traps = ExtendedContext.traps.copy()
DefaultContext.traps[InvalidOperation] = 1
setcontext(DefaultContext)

# Afterwards, the threads can be started
t1.start()
t2.start()
t3.start()
```

## [9.4.9. レシピ](https://docs.python.jp/3/library/decimal.html#recipes)

> Decimal クラスの利用を実演している例をいくつか示します。これらはユーティリティ関数としても利用できます:

```python
from decimal import Decimal, getcontext
def moneyfmt(value, places=2, curr='', sep=',', dp='.',
             pos='', neg='-', trailneg=''):
    """Convert Decimal to a money formatted string.

    places:  required number of places after the decimal point
    curr:    optional currency symbol before the sign (may be blank)
    sep:     optional grouping separator (comma, period, space, or blank)
    dp:      decimal point indicator (comma or period)
             only specify as blank when places is zero
    pos:     optional sign for positive numbers: '+', space or blank
    neg:     optional sign for negative numbers: '-', '(', space or blank
    trailneg:optional trailing minus indicator:  '-', ')', space or blank

    d = Decimal('-1234567.8901')
    moneyfmt(d, curr='$')
    '-$1,234,567.89'
    moneyfmt(d, places=0, sep='.', dp='', neg='', trailneg='-')
    '1.234.568-'
    moneyfmt(d, curr='$', neg='(', trailneg=')')
    '($1,234,567.89)'
    moneyfmt(Decimal(123456789), sep=' ')
    '123 456 789.00'
    moneyfmt(Decimal('-0.02'), neg='<', trailneg='>')
    '<0.02>'

    """
    q = Decimal(10) ** -places      # 2 places --> '0.01'
    sign, digits, exp = value.quantize(q).as_tuple()
    result = []
    digits = list(map(str, digits))
    build, next = result.append, digits.pop
    if sign:
        build(trailneg)
    for i in range(places):
        build(next() if digits else '0')
    if places:
        build(dp)
    if not digits:
        build('0')
    i = 0
    while digits:
        build(next())
        i += 1
        if i == 3 and digits:
            i = 0
            build(sep)
    build(curr)
    build(neg if sign else pos)
    return ''.join(reversed(result))

def pi():
    """Compute Pi to the current precision.

    print(pi())
    3.141592653589793238462643383

    """
    getcontext().prec += 2  # extra digits for intermediate steps
    three = Decimal(3)      # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s               # unary plus applies the new precision

def exp(x):
    """Return e raised to the power of x.  Result type matches input type.

    print(exp(Decimal(1)))
    2.718281828459045235360287471
    print(exp(Decimal(2)))
    7.389056098930650227230427461
    print(exp(2.0))
    7.38905609893
    print(exp(2+0j))
    (7.38905609893+0j)

    """
    getcontext().prec += 2
    i, lasts, s, fact, num = 0, 0, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 1
        fact *= i
        num *= x
        s += num / fact
    getcontext().prec -= 2
    return +s

def cos(x):
    """Return the cosine of x as measured in radians.

    The Taylor series approximation works best for a small value of x.
    For larger values, first compute x = x % (2 * pi).

    print(cos(Decimal('0.5')))
    0.8775825618903727161162815826
    print(cos(0.5))
    0.87758256189
    print(cos(0.5+0j))
    (0.87758256189+0j)

    """
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s

def sin(x):
    """Return the sine of x as measured in radians.

    The Taylor series approximation works best for a small value of x.
    For larger values, first compute x = x % (2 * pi).

    print(sin(Decimal('0.5')))
    0.4794255386042030002732879352
    print(sin(0.5))
    0.479425538604
    print(sin(0.5+0j))
    (0.479425538604+0j)

    """
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s

d = Decimal('-1234567.8901')
moneyfmt(d, curr='$')
print(pi())
print(exp(Decimal(1)))
print(cos(Decimal('0.5')))
```
```sh
$ python 1.py 
3.141592653589793238462643383
2.718281828459045235360287471
0.8775825618903727161162815826
```

## [9.4.10. Decimal FAQ](https://docs.python.jp/3/library/decimal.html#decimal-faq)

> Q. decimal.Decimal('1234.5') などと打ち込むのは煩わしいのですが、対話式インタプリタを使う際にタイプ量を少なくする方法はありませんか?

> A. コンストラクタを1文字に縮める人もいるようです:

```python
D = decimal.Decimal
D('1.23') + D('3.45')
Decimal('4.68')
```

予約語でないから名前重複の恐れあり。

> Q. 小数点以下2桁の固定小数点数のアプリケーションの中で、いくつかの入力が余計な桁を保持しているのでこれを丸めなければなりません。その他のものに余計な桁はなくそのまま使えます。どのメソッドを使うのがいいでしょうか?

> A. quantize() メソッドで固定した桁に丸められます。 Inexact トラップを設定しておけば、確認にも有用です:

```python
>>> TWOPLACES = Decimal(10) ** -2       # same as Decimal('0.01')
```
```python
>>> # Round to two places
>>> Decimal('3.214').quantize(TWOPLACES)
Decimal('3.21')
```
```python
>>> # Validate that a number does not exceed two places
>>> Decimal('3.21').quantize(TWOPLACES, context=Context(traps=[Inexact]))
Decimal('3.21')
```
```python
>>> Decimal('3.214').quantize(TWOPLACES, context=Context(traps=[Inexact]))
Traceback (most recent call last):
   ...
Inexact: None
```

> Q. 正当な2桁の入力が得られたとして、その正当性をアプリケーション実行中も変わらず保ち続けるにはどうすればいいでしょうか?

> A. 加減算あるいは整数との乗算のような演算は自動的に固定小数点を守ります。その他の除算や整数以外の乗算などは小数点以下の桁を変えてしまいますので実行後は quantize() ステップが必要です:

```python
>>> a = Decimal('102.72')           # Initial fixed-point values
>>> b = Decimal('3.17')
>>> a + b                           # Addition preserves fixed-point
Decimal('105.89')
>>> a - b
Decimal('99.55')
>>> a * 42                          # So does integer multiplication
Decimal('4314.24')
>>> (a * b).quantize(TWOPLACES)     # Must quantize non-integer multiplication
Decimal('325.62')
>>> (b / a).quantize(TWOPLACES)     # And quantize division
Decimal('0.03')
```

> 固定小数点のアプリケーションを開発する際は、 quantize() の段階を扱う関数を定義しておくと便利です:

```python
>>> def mul(x, y, fp=TWOPLACES):
...     return (x * y).quantize(fp)
>>> def div(x, y, fp=TWOPLACES):
...     return (x / y).quantize(fp)

>>>

>>> mul(a, b)                       # Automatically preserve fixed-point
Decimal('325.62')
>>> div(b, a)
Decimal('0.03')
```

> Q. 一つの値に対して多くの表現方法があります。 200 と 200.000 と 2E2 と 02E+4 は全て同じ値で違った精度の数です。これらをただ一つの正規化された値に変換することはできますか?

> A. normalize() メソッドは全ての等しい値をただ一つの表現に直します:

```python
>>> values = map(Decimal, '200 200.000 2E2 .02E+4'.split())
>>> [v.normalize() for v in values]
[Decimal('2E+2'), Decimal('2E+2'), Decimal('2E+2'), Decimal('2E+2')]
```

> Q. ある種の十進数値はいつも指数表記で表示されます。指数表記以外の表示にする方法はありますか?

> A. 値によっては、指数表記だけが有効桁数を表せる表記法なのです。たとえば、 5.0E+3 を 5000 と表してしまうと、値は変わりませんが元々の2桁という有効数字が反映されません。

> もしアプリケーションが有効数字の追跡を等閑視するならば、指数部や末尾のゼロを取り除き、有効数字を忘れ、しかし値を変えずにおくことは容易です:

```python
>>> def remove_exponent(d):
...     return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()

>>>

>>> remove_exponent(Decimal('5E+3'))
Decimal('5000')
```

> Q. 普通の float を Decimal に変換できますか?

> A. はい。どんな 2 進浮動小数点数も Decimal として正確に表現できます。ただし、正確な変換は直感的に考えたよりも多い桁になることがあります:

```python
>>> Decimal(math.pi)
Decimal('3.141592653589793115997963468544185161590576171875')
```

> Q. 複雑な計算の中で、精度不足や丸めの異常で間違った結果になっていないことをどうやって保証すれば良いでしょうか。

> A. decimal モジュールでは検算は容易です。一番良い方法は、大きめの精度や様々な丸めモードで再計算してみることです。大きく異なった結果が出てきたら、精度不足や丸めの問題や悪条件の入力、または数値計算的に不安定なアルゴリズムを示唆しています。

> Q. コンテキストの精度は計算結果には適用されていますが入力には適用されていないようです。様々に異なる精度の入力値を混ぜて計算する時に注意すべきことはありますか?

> A. はい。原則として入力値は正確であると見做しておりそれらの値を使った計算も同様です。結果だけが丸められます。入力の強みは “what you type is what you get” (打ち込んだ値が得られる値)という点にあります。入力が丸められないということを忘れていると結果が奇妙に見えるというのは弱点です:

```python
>>> getcontext().prec = 3
>>> Decimal('3.104') + Decimal('2.104')
Decimal('5.21')
>>> Decimal('3.104') + Decimal('0.000') + Decimal('2.104')
Decimal('5.20')
```

> 解決策は、精度を増やすか、単項プラス演算子を使って入力の丸めを強制することです:

```python
>>> getcontext().prec = 3
>>> +Decimal('1.23456789')      # unary plus triggers rounding
Decimal('1.23')
```

> もしくは、入力を Context.create_decimal() を使って生成時に丸めてしまうこともできます:

```python
>>> Context(prec=5, rounding=ROUND_DOWN).create_decimal('1.2345678')
Decimal('1.2345')
```

