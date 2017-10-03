# [9.7. statistics — 数理統計関数](https://docs.python.jp/3/library/statistics.html#module-statistics)

< [9. 数値と数学モジュール](https://docs.python.jp/3/library/numeric.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/statistics.py](https://github.com/python/cpython/tree/3.6/Lib/statistics.py)

> このモジュールは、数値 (Real 型) データを数学的に統計計算するための関数を提供します。

> 注釈

> 特に明記しない限り、これらの関数は int, float, decimal.Decimal そして fractions.Fraction をサポートします。他の型 (算術型及びそれ以外) は現在サポートされていません。混合型 (mixed type) も未定義で実装依存です。入力データが混合型を含んでいる場合、map() を使用すると正しい結果が得られるでしょう。 e.g. map(float, input_data)。 

## [9.7.1. 平均及び中心位置の測度](https://docs.python.jp/3/library/statistics.html#averages-and-measures-of-central-location)

> これらの関数は母集団または標本の平均値や標準値を計算します。

属性|説明
----|----
mean()|データの算術平均。
harmonic_mean() 	Harmonic mean of data.
median()|データの中央値。
median_low()|データの low median。
median_high()|データの high median。
median_grouped()|grouped data の中央値、すなわち50パーセンタイル。
mode()|離散データの最頻値。

## [9.7.2. 分散の測度](https://docs.python.jp/3/library/statistics.html#measures-of-spread)

これらの関数は母集団または標本が標準値や平均値からどれくらい離れているかについて計算します。

属性|説明
----|----
pstdev()|データの母標準偏差。
pvariance()|データの母分散。
stdev()|データの標本標準偏差。
variance()|データの標本標準分散。

## [9.7.3. 関数の詳細](https://docs.python.jp/3/library/statistics.html#function-details)

> 註釈: 関数の引数となるデータをソートしておく必要はありません。例の多くがソートされているのは見やすさのためです。

属性|説明
----|----
statistics.mean(data)|シーケンスまたはイテレータになるデータのサンプルの算術平均を返します。(Return the sample arithmetic mean of data which can be a sequence or iterator.)
statistics.harmonic_mean(data)|実数値のシーケンスまたはイテレータであるデータの高調波平均を返します。(Return the harmonic mean of data, a sequence or iterator of real-valued numbers.)
statistics.median(data)|一般的な「中間2の平均」法を使用して数値データの中央値（中間値）を返します。 データが空の場合、StatisticsErrorが発生します。 データはシーケンスまたは反復子にすることができます。(Return the median (middle value) of numeric data, using the common “mean of middle two” method. If data is empty, StatisticsError is raised. data can be a sequence or iterator.)
statistics.median_low(data)|数値データの中央値を返します。 データが空の場合、StatisticsErrorが発生します。 データはシーケンスまたは反復子にすることができます。(Return the low median of numeric data. If data is empty, StatisticsError is raised. data can be a sequence or iterator.)
statistics.median_high(data)|データの高い中央値を返します。 データが空の場合、StatisticsErrorが発生します。 データはシーケンスまたは反復子にすることができます。(Return the high median of data. If data is empty, StatisticsError is raised. data can be a sequence or iterator.)
statistics.median_grouped(data, interval=1)|補間を使用して、50番目のパーセンタイルとして計算されたグループ化された連続データの中央値を返します。 データが空の場合、StatisticsErrorが発生します。 データはシーケンスまたは反復子にすることができます。(Return the median of grouped continuous data, calculated as the 50th percentile, using interpolation. If data is empty, StatisticsError is raised. data can be a sequence or iterator.)
statistics.mode(data)|離散データや名目データ data の最頻値を返します。最頻値は (存在するときは) 最も標準的な値で、中心位置のロバストな測度です。
statistics.pstdev(data, mu=None)|母標準偏差 (母分散の平方根) を返します。引数や詳細は pvariance() を参照してください。
statistics.stdev(data, xbar=None)|標本標準偏差 (標本分散の平方根) を返します。引数や詳細は variance() を参照してください。
statistics.variance(data, xbar=None)|data の標本分散を返します。data は少なくとも2つの実数の iterable です。分散、すなわち2次の中心化モーメントはデータの散らばり具合の測度です。分散が大きいデータはばらつきが大きく、分散が小さいデータは平均値のまわりに固まっています。

## [9.7.4. 例外](https://docs.python.jp/3/library/statistics.html#exceptions)

属性|説明
----|----
exception statistics.StatisticsError|統計関係の例外。ValueError の派生クラス。

## ソースコード

```python
from statistics import *
print(mean([1, 2, 3, 4, 4]))
print(harmonic_mean([2.5, 3, 10]))
print(median([1, 3, 5]))
print(median_low([1, 3, 5]))
print(median_high([1, 3, 5]))
print(median_grouped([52, 52, 53, 54]))
print(median_grouped([1, 3, 3, 5, 7], interval=1))
print(median_grouped([1, 3, 3, 5, 7], interval=2))
print(mode([1, 1, 2, 3, 3, 3, 3, 4]))
print(mode(["red", "blue", "blue", "red", "green", "red", "red"]))
print(pstdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))
print(stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))
print(variance([2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]))
```
```sh
$ python 0.py 
2.8
3.6
3
3
3
52.5
3.25
3.5
3
red
0.986893273527251
1.0810874155219827
1.3720238095238095
```

