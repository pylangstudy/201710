# [12.5. dbm — Unix "データベース" へのインタフェース](https://docs.python.jp/3/library/dbm.html)

< [12. データの永続化](https://docs.python.jp/3/library/persistence.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/dbm/__init__.py](https://github.com/python/cpython/tree/3.6/Lib/dbm/__init__.py)

> dbm は DBM データベースのいくつかの種類 ( dbm.gnu または dbm.ndbm ) に対する汎用的なインタフェースです。これらのモジュールのどれもインストールされていなければ、モジュール dbm.dumb に含まれる低速だが単純な実装が使用されます。Oracle Berkeley DB に対する サードパーティのインタフェース があります。

属性|概要
----|----
exception dbm.error|サポートされているモジュールそれぞれによって送出される可能性のある例外を含むタプル。これにはユニークな例外があり、最初の要素として同じく dbm.error という名前の例外が含まれます — dbm.error が送出される場合、後者(訳注:タプルの dbm.error ではなく例外 dbm.error)が使用されます。
dbm.whichdb(filename)|この関数は、与えられたファイルを開くために、利用可能ないくつかの単純なデータベースモジュール — dbm.gnu, dbm.ndbm, dbm.dumb — のどれを使用すべきか推測を試みます。
dbm.open(file, flag='r', mode=0o666)|データベースファイル file を開いて対応するオブジェクトを返します。

> open() によって返されたオブジェクトは辞書とほとんど同じ機能をサポートします; キーとそれに対応付けられた値を記憶し、取り出し、削除することができ、 in 演算子や keys() メソッド、また get() や setdefault() を使うことができます。

> バージョン 3.2 で変更: get() と setdefault() がすべてのデータベースモジュールで利用できるようになりました。

> キーと値は常に byte 列として格納されます。これは、文字列が使用された場合は格納される前に暗黙的にデフォルトエンコーディングに変換されるということを意味します。

> これらのオブジェクトは、 with 文での使用にも対応しています。with 文を使用した場合、終了時に自動的に閉じられます。

> バージョン 3.4 で変更: open() が返すオブジェクトに対するコンテキスト管理のプロトコルがネイティブにサポートされました。

> 以下の例ではホスト名と対応するタイトルをいくつか記録し、データベースの内容を出力します:

```python
import dbm

# Open database, creating it if necessary.
with dbm.open('cache', 'c') as db:

    # Record some values
    db[b'hello'] = b'there'
    db['www.python.org'] = 'Python Website'
    db['www.cnn.com'] = 'Cable News Network'

    # Note that the keys are considered bytes now.
    assert db[b'www.python.org'] == b'Python Website'
    # Notice how the value is now in bytes.
    assert db['www.cnn.com'] == b'Cable News Network'

    # Often-used methods of the dict interface work too.
    print(db.get('python.org', b'not present'))

    # Storing a non-string key or value will raise an exception (most
    # likely a TypeError).
    db['www.yahoo.com'] = 4

# db is automatically closed when leaving the with statement.
```

### 参考

モジュール|概要
----------|----
shelve|非文字列データを記録する永続化モジュール。

> 個々のサブモジュールは以降の節で説明されます。


## [12.5.1. dbm.gnu — GNU による dbm 拡張](https://docs.python.jp/3/library/dbm.html#module-dbm.gnu)

ソースコード: [Lib/dbm/gnu.py](https://github.com/python/cpython/tree/3.6/Lib/dbm/gnu.py)

> このモジュールは dbm モジュールによく似ていますが、GNU ライブラリ gdbm を使っていくつかの追加機能を提供しています。 dbm.gnu と dbm.ndbm では生成されるファイル形式に互換性がないので注意してください。

> dbm.gnu モジュールでは GNU DBM ライブラリへのインタフェースを提供します。 dbm.gnu.gdbm オブジェクトはキーと値が必ず保存の前にバイト列に変換されることを除き、マップ型 (辞書型) と同じように動作します。 gdbm オブジェクトに対して print() を適用してもキーや値を印字することはなく、 items() 及び values() メソッドはサポートされていません。

属性|概要
----|----
exception dbm.gnu.error|I/O エラーのような dbm.gnu 特有のエラーで送出されます。誤ったキーの指定のように、一般的なマップ型のエラーに対しては KeyError が送出されます。
dbm.gnu.open(filename[, flag[, mode]])|gdbm データベースを開いて gdbm オブジェクトを返します。 filename 引数はデータベースファイルの名前です。
    gdbm.firstkey()|    このメソッドと nextkey() メソッドを使って、データベースの全てのキーにわたってループ処理を行うことができます。探索は gdbm の内部ハッシュ値の順番に行われ、キーの値に順に並んでいるとは限りません。このメソッドは最初のキーを返します。
    gdbm.nextkey(key)|    データベースの順方向探索において、key よりも後に来るキーを返します。以下のコードはデータベース db について、キー全てを含むリストをメモリ上に生成することなく全てのキーを出力します:
    gdbm.reorganize()|    大量の削除を実行した後、gdbm ファイルの占めるスペースを削減したい場合、このルーチンはデータベースを再組織化します。この再組織化を使用する方法以外に gdbm オブジェクトがデータベースファイルの大きさを短くすることはありません。サイズを縮小しない場合、削除された部分のファイルスペースは保持され、新たな (キー、値の) ペアが追加される際に再利用されます。
    gdbm.sync()|    データベースが高速モードで開かれていた場合、このメソッドはディスクにまだ書き込まれていないデータを全て書き込ませます。
    gdbm.close()|    gdbm データベースをクローズします。

```python
import dbm
#import dbm.gnu#ModuleNotFoundError: No module named '_gdbm'

with dbm.gnu.open('cache_gnu', 'c') as db:#AttributeError: module 'dbm' has no attribute 'gnu'
    db[b'hello'] = b'there'
    db['www.python.org'] = 'Python Website'
    db['www.cnn.com'] = 'Cable News Network'
    assert db[b'www.python.org'] == b'Python Website'
    assert db['www.cnn.com'] == b'Cable News Network'
    print(db.get('python.org', b'not present'))
#    db['www.yahoo.com'] = 4

    print(db.firstkey())
    k = db.firstkey()
    while k != None:
        print(k)
        k = db.nextkey(k)

    #大量の削除を実行した後、gdbm ファイルの占めるスペースを削減したい場合、このルーチンはデータベースを再組織化します。
#    db.reorganize()
```

エラーが出る。使い方がわからない。

## [12.5.2. dbm.ndbm — ndbm に基づくインタフェース](https://docs.python.jp/3/library/dbm.html#module-dbm.ndbm)

ソースコード: [Lib/dbm/ndbm.py](https://github.com/python/cpython/tree/3.6/Lib/dbm/ndbm.py)

> dbm.ndbm モジュールはUnixの"(n)dbm"ライブラリのインタフェースを提供します。 dbmオブジェクトは、キーと値が必ずバイト列である以外は辞書オブジェクトのようなふるまいをします。 print関数などで dbm オブジェクトを出力してもキーと値は出力されません。また、 items() と values() メソッドはサポートされません。

> このモジュールは、GNU GDBM互換インタフェースを持った "クラシックな" ndbmインタフェースを使うことができます。 Unix上のビルド時に configure スクリプトで適切なヘッダファイルが割り当られます。

属性|概要
----|----
exception dbm.ndbm.error|I/O エラーのような dbm.ndbm 特有のエラーで送出されます。誤ったキーの指定のように、一般的なマップ型のエラーに対しては KeyError が送出されます。
dbm.ndbm.library|ndbm が使用している実装ライブラリ名です。
dbm.ndbm.open(filename[, flag[, mode]])|dbmデータベースを開いて ndbm オブジェクトを返します。引数 filename はデータベースのファイル名を指定します。 (拡張子 .dir や .pag は付けません)。
    ndbm.close()|    ndbm データベースをクローズします。

## [12.5.3. dbm.dumb — 可搬性のある DBM 実装](https://docs.python.jp/3/library/dbm.html#module-dbm.dumb)

ソースコード: [Lib/dbm/dumb.py](https://github.com/python/cpython/tree/3.6/Lib/dbm/dumb.py)

> 注釈

> dbm.dumb モジュールは、 dbm が頑健なモジュールを他に見つけることができなかった際の最後の手段とされています。 dbm.dumb モジュールは速度を重視して書かれているわけではなく、他のデータベースモジュールのように重い使い方をするためのものではありません。

> dbm.dumb モジュールは永続性辞書に類似したインタフェースを提供し、全て Python で書かれています。 dbm.gnu のようなモジュールと異なり、外部ライブラリは必要ありません。他の永続性マップ型のように、キーおよび値は常にバイト列として保存されます。

> このモジュールは以下を定義します:

属性|概要
----|----
exception dbm.dumb.error|I/O エラーのような dbm.dumb 特有のエラーの際に送出されます。不正なキーを指定したときのような、一般的な対応付けエラーの際には KeyError が送出されます。
dbm.dumb.open(filename[, flag[, mode]])|dumbdbm データベースを開き、 dubmdbm オブジェクトを返します。 filename 引数はデータベースファイル名の雛型 (特定の拡張子をもたないもの) です。dumbdbm データベースが生成される際、 .dat および .dir の拡張子を持ったファイルが生成されます。
    dumbdbm.sync()|    ディスク上の辞書とデータファイルを同期します。このメソッドは Shelve.sync() メソッドから呼び出されます。
    dumbdbm.close()|    dumbdbm データベースをクローズします。

```python
import dbm
#import dbm.gnu#ModuleNotFoundError: No module named '_gdbm'
import dbm.dumb
with dbm.dumb.open('cache_gnu', 'c') as db:#AttributeError: module 'dbm' has no attribute 'dumb'
    db[b'hello'] = b'there'
    db['www.python.org'] = 'Python Website'
    db['www.cnn.com'] = 'Cable News Network'
    assert db[b'www.python.org'] == b'Python Website'
    assert db['www.cnn.com'] == b'Cable News Network'
    print(db.get('python.org', b'not present'))
#    db['www.yahoo.com'] = 4

    print(db)
    for k in db: print(k, db[k])
```
```sh
$ python 2.py 
b'not present'
<dbm.dumb._Database object at 0xb715ed0c>
b'hello' b'there'
b'www.python.org' b'Python Website'
b'www.cnn.com' b'Cable News Network'
```

