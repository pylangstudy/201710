# [10.3. operator — 関数形式の標準演算子](https://docs.python.jp/3/library/operator.html)

< [10. 関数型プログラミング用モジュール](https://docs.python.jp/3/library/functional.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/operator.py](https://github.com/python/cpython/tree/3.6/Lib/operator.py)

> operator モジュールは、Python の組み込み演算子に対応する効率的な関数群を提供します。例えば、 operator.add(x, y) は式 x+y と等価です。関数の名前は、特殊クラスメソッドに使われている名前と同じです; 便宜上、先頭と末尾の __ を取り除いたものも提供されています。

> これらの関数は、オブジェクト比較、論理演算、数学演算、シーケンス演算をするものに分類されます。

> オブジェクト比較関数は全てのオブジェクトで有効で、関数の名前はサポートする拡張比較演算子からとられています:


属性|説明
----|----
operator.lt(a, b), operator.le(a, b), operator.eq(a, b), operator.ne(a, b), operator.ge(a, b), operator.gt(a, b), operator.__lt__(a, b), operator.__le__(a, b), operator.__eq__(a, b), operator.__ne__(a, b), operator.__ge__(a, b), operator.__gt__(a, b)|a と b の “拡張比較 (rich comparisons)” を行います。具体的には、 lt(a, b) は a < b 、 le(a, b) は a <= b 、 eq(a, b) は a == b 、 ne(a, b) は a != b 、 gt(a, b) は a >= b 、そして ge(a, b) は a >= b と等価です。これらの関数はどのような値を返してもよく、ブール値として解釈できてもできなくてもかまいません。拡張比較の詳細については 比較 を参照してください。
operator.not_(obj), operator.__not__(obj)|not obj の結果を返します。(オブジェクトインスタンスには __not__() メソッドは無いので注意してください; インタプリタコアがこの演算を定義しているだけです。結果は __bool__() および __len__() メソッドに影響されます。)
operator.truth(obj)|obj が真の場合 True を返し、そうでない場合 False を返します。この関数は bool のコンストラクタ呼び出しと同等です。
operator.is_(a, b)|a is b を返します。オブジェクトの同一性を判定します。
operator.is_not(a, b)|a is not b を返します。オブジェクトの同一性を判定します。

演算子で最も多いのは数学演算およびビット単位の演算です:

属性|説明
----|----
operator.abs(obj), operator.__abs__(obj)|obj の絶対値を返します。
operator.add(a, b), operator.__add__(a, b)|数値 a および b について a + b を返します。
operator.and_(a, b), operator.__and__(a, b)|a と b のビット単位論理積を返します。
operator.floordiv(a, b), operator.__floordiv__(a, b)|a // b を返します。
operator.index(a), operator.__index__(a)|整数に変換された a を返します。a.__index__() と同等です。
operator.inv(obj), operator.invert(obj), operator.__inv__(obj), operator.__invert__(obj)|obj のビット単位反転を返します。~obj と同じです。
operator.lshift(a, b), operator.__lshift__(a, b)|a の b ビット左シフトを返します。
operator.mod(a, b), operator.__mod__(a, b)|a % b を返します。
operator.mul(a, b), operator.__mul__(a, b)|数値 a および b について a * b を返します。
operator.matmul(a, b), operator.__matmul__(a, b)|a @ b を返します。
operator.neg(obj), operator.__neg__(obj)|負の obj (-obj) を返します。
operator.or_(a, b), operator.__or__(a, b)|a と b のビット単位論理和を返します。
operator.pos(obj), operator.__pos__(obj)|正の obj (+obj) を返します。
operator.pow(a, b), operator.__pow__(a, b)|数値 a および b について a ** b を返します。
operator.rshift(a, b), operator.__rshift__(a, b)|a の b ビット右シフトを返します。
operator.sub(a, b), operator.__sub__(a, b)|a - b を返します。
operator.truediv(a, b), operator.__truediv__(a, b)|2/3 が 0 ではなく 0.66 となるような a / b を返します。 “真の” 除算としても知られています。
operator.xor(a, b), operator.__xor__(a, b)|a および b のビット単位排他的論理和を返します。

シーケンスを扱う演算子（いくつかの演算子はマッピングも扱います）には以下のようなものがあります:

属性|説明
----|----
operator.concat(a, b), operator.__concat__(a, b)|シーケンス a および b について a + b を返します。
operator.contains(a, b), operator.__contains__(a, b)|b in a の判定結果を返します。被演算子が左右反転しているので注意してください。
operator.countOf(a, b)|a の中に b が出現する回数を返します。
operator.delitem(a, b), operator.__delitem__(a, b)|a でインデクスが b の値を削除します。
operator.getitem(a, b), operator.__getitem__(a, b)|a でインデクスが b の値を返します。
operator.indexOf(a, b)|a で最初に b が出現する場所のインデクスを返します。
operator.setitem(a, b, c), operator.__setitem__(a, b, c)|a でインデクスが b の値を c に設定します。
operator.length_hint(obj, default=0)|オブジェクト o の概算の長さを返します。最初に実際の長さを、次に object.__length_hint__() を使って概算の長さを、そして最後にデフォルトの値を返そうとします。
operator.attrgetter(attr), operator.attrgetter(*attrs)|演算対象から attr を取得する呼び出し可能なオブジェクトを返します。二つ以上の属性を要求された場合には、属性のタプルを返します。属性名はドットを含むこともできます。
operator.itemgetter(item), operator.itemgetter(*items)|演算対象からその __getitem__() メソッドを使って item を取得する呼び出し可能なオブジェクトを返します。 二つ以上のアイテムを要求された場合には、アイテムのタプルを返します。
operator.methodcaller(name[, args...])|引数の name メソッドを呼び出す呼び出し可能オブジェクトを返します。追加の引数および/またはキーワード引数が与えられると、これらもそのメソッドに引き渡されます。

```python
import operator
print(operator.lt(1, 2))
print(operator.lt(2, 1))
```
```sh
$ python 0.py 
True
False
```

`object.__lt__(other)`などよりも、`operator.lt(a, b)`などのメソッドを先に知らせるほうが混乱が少なかったと思う。動的言語らしいメソッドの数々。

## [10.3.1. 演算子から関数への対応表](https://docs.python.jp/3/library/operator.html#mapping-operators-to-functions)

> 下のテーブルでは、個々の抽象的な操作が、どのように Python 構文上の各演算子や operator モジュールの関数に対応しているかを示しています。


演算|操作|関数
----|----|----
加算|a + b 	add(a, b)
結合|seq1 + seq2 	concat(seq1, seq2)
包含判定|obj in seq 	contains(seq, obj)
除算|a / b 	truediv(a, b)
除算|a // b 	floordiv(a, b)
ビット単位論理積|a & b 	and_(a, b)
ビット単位排他的論理和|a ^ b 	xor(a, b)
ビット単位反転|~ a 	invert(a)
ビット単位論理和|a | b 	or_(a, b)
冪乗|a ** b 	pow(a, b)
同一性|a is b 	is_(a, b)
同一性|a is not b 	is_not(a, b)
インデクス指定の代入|obj[k] = v 	setitem(obj, k, v)
インデクス指定の削除|del obj[k] 	delitem(obj, k)
インデクス指定|obj[k] 	getitem(obj, k)
左シフト|a << b 	lshift(a, b)
剰余|a % b 	mod(a, b)
乗算|a * b 	mul(a, b)
行列の乗算|a @ b 	matmul(a, b)
(算術) 負|- a 	neg(a)
(論理) 否|not a 	not_(a)
正|+ a 	pos(a)
右シフト|a >> b 	rshift(a, b)
スライス指定の代入|seq[i:j] = values 	setitem(seq, slice(i, j), values)
スライス指定の削除|del seq[i:j] 	delitem(seq, slice(i, j))
スライス指定|seq[i:j] 	getitem(seq, slice(i, j))
文字列書式化|s % obj 	mod(s, obj)
減算|a - b 	sub(a, b)
真理値判定|obj 	truth(obj)
順序付け|a < b 	lt(a, b)
順序付け|a <= b 	le(a, b)
等価性|a == b 	eq(a, b)
不等性|a != b 	ne(a, b)
順序付け|a >= b 	ge(a, b)
順序付け|a > b 	gt(a, b)

## [10.3.2. インプレース演算子](https://docs.python.jp/3/library/operator.html#inplace-operators)

> 多くの演算に「インプレース」版があります。 以下の関数はそうした演算子の通常の文法に比べてより素朴な呼び出し方を提供します。たとえば、文(statement) x += y は x = operator.iadd(x, y) と等価です。別の言い方をすると、 z = operator.iadd(x, y) は複合文 z = x; z += y と等価です。

> なお、これらの例では、インプレースメソッドが呼び出されたとき、計算と代入は二段階に分けて行われます。以下に挙げるインプレース関数は、インプレースメソッドを呼び出してその第一段階だけを行います。第二段階の代入は扱われません。

> 文字列、数、タプルのようなイミュータブルなターゲットでは、更新された値が計算されますが、入力変数に代入し返されはしません。

```python
>>> a = 'hello'
>>> iadd(a, ' world')
'hello world'
>>> a
'hello'
```

```python
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
```
```sh
$ python 1.py 
a= 100
b= 1
101
a= 100
b= 1
101
a= 100
b= 1
```
上記をみるとadd, iaddに違いが見られない…。


リストや辞書のようなミュータブルなターゲットでは、インプレースメソッドは更新を行うので、続く代入は必要ありません。

```python
>>> s = ['h', 'e', 'l', 'l', 'o']
>>> iadd(s, [' ', 'w', 'o', 'r', 'l', 'd'])
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
>>> s
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
```

メソッド|説明
--------|----
operator.iadd(a, b), operator.__iadd__(a, b)|a = iadd(a, b) は a += b と等価です。
operator.iand(a, b), operator.__iand__(a, b)|a = iand(a, b) は a &= b と等価です。
operator.iconcat(a, b), operator.__iconcat__(a, b)|a = iconcat(a, b) は二つのシーケンス a と b に対し a += b と等価です。
operator.ifloordiv(a, b), operator.__ifloordiv__(a, b)|a = ifloordiv(a, b) は a //= b と等価です。
operator.ilshift(a, b), operator.__ilshift__(a, b)|a = ilshift(a, b) は a <<= b と等価です。
operator.imod(a, b), operator.__imod__(a, b)|a = imod(a, b) は a %= b と等価です。
operator.imul(a, b), operator.__imul__(a, b)|a = imul(a, b) は a *= b と等価です。
operator.imatmul(a, b), operator.__imatmul__(a, b)|a = imatmul(a, b) は a @= b と等価です。
operator.ior(a, b), operator.__ior__(a, b)|a = ior(a, b) は a |= b と等価です。
operator.ipow(a, b), operator.__ipow__(a, b)|a = ipow(a, b) は a **= b と等価です。
operator.irshift(a, b), operator.__irshift__(a, b)|a = irshift(a, b) は a >>= b と等価です。
operator.isub(a, b), operator.__isub__(a, b)|a = isub(a, b) は a -= b と等価です。
operator.itruediv(a, b), operator.__itruediv__(a, b)|a = itruediv(a, b) は a /= b と等価です。
operator.ixor(a, b), operator.__ixor__(a, b)|a = ixor(a, b) は a ^= b と等価です。

