# [12.4. marshal — 内部使用向けの Python オブジェクト整列化](https://docs.python.jp/3/library/marshal.html)

< [12. データの永続化](https://docs.python.jp/3/library/persistence.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> このモジュールには Python 値をバイナリ形式で読み書きできるような関数が含まれています。このバイナリ形式は Python 特有のものですが、マシンアーキテクチャ非依存のものです (つまり、Python の値を PC 上でファイルに書き込み、Sun に転送し、そこで読み戻すことができます)。バイナリ形式の詳細は意図的にドキュメント化されていません; この形式は (稀にしかないことですが) Python のバージョン間で変更される可能性があるからです。[1]

### 脚注

> [1]	このモジュールの名前は (特に) Modula-3 の設計者の間で使われていた用語の一つに由来しています。彼らはデータを自己充足的な形式で輸送する操作に "整列化 (marshalling)" という用語を使いました。厳密に言えば、"整列させる (to marshal)" とは、あるデータを (例えば RPC バッファのように) 内部表現形式から外部表現形式に変換することを意味し、"非整列化 (unmarshalling)" とはその逆を意味します。

> このモジュールは汎用の "永続化 (persistence)" モジュールではありません。汎用的な永続化や、RPC 呼び出しを通じた Python オブジェクトの転送については、モジュール pickle および shelve を参照してください。 marshal モジュールは主に、 "擬似コンパイルされた (pseudo-compiled)" コードの .pyc ファイルへの読み書きをサポートするために存在します。したがって、 Python のメンテナンス担当者は、必要が生じれば marshal 形式を後方互換性のないものに変更する権利を有しています。 Python オブジェクトを直列化 (シリアライズ) および非直列化 (デシリアライズ) する場合には、 pickle モジュールを使ってください。 pickle は速度は同等で、バージョン間の互換性が保証されていて、 marshal より広範囲のオブジェクトをサポートしています。

### 警告

> marshal モジュールは、誤ったデータや悪意を持って作成されたデータに対する安全性を考慮していません。信頼できない、もしくは認証されていない出所からのデータを非整列化してはなりません。

> すべての Python オブジェクト型がサポートされているわけではありません。一般に、このモジュールによって読み書きすることができるオブジェクトは、その値が Python の特定の起動に依存していないオブジェクトに限ります。次の型がサポートされています。真偽値、整数、浮動小数点数、複素数、文字列、 byte 、bytearray 、タプル、リスト、 set 、frozenset 、辞書、コードオブジェクト。ここで、タプル、リスト、 set 、 frozenset 、辞書は、その中に含まれる値がそれ自身サポートされる場合に限りサポートされます。シングルトン None 、 Ellipsis 、 StopIteration も読み書き (marshalled and unmarshalled) できます。3 未満のフォーマット version では、再帰的なリスト、 set 、辞書を書き出すことはできません (下記参照)。

> There are functions that read/write files as well as functions operating on bytes-like objects.

> (ファイルを読み書きする機能と、バイト状のオブジェクトで動作する関数があります。)

このモジュールでは、以下の関数が定義されています。

属性|概要
----|----
marshal.dump(value, file[, version])|Write the value on the open file. The value must be a supported type. The file must be a writeable binary file.(開いているファイルに値を書き込みます。 値はサポートされている型でなければなりません。 ファイルは書き込み可能なバイナリファイルでなければなりません。)
marshal.load(file)|Read one value from the open file and return it. If no valid value is read (e.g. because the data has a different Python version’s incompatible marshal format), raise EOFError, ValueError or TypeError. The file must be a readable binary file.(開いているファイルから1つの値を読み取り、それを返します。 有効な値が読み取られない場合（データに異なるPythonバージョンの互換性のない整列形式があるなど）、EOFError、ValueErrorまたはTypeErrorを発生させます。 ファイルは読み込み可能なバイナリファイルでなければなりません。)
marshal.dumps(value[, version])|Return the bytes object that would be written to a file by dump(value, file). The value must be a supported type. Raise a ValueError exception if value has (or contains an object that has) an unsupported type.(dump（value、file）によってファイルに書き込まれるバイトオブジェクトを返します。 値はサポートされている型でなければなりません。 値がサポートされていない型を持つ（または持つオブジェクトを含む）場合は、ValueError例外を発生させます。)
marshal.loads(bytes)|Convert the bytes-like object to a value. If no valid value is found, raise EOFError, ValueError or TypeError. Extra bytes in the input are ignored.(バイトのようなオブジェクトを値に変換します。 有効な値が見つからない場合は、EOFError、ValueErrorまたはTypeErrorを発生させます。 入力の余分なバイトは無視されます。)

> これに加えて、以下の定数が定義されています:

属性|概要
----|----
marshal.version|このモジュールが利用するバージョンを表します。バージョン0 は歴史的なフォーマットです。バージョン1 は文字列の再利用をします。バージョン2 は浮動小数点数にバイナリフォーマットを使用します。バージョン3 はオブジェクトのインスタンス化と再帰をサポートします。現在のバージョンは4です。

この章はスルーする。使わなそうだし、.pycの作り方を調べるのが面倒だし、dumpの引数valueがわからないから。
