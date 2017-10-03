# [9.6. random — 擬似乱数を生成する](https://docs.python.jp/3/library/random.html#module-random)

< [9. 数値と数学モジュール](https://docs.python.jp/3/library/numeric.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/random.py](https://github.com/python/cpython/tree/3.6/Lib/random.py)

> このモジュールでは様々な分布をもつ擬似乱数生成器を実装しています。

> 整数用に、ある範囲からの一様な選択があります。シーケンス用には、シーケンスからのランダムな要素の一様な選択、リストのランダムな置換をインプレースに生成する関数、順列を置換せずにランダムサンプリングする関数があります。

> 実数用としては、一様分布、正規分布 (ガウス分布)、対数正規分布、負の指数分布、ガンマおよびベータ分布を計算する関数があります。角度の分布を生成するにはフォン・ミーゼス分布が利用できます。

> ほとんど全てのモジュール関数は、基礎となる関数 random() に依存します。この関数はランダムな浮動小数点数を半開区間 [0.0, 1.0) 内に一様に生成します。Python は中心となる乱数生成器としてメルセンヌツイスタを使います。これは 53 ビット精度の浮動小数点を生成し、周期は 2**19937-1 です。本体は C で実装されていて、高速でスレッドセーフです。メルセンヌツイスタは、現存する中で最も広範囲にテストされた乱数生成器のひとつです。しかしながら、メルセンヌツイスタは完全に決定論的であるため、全ての目的に合致しているわけではなく、暗号化の目的には全く向いていません。

> このモジュールで提供されている関数は、実際には random.Random クラスの隠蔽されたインスタンスのメソッドに束縛されています。内部状態を共有しない生成器を取得するため、自分で Random のインスタンスを生成することができます。

> 自分で考案した基本乱数生成器を使いたい場合、クラス Random をサブクラス化することもできます。この場合、メソッド random()、seed()、getstate()、setstate() をオーバライドしてください。オプションとして、新しいジェネレータは getrandbits() メソッドを提供することができます。これにより randrange() メソッドが任意に大きな範囲から選択を行えるようになります。

> random モジュールは SystemRandom クラスも提供していて、このクラスは OS が提供している乱数発生源を利用して乱数を生成するシステム関数 os.urandom() を使うものです。

> 警告

> このモジュールの擬似乱数生成器をセキュリティ目的に使用してはいけません。セキュリティや暗号学的な用途については secrets モジュールを参照してください。

> 参考

> M. Matsumoto and T. Nishimura, “Mersenne Twister: A 623-dimensionally equidistributed uniform pseudorandom number generator”, ACM Transactions on Modeling and Computer Simulation Vol. 8, No. 1, January pp.3–30 1998.

> Complementary-Multiply-with-Carry recipe 長い周期と比較的シンプルな更新操作を備えた互換性のある別の乱数生成器。

Python以前に数学がわからないので何を言っているのかチンプンカンプン。

## [9.6.1. 保守 (bookkeeping) 関数](https://docs.python.jp/3/library/random.html#bookkeeping-functions)

属性|説明
----|----
random.seed(a=None, version=2)|乱数生成器を初期化します。
random.getstate()|乱数生成器の現在の内部状態を記憶したオブジェクトを返します。このオブジェクトを setstate() に渡して内部状態を復元することができます。
random.setstate(state)|state は予め getstate() を呼び出して得ておかなくてはなりません。 setstate() は getstate() が呼び出された時の乱数生成器の内部状態を復元します。
random.getrandbits(k)|k 桁の乱数ビットで Python の整数を生成し、返します。このメソッドはメルセンヌツイスタ生成器で提供されており、その他の乱数生成器でもオプションの API として提供されている場合があります。randrange() メソッドを使用できる場合、getrandbits() はそのメソッドを有効にし、任意の大きな範囲を扱えるようになります。

## [9.6.2. 整数用の関数](https://docs.python.jp/3/library/random.html#functions-for-integers)

属性|説明
----|----
random.randrange(stop), random.randrange(start, stop[, step])|range(start, stop, step) の要素からランダムに選ばれた要素を返します。この関数は choice(range(start, stop, step)) と等価ですが、実際には range オブジェクトを生成しません。
random.randint(a, b)|a <= N <= b であるようなランダムな整数 N を返します。randrange(a, b+1) のエイリアスです。

## [9.6.3. シーケンス用の関数](https://docs.python.jp/3/library/random.html#functions-for-sequences)

属性|説明
----|----
random.choice(seq)|空でないシーケンス seq からランダムに要素を返します。 seq が空のときは、 IndexError が送出されます。
random.choices(population, weights=None, *, cum_weights=None, k=1)|population から重複ありで選んだ要素からなる大きさ k のリストを返します。population が空の場合 IndexError を送出します。
random.shuffle(x[, random])|シーケンス x をインプレースにシャッフルします。
random.sample(population, k)|母集団のシーケンスまたは集合から選ばれた長さ k の一意な要素からなるリストを返します。重複無しのランダムサンプリングに用いられます。

## [9.6.4. 実数分布](https://docs.python.jp/3/library/random.html#real-valued-distributions)

> 以下の関数は特定の実数値分布を生成します。関数の引数の名前は、一般的な数学の慣例で使われている分布の公式の対応する変数から取られています; これらの公式のほとんどはどんな統計学のテキストにも載っています。

属性|説明
----|----
random.random()|次のランダムな浮動小数点数（範囲は [0.0, 1.0) ）を返します。
random.uniform(a, b)|a <= b であれば a <= N <= b 、b < a であれば b <= N <= a であるようなランダムな浮動小数点数 N を返します。
random.triangular(low, high, mode)|low <= N <= high でありこれら境界値の間に指定された最頻値 mode を持つようなランダムな浮動小数点数 N を返します。境界 low と high のデフォルトは 0 と 1 です。最頻値 mode 引数のデフォルトは両境界値の中点になり、対称な分布を与えます。
random.betavariate(alpha, beta)|ベータ分布です。引数の満たすべき条件は alpha > 0 および beta > 0 です。 0 から 1 の範囲の値を返します。
random.expovariate(lambd)|指数分布です。lambd は平均にしたい値の逆数です。(この引数は “lambda” と呼ぶべきなのですが、Python の予約語なので使えません。) 返す値の範囲は lambd が正なら 0 から正の無限大、lambd が負なら負の無限大から 0 です。
random.gammavariate(alpha, beta)|ガンマ分布です (ガンマ関数 ではありません ！)。引数の満たすべき条件は alpha > 0 および beta > 0 です。
random.gauss(mu, sigma)|ガウス分布です。 mu は平均であり、 sigma は標準偏差です。この関数は後で定義する関数 normalvariate() より少しだけ高速です。
random.lognormvariate(mu, sigma)|対数正規分布です。この分布を自然対数を用いた分布にした場合、平均 mu で標準偏差 sigma の正規分布になります。 mu は任意の値を取ることができ、sigma はゼロより大きくなければなりません。
random.normalvariate(mu, sigma)|正規分布です。 mu は平均で、 sigma は標準偏差です。
random.vonmisesvariate(mu, kappa)|mu は平均の角度で、0 から 2*pi までのラジアンで表されます。 kappa は濃度パラメータで、ゼロ以上でなければなりません。kappa がゼロに等しい場合、この分布は範囲 0 から 2*pi の一様でランダムな角度の分布に退化します。
random.paretovariate(alpha)|パレート分布です。 alpha は形状パラメータです。
random.weibullvariate(alpha, beta)|ワイブル分布です。 alpha は尺度パラメタで、 beta は形状パラメータです。

カッパと言われても頭に皿をのせたやつしか思い浮かばない。

```python
import random
random.seed()
print(random.random())
print(random.uniform(0,10))
print(random.triangular(0,10,5))
print(random.betavariate(.1,.5))
print(random.expovariate(100))
print(random.gammavariate(1,2))
print(random.gauss(1,2))
print(random.lognormvariate(1,2))
print(random.vonmisesvariate(1,2))
print(random.paretovariate(1))
print(random.weibullvariate(1,2))
```
```sh
$ python 1.py 
0.942445266562504
4.695848559418964
7.028513822995447
8.015203212680431e-05
0.012939235363459542
3.1122327055347188
-2.8705579558891423
2.7792325217821414
1.1079161064719412
1.5316627829068523
0.5873967074047177
```

## [9.6.5. 他の生成器](https://docs.python.jp/3/library/random.html#alternative-generator)

属性|説明
----|----
class random.SystemRandom([seed])|オペレーティングシステムの提供する発生源によって乱数を生成する os.urandom() 関数を使うクラスです。

## [9.6.6. 再現性について](https://docs.python.jp/3/library/random.html#notes-on-reproducibility)

> 疑似乱数生成器から与えられたシーケンスを再現できると便利なことがあります。シード値を再利用することで、複数のスレッドが実行されていない限り、実行ごとに同じシーケンスが再現できます。

> random モジュールのアルゴリズムやシード処理関数のほとんどは、Python バージョン間で変更される対象となりますが、次の二点は変更されないことが保証されています:

>     新しいシード処理メソッドが追加されたら、後方互換なシード処理器が提供されます。

>     生成器の random() メソッドは、互換なシード処理器に同じシードが与えられた場合、引き続き同じシーケンスを生成します。

## [9.6.7. 例とレシピ](https://docs.python.jp/3/library/random.html#examples-and-recipes)

> 参考

> Statistics for Hackers Jake Vanderplas による統計解析のビデオ。シミュレーション、サンプリング、シャッフル、交差検定といった基本的な概念のみを用いています。

> Economics Simulation Peter Norvig による市場価格のシミュレーション。このモジュールが提供する多くのツールや分布 (gauss, uniform, sample, betavariate, choice, triangular, randrange) の活用法を示しています。

> A Concrete Introduction to Probability (using Python) Peter Norvig によるチュートリアル。確率論の基礎、シミュレーションの書き方、Python を使用したデータ解析法をカバーしています。

高度すぎて何をしているのかさっぱり。

