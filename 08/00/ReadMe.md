# [10.2. functools — 高階関数と呼び出し可能オブジェクトの操作](https://docs.python.jp/3/library/functools.html#module-functools)

< [10. 関数型プログラミング用モジュール](https://docs.python.jp/3/library/functional.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/functools.py](https://github.com/python/cpython/tree/3.6/Lib/functools.py)

> functools モジュールは高階関数、つまり関数に影響を及ぼしたり他の関数を返したりする関数のためのものです。一般に、どんな呼び出し可能オブジェクトでもこのモジュールの目的には関数として扱えます。

> モジュール functools は以下の関数を定義します:

属性|説明
----|----
functools.cmp_to_key(func)|古いスタイルの比較関数を key function に変換します。
@functools.lru_cache(maxsize=128, typed=False)|関数をメモ化用の呼び出し可能オブジェクトでラップし、最近の呼び出し最大 maxsize 回まで保存するするデコレータです。
@functools.total_ordering|ひとつ以上の拡張順序比較メソッド (rich comparison ordering methods) を定義したクラスを受け取り、残りを実装するクラスデコレータです。このデコレータは全ての拡張順序比較演算をサポートするための労力を軽減します:
functools.partial(func, *args, **keywords)|新しい partial オブジェクトを返します。このオブジェクトは呼び出されると位置引数 args とキーワード引数 keywords 付きで呼び出された func のように振る舞います。呼び出しに際してさらなる引数が渡された場合、それらは args に付け加えられます。追加のキーワード引数が渡された場合には、それらで keywords を拡張または上書きします。大雑把にいうと、次のコードと等価です:
class functools.partialmethod(func, *args, **keywords)|partial と似た動作をする新しい partialmethod 記述子 (デスクリプタ) を返します。直接呼び出しではなく、メソッド定義としての使用が目的であることのみが、partial とは異なります。
functools.reduce(function, iterable[, initializer])|2 引数の function を iterable の要素に対して左から右に累積的に適用し、イテラブルを単一の値に縮約します。
@functools.singledispatch(default)|関数を シングルディスパッチ generic function に変換します。
functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)|wrapper 関数を wrapped 関数に見えるようにアップデートします。
@functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)|これはラッパー関数を定義するときに update_wrapper() を関数デコレータとして呼び出す便宜関数です。


```python
from functools import *
import locale
import urllib
import urllib.request
import urllib.error

print(sorted(['あ','い','う'], key=cmp_to_key(locale.strcoll)))

@lru_cache(maxsize=32)
def get_pep(num):
    'Retrieve text of a Python Enhancement Proposal'
    resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except urllib.error.HTTPError:
        return 'Not Found'

for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
    pep = get_pep(n)
    print(n, len(pep))

print(get_pep.cache_info())
```
```sh
$ python 0.py 
['あ', 'い', 'う']
8 103643
290 58963
308 52110
320 48798
8 103643
218 46002
320 48798
279 47770
289 50095
320 48798
9991 9
CacheInfo(hits=3, misses=8, maxsize=32, currsize=8)
```

```python
from functools import *

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print([fib(n) for n in range(16)])
print(fib.cache_info())
```
```sh
$ python 1.py 
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)
```

```python
from functools import *
@total_ordering
class Student:
    def _is_valid_operand(self, other):
        return (hasattr(other, "lastname") and
                hasattr(other, "firstname"))
    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))

s = Student()
print(s)
print(s._is_valid_operand(s))
print(s == s)
print(s != s)
#print(s < s)
#print(s <= s)
#print(s > s)
#print(s >= s)
print(s is s)
print(s is not s)
```
```sh
$ python 2.py 
<__main__.Student object at 0xb7187d6c>
False
True
False
True
False
```

```python
from functools import *
basetwo = partial(int, base=2)
basetwo.__doc__ = 'Convert base 2 string to an int.'
print(basetwo('10010'))
```
```sh
$ python 3.py 
18
```

```python
from functools import *
class Cell(object):
    def __init__(self):
        self._alive = False
    @property
    def alive(self):
        return self._alive
    def set_state(self, state):
        self._alive = bool(state)
    set_alive = partialmethod(set_state, True)
    set_dead = partialmethod(set_state, False)

c = Cell()
print(c.alive)
c.set_alive()
print(c.alive)
```
```sh
$ python 4.py 
False
True
```

```python
import functools
functools.reduce(lambda x,y: print(x,y), [1,2,3])
```
```sh
$ python 5.py 
1 2
None 3
```

```python
from functools import singledispatch
@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)
print(fun(1))
```
```sh
$ python 6.py 
1
None
```
```python
```
```sh
```
```python
```
```sh
```
```python
```
```sh
```
```python
```
```sh
```
```python
```
```sh
```
```python
```
```sh
```


### オーバーロード

面倒かつ限定的だが、オーバーロード実装できる。

* @functools.singledispatch
    * `@funcName.`
* 引数1つのみ

```python
from functools import singledispatch
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

print(fun(1, True))
print(fun([2], True))
```
```sh
$ python 7.py 
Strength in numbers, eh? 1
None
Enumerate this:
0 2
None
```

```python
from functools import wraps
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper
@my_decorator
def example():
    """Docstring"""
    print('Called example function')

print(example())
print(example.__name__)
print(example.__doc__)
```
```sh
$ python D.py 
Calling decorated function
Called example function
None
example
Docstring
```

## [10.2.1. partial オブジェクト](https://docs.python.jp/3/library/functools.html#partial-objects)

> partial オブジェクトは、 partial() 関数によって作られる呼び出し可能オブジェクトです。オブジェクトには読み取り専用の属性が三つあります:

属性|説明
----|----
partial.func|呼び出し可能オブジェクトまたは関数です。 partial オブジェクトの呼び出しは新しい引数とキーワードと共に func に転送されます。
partial.args|最左の位置引数で、 partial オブジェクトの呼び出し時にその呼び出しの際の位置引数の前に追加されます。
partial.keywords|partial オブジェクトの呼び出し時に渡されるキーワード引数です。

> partial オブジェクトは function オブジェクトのように呼び出し可能で、弱参照可能で、属性を持つことができます。重要な相違点もあります。例えば、 __name__ と __doc__ 両属性は自動では作られません。また、クラス中で定義された partial オブジェクトはスタティックメソッドのように振る舞い、インスタンスの属性問い合わせの中で束縛メソッドに変換されません。

