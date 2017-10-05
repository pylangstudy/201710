# [10.1. itertools — 効率的なループ実行のためのイテレータ生成関数](https://docs.python.jp/3/library/itertools.html#module-itertools)

< [10. 関数型プログラミング用モジュール](https://docs.python.jp/3/library/functional.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/statistics.py](https://github.com/python/cpython/tree/3.6/Lib/statistics.py)

> このモジュールは イテレータ を構築する部品を実装しています。プログラム言語 APL, Haskell, SML からアイデアを得ていますが、 Python に適した形に修正されています。

> このモジュールは、高速でメモリ効率に優れ、単独でも組合せても使用することのできるツールを標準化したものです。同時に、このツール群は “イテレータの代数” を構成していて、pure Python で簡潔かつ効率的なツールを作れるようにしています。

> 例えば、SML の作表ツール tabulate(f) は f(0), f(1), ... のシーケンスを作成します。同じことを Python では map() と count() を組合せて map(f, count()) という形で実現できます。

> これらのツールと組み込み関数は operator モジュール内の高速な関数とともに使うことで見事に動作します。例えば、乗算演算子を2つのベクトルにわたってマップすることで効率的な内積計算を実現できます: sum(map(operator.mul, vector1, vector2)) 。

## 無限イテレータ

イテレータ|引数|結果|使用例
----------|----|----|------
count()|start, [step]|start, start+step, start+2*step, ...|count(10) --> 10 11 12 13 14 ...
cycle()|p|p0, p1, ... plast, p0, p1, ...|cycle('ABCD') --> A B C D A B C D ...
repeat()|elem [,n]|elem, elem, elem, ... 無限もしくは n 回|repeat(10, 3) --> 10 10 10

```python
import itertools
for c in itertools.count(10):
    print(c)
    if c == 20: break
for c in itertools.cycle('CDEFGAB'):
    print(c)
    if c == 'B': break
for c in itertools.repeat(10, 3): print(c)
```
```sh
 $ python 0.py 
10
11
12
13
14
15
16
17
18
19
20
C
D
E
F
G
A
B
10
10
10
```    

## 一番短い入力シーケンスで止まるイテレータ

イテレータ|引数|結果|使用例
----------|----|----|------
accumulate()|p [,func]|p0, p0+p1, p0+p1+p2, ...|accumulate([1,2,3,4,5]) --> 1 3 6 10 15
chain()|p, q, ...|p0, p1, ... plast, q0, q1, ...|chain('ABC', 'DEF') --> A B C D E F
chain.from_iterable()|iterable|p0, p1, ... plast, q0, q1, ...|chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
compress()|data, selectors|(d[0] if s[0]), (d[1] if s[1]), ...|compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
dropwhile()|pred, seq|seq[n], seq[n+1], pred が偽の場所から始まる|dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
filterfalse()|pred, seq|pred(elem) が偽になるseqの要素|filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
groupby()|iterable[, keyfunc]|keyfunc(v) の値でグループ化したサブイテレータ| 
islice()|seq, [start,] stop [, step]|seq[start:stop:step]|islice('ABCDEFG', 2, None) --> C D E F G
starmap()|func, seq|func(*seq[0]), func(*seq[1]), ...|starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
takewhile()|pred, seq|seq[0], seq[1], pred が偽になるまで|takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
tee()|it, n|it1, it2 , ... itn 一つのイテレータを n 個に分ける| 
zip_longest()|p, q, ...|(p[0], q[0]), (p[1], q[1]), ...|zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-

```python
import itertools
for c in itertools.accumulate([1,2,3,4,5]): print(c)
for c in itertools.chain('ABC', 'DEF'): print(c)
for c in itertools.chain.from_iterable(['ABC', 'DEF']): print(c)
for c in itertools.compress('ABCDEF', [1,0,1,0,1,1]): print(c)
for c in itertools.dropwhile(lambda x: x<5, [1,4,6,4,1]): print(c)
for c in itertools.filterfalse(lambda x: x%2, range(10)): print(c)
for c in itertools.groupby([1,2,3,4,5], lambda x: x%2): print(c)
for c in itertools.islice('ABCDEFG', 2, None): print(c)
for c in itertools.starmap(pow, [(2,5), (3,2), (10,3)]): print(c)
for c in itertools.takewhile(lambda x: x<5, [1,4,6,4,1]): print(c)
for c in itertools.tee([1,2,3,4,5], 2): print(c)
for c in itertools.zip_longest('ABCD', 'xy', fillvalue='-'): print(c)
```
```sh
$ python 1.py 
1
3
6
10
15
A
B
C
D
E
F
A
B
C
D
E
F
A
C
E
F
6
4
1
0
2
4
6
8
(1, <itertools._grouper object at 0xb7158eec>)
(0, <itertools._grouper object at 0xb70e572c>)
(1, <itertools._grouper object at 0xb7158eec>)
(0, <itertools._grouper object at 0xb70e572c>)
(1, <itertools._grouper object at 0xb7158eec>)
C
D
E
F
G
32
9
1000
1
4
<itertools._tee object at 0xb70e572c>
<itertools._tee object at 0xb70e576c>
('A', 'x')
('B', 'y')
('C', '-')
('D', '-')
```

## 組合せジェネレータ

イテレータ|引数|結果
----------|----|----
product()|p, q, ... [repeat=1]|デカルト積、ネストしたforループと等価
permutations()|p[, r]|長さrのタプル列、重複なしのあらゆる並び
combinations()|p, r|長さrのタプル列、ソートされた順で重複なし
combinations_with_replacement()|p, r|長さrのタプル列、ソートされた順で重複あり
product('ABCD', repeat=2)| |AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
permutations('ABCD', 2)| |AB AC AD BA BC BD CA CB CD DA DB DC
combinations('ABCD', 2)| |AB AC AD BC BD CD
combinations_with_replacement('ABCD', 2)| |AA AB AC AD BB BC BD CC CD DD

```python
import itertools
for c in itertools.product([1,2,3,4,5],[1,2,3,4,5]): print(c)
for c in itertools.permutations([1,2,3,4,5],3): print(c)#順列?
for c in itertools.combinations([1,2,3,4,5],4): print(c)#組合せ?
for c in itertools.combinations_with_replacement([1,2,3,4,5],3): print(c)
for c in itertools.product('ABCD', repeat=2): print(c)
for c in itertools.permutations('ABCD', 2): print(c)
for c in itertools.combinations('ABCD', 2): print(c)
for c in itertools.combinations_with_replacement('ABCD', 2): print(c)
```
```sh
$ python 2.py 
(1, 1)
(1, 2)
(1, 3)
(1, 4)
(1, 5)
(2, 1)
(2, 2)
(2, 3)
(2, 4)
(2, 5)
(3, 1)
(3, 2)
(3, 3)
(3, 4)
(3, 5)
(4, 1)
(4, 2)
(4, 3)
(4, 4)
(4, 5)
(5, 1)
(5, 2)
(5, 3)
(5, 4)
(5, 5)
(1, 2, 3)
(1, 2, 4)
(1, 2, 5)
(1, 3, 2)
(1, 3, 4)
(1, 3, 5)
(1, 4, 2)
(1, 4, 3)
(1, 4, 5)
(1, 5, 2)
(1, 5, 3)
(1, 5, 4)
(2, 1, 3)
(2, 1, 4)
(2, 1, 5)
(2, 3, 1)
(2, 3, 4)
(2, 3, 5)
(2, 4, 1)
(2, 4, 3)
(2, 4, 5)
(2, 5, 1)
(2, 5, 3)
(2, 5, 4)
(3, 1, 2)
(3, 1, 4)
(3, 1, 5)
(3, 2, 1)
(3, 2, 4)
(3, 2, 5)
(3, 4, 1)
(3, 4, 2)
(3, 4, 5)
(3, 5, 1)
(3, 5, 2)
(3, 5, 4)
(4, 1, 2)
(4, 1, 3)
(4, 1, 5)
(4, 2, 1)
(4, 2, 3)
(4, 2, 5)
(4, 3, 1)
(4, 3, 2)
(4, 3, 5)
(4, 5, 1)
(4, 5, 2)
(4, 5, 3)
(5, 1, 2)
(5, 1, 3)
(5, 1, 4)
(5, 2, 1)
(5, 2, 3)
(5, 2, 4)
(5, 3, 1)
(5, 3, 2)
(5, 3, 4)
(5, 4, 1)
(5, 4, 2)
(5, 4, 3)
(1, 2, 3, 4)
(1, 2, 3, 5)
(1, 2, 4, 5)
(1, 3, 4, 5)
(2, 3, 4, 5)
(1, 1, 1)
(1, 1, 2)
(1, 1, 3)
(1, 1, 4)
(1, 1, 5)
(1, 2, 2)
(1, 2, 3)
(1, 2, 4)
(1, 2, 5)
(1, 3, 3)
(1, 3, 4)
(1, 3, 5)
(1, 4, 4)
(1, 4, 5)
(1, 5, 5)
(2, 2, 2)
(2, 2, 3)
(2, 2, 4)
(2, 2, 5)
(2, 3, 3)
(2, 3, 4)
(2, 3, 5)
(2, 4, 4)
(2, 4, 5)
(2, 5, 5)
(3, 3, 3)
(3, 3, 4)
(3, 3, 5)
(3, 4, 4)
(3, 4, 5)
(3, 5, 5)
(4, 4, 4)
(4, 4, 5)
(4, 5, 5)
(5, 5, 5)
('A', 'A')
('A', 'B')
('A', 'C')
('A', 'D')
('B', 'A')
('B', 'B')
('B', 'C')
('B', 'D')
('C', 'A')
('C', 'B')
('C', 'C')
('C', 'D')
('D', 'A')
('D', 'B')
('D', 'C')
('D', 'D')
('A', 'B')
('A', 'C')
('A', 'D')
('B', 'A')
('B', 'C')
('B', 'D')
('C', 'A')
('C', 'B')
('C', 'D')
('D', 'A')
('D', 'B')
('D', 'C')
('A', 'B')
('A', 'C')
('A', 'D')
('B', 'C')
('B', 'D')
('C', 'D')
('A', 'A')
('A', 'B')
('A', 'C')
('A', 'D')
('B', 'B')
('B', 'C')
('B', 'D')
('C', 'C')
('C', 'D')
('D', 'D')
```

