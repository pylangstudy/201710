# [10.1.1. Itertool関数](https://docs.python.jp/3/library/itertools.html#itertool-functions)

< [10.1. itertools — 効率的なループ実行のためのイテレータ生成関数](https://docs.python.jp/3/library/itertools.html#module-itertools) < [10. 関数型プログラミング用モジュール](https://docs.python.jp/3/library/functional.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

```python
import itertools
import operator
for i in itertools.accumulate([1,2,3,4,5]): print(i)
for i in itertools.accumulate([1,2,3,4,5], operator.mul): print(i)
```
```sh
 $ python 0.py 
1
3
6
10
15
1
2
6
24
120
```

```python
import itertools
import operator
data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
print(list(itertools.accumulate(data, operator.mul)))     # running product
print(list(itertools.accumulate(data, max)))              # running maximum

# Amortize a 5% loan of 1000 with 4 annual payments of 90
cashflows = [1000, -90, -90, -90, -90]
print(list(itertools.accumulate(cashflows, lambda bal, pmt: bal*1.05 + pmt)))

# Chaotic recurrence relation https://en.wikipedia.org/wiki/Logistic_map
logistic_map = lambda x, _:  r * x * (1 - x)
r = 3.8
x0 = 0.4
inputs = itertools.repeat(x0, 36)     # only the initial value is used
print(inputs)
```
```sh
$ python 1.py 
[3, 12, 72, 144, 144, 1296, 0, 0, 0, 0]
[3, 4, 6, 6, 6, 9, 9, 9, 9, 9]
[1000, 960.0, 918.0, 873.9000000000001, 827.5950000000001]
repeat(0.4, 36)
```

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
for c in itertools.compress('ABCDEF', [1,0,1,0,1,1]): print(c)
for c in itertools.count(10):
    print(c)
    if c == 20: break
for c in itertools.count(2.5, 0.5):
    print(c)
    if c == 5: break
for c in itertools.cycle('ABCD'):
    print(c)
    if c == 'D': break
for c in itertools.dropwhile(lambda x: x<5, [1,4,6,4,1]): print(c)
for c in itertools.filterfalse(lambda x: x%2, range(10)): print(c)
print([k for k, g in itertools.groupby('AAAABBBCCDAABBB')])
print([list(g) for k, g in itertools.groupby('AAAABBBCCD')])
for c in itertools.islice('ABCDEFG', 2): print(c)
for c in itertools.islice('ABCDEFG', 2, 4): print(c)
for c in itertools.islice('ABCDEFG', 2, None): print(c)
for c in itertools.islice('ABCDEFG', 0, None, 2): print(c)
for c in itertools.permutations('ABCD', 2): print(c)
for c in itertools.permutations(range(3)): print(c)
for c in itertools.product('ABCD', 'xy'): print(c)
for c in itertools.product(range(2), repeat=3): print(c)
for c in itertools.repeat(10, 3): print(c)
print(list(map(pow, range(10), itertools.repeat(2))))
for c in itertools.starmap(pow, [(2,5), (3,2), (10,3)]): print(c)
for c in itertools.takewhile(lambda x: x<5, [1,4,6,4,1]): print(c)
for c in itertools.tee([1,2,3,4,5]): print(c)
for c in itertools.zip_longest('ABCD', 'xy', fillvalue='-'): print(c)
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
A
C
E
F
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
2.5
3.0
3.5
4.0
4.5
5.0
A
B
C
D
6
4
1
0
2
4
6
8
['A', 'B', 'C', 'D', 'A', 'B']
[['A', 'A', 'A', 'A'], ['B', 'B', 'B'], ['C', 'C'], ['D']]
A
B
C
D
C
D
E
F
G
A
C
E
G
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
(0, 1, 2)
(0, 2, 1)
(1, 0, 2)
(1, 2, 0)
(2, 0, 1)
(2, 1, 0)
('A', 'x')
('A', 'y')
('B', 'x')
('B', 'y')
('C', 'x')
('C', 'y')
('D', 'x')
('D', 'y')
(0, 0, 0)
(0, 0, 1)
(0, 1, 0)
(0, 1, 1)
(1, 0, 0)
(1, 0, 1)
(1, 1, 0)
(1, 1, 1)
10
10
10
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
32
9
1000
1
4
<itertools._tee object at 0xb710264c>
<itertools._tee object at 0xb71026cc>
('A', 'x')
('B', 'y')
('C', '-')
('D', '-')
```
