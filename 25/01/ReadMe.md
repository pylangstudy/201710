# [12.3. shelve — Python オブジェクトの永続化](https://docs.python.jp/3/library/shelve.html)

< [12. データの永続化](https://docs.python.jp/3/library/persistence.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/shelve.py](https://github.com/python/cpython/tree/3.6/Lib/shelve.py)

> "シェルフ (shelf, 棚)" は辞書に似た永続性を持つオブジェクトです。 "dbm" データベースとの違いは、シェルフの値 (キーではありません！) は実質上どんな Python オブジェクトにも — pickle モジュールが扱えるなら何でも — できるということです。これにはほとんどのクラスインスタンス、再帰的なデータ型、沢山の共有されたサブオブジェクトを含むオブジェクトが含まれます。キーは通常の文字列です。

shelve.open(filename, flag='c', protocol=None, writeback=False)|永続的な辞書を開きます。指定された filename は、根底にあるデータベースの基本ファイル名となります。副作用として、 filename には拡張子がつけられる場合があり、ひとつ以上のファイルが生成される可能性もあります。デフォルトでは、根底にあるデータベースファイルは読み書き可能なように開かれます。オプションの flag パラメータは dbm.open() における flag パラメータと同様に解釈されます。

### 注釈

> シェルフが自動的に閉じることに依存しないでください; それがもう必要ない場合は常に close() を明示的に呼ぶか、 shelve.open() をコンテキストマネージャとして使用してください:

```python
import shelve
with shelve.open('spam') as db:
    db['eggs'] = 'eggs'
    db['日本語'] = '値'
    print(db)
    print(db['eggs'])
    print(db['日本語'])
```
```sh
$ python 0.py 
<shelve.DbfilenameShelf object at 0xb717cd0c>
eggs
値
```

### 警告

> shelve モジュールは裏で pickle を使っているので、信頼できないソースからシェルフを読み込むのは危険です。 pickle と同じく、 shelf の読み込みでも任意のコードを実行できるからです。

> シェルフオブジェクトは辞書がサポートする全てのメソッドをサポートしています。これにより、辞書ベースのスクリプトから永続的な記憶媒体を必要とするスクリプトに容易に移行できるようになります。

> 追加でサポートされるメソッドが二つあります:

属性|概要
----|----
Shelf.sync()|シェルフが writeback を True にセットして開かれている場合に、キャッシュ中の全てのエントリを書き戻します。また可能な場合は、キャッシュを空にしてディスク上の永続的な辞書を同期します。このメソッドはシェルフを close() によって閉じるとき自動的に呼び出されます。
Shelf.close()|永続的な 辞書 オブジェクトを同期して閉じます。既に閉じられているシェルフに対して呼び出すと ValueError を出し失敗します。

### 参考

通常の辞書に近い速度をもち、いろいろなストレージフォーマットに対応した、 [永続化辞書のレシピ](https://code.activestate.com/recipes/576642/)。

## [12.3.1. 制限事項](https://docs.python.jp/3/library/shelve.html#restrictions)

> どのデータベースパッケージが使われるか (例えば dbm.ndbm 、 dbm.gnu) は、どのインタフェースが利用可能かに依存します。従って、データベースを dbm を使って直接開く方法は安全ではありません。データベースはまた、 dbm が使われた場合 (不幸なことに) その制約に縛られます — これはデータベースに記録されたオブジェクト (の pickle 化された表現) はかなり小さくなければならず、キー衝突が生じた場合に、稀にデータベースを更新することができなくなることを意味します。
    shelve モジュールは、シェルフに置かれたオブジェクトの 並列した 読み出し/書き込みアクセスをサポートしません (複数の同時読み出しアクセスは安全です)。あるプログラムが書き込みのために開かれたシェルフを持っているとき、他のプログラムはそのシェルフを読み書きのために開いてはいけません。この問題を解決するために Unix のファイルロック機構を使うことができますが、この機構は Unix のバージョン間で異なり、使われているデータベースの実装について知識が必要となります。

class shelve.Shelf(dict, protocol=None, writeback=False, keyencoding='utf-8')|collections.abc.MutableMapping のサブクラスで、 dict オブジェクト内にpickle化された値を保持します。

    デフォルトでは、値を整列化する際にはバージョン 3 の pickle 化が用いられます。pickle 化プロトコルのバージョンは protocol パラメータで指定することができます。pickle 化プロトコルについては pickle のドキュメントを参照してください。

    writeback パラメータが True に設定されていれば、アクセスされたすべてのエントリはメモリ上にキャッシュされ、ファイルを閉じる際に dict に書き戻されます; この機能により、可変のエントリに対して自然な操作が可能になりますが、さらに多くのメモリを消費し、辞書をファイルと同期して閉じる際に長い時間がかかるようになります。

    keyencoding パラメータは、shelf の背後にある dict に対して使われる前にキーをエンコードするのに使用されるエンコーディングです。

    Shelf オブジェクトは、コンテキストマネージャとしても使用できます。この場合、 with ブロックが終了する際に、自動的に閉じられます。

    バージョン 3.2 で変更: keyencoding パラメータを追加; 以前はキーは常に UTF-8 でエンコードされていました。

    バージョン 3.4 で変更: コンテキストマネージャーサポートが追加されました。

class shelve.BsdDbShelf(dict, protocol=None, writeback=False, keyencoding='utf-8')(原文)

> Shelf のサブクラスで、 first(), next(), previous(), last(), set_location() メソッドを外部に提供しています。これらのメソッドは pybsddb にあるサードパーティの bsddb モジュールでは利用可能ですが、他のデータベースモジュールでは利用できません。コンストラクタに渡される dict オブジェクトは上記のメソッドをサポートしていなくてはなりません。通常は、 bsddb.hashopen(), bsddb.btopen() または bsddb.rnopen() のいずれかを呼び出して得られるオブジェクトが条件を満たしています。オプションの protocol, writeback および keyencoding パラメータは Shelf クラスにおけるパラメータと同様に解釈されます。

class shelve.DbfilenameShelf(filename, flag='c', protocol=None, writeback=False)|Shelf のサブクラスで、辞書に似たオブジェクトの代わりに filename を受理します。根底にあるファイルは dbm.open() を使って開かれます。デフォルトでは、ファイルは読み書き可能な状態で開かれます。オプションの flag パラメータは open() 関数におけるパラメータと同様に解釈されます。オプションの protocol および writeback パラメータは Shelf クラスにおけるパラメータと同様に解釈されます。

## [12.3.2. 使用例](https://docs.python.jp/3/library/shelve.html#example)

> インタフェースは以下のコードに集約されています (key は文字列で、data は任意のオブジェクトです):

```python
#!python3.6
#encoding:utf-8
import shelve
filename = 'shelve_file'
d = shelve.open(filename)  # open -- file may get suffix added by low-level
                           # library
key = 'key1'
data = 'value1'
d[key] = data              # store data at key (overwrites old data if
                           # using an existing key)
data = d[key]              # retrieve a COPY of data at key (raise KeyError
                           # if no such key)
del d[key]                 # delete data stored at key (raises KeyError
                           # if no such key)

flag = key in d            # true if the key exists
klist = list(d.keys())     # a list of all existing keys (slow!)
print('flag=', flag)
print('klist=', klist)

# as d was opened WITHOUT writeback=True, beware:
d['xx'] = [0, 1, 2]        # this works as expected, but...
print("d['xx']=", d['xx'])
d['xx'].append(3)          # *this doesn't!* -- d['xx'] is STILL [0, 1, 2]!
print("d['xx']=", d['xx'])

# having opened d without writeback=True, you need to code carefully:
temp = d['xx']             # extracts the copy
temp.append(5)             # mutates the copy
d['xx'] = temp             # stores the copy right back, to persist it
print("d['xx']=", d['xx'])

# or, d=shelve.open(filename,writeback=True) would let you just code
# d['xx'].append(5) and have it work as expected, BUT it would also
# consume more memory and make the d.close() operation slower.

d.close()                  # close it
```
```sh
$ python 1.py 
flag= False
klist= []
d['xx']= [0, 1, 2]
d['xx']= [0, 1, 2]
d['xx']= [0, 1, 2, 5]
```

### 参考

モジュール|概要
----------|----
[dbm](https://docs.python.jp/3/library/dbm.html#module-dbm)|dbm スタイルのデータベースに対する共通インタフェース。
[pickle](https://docs.python.jp/3/library/pickle.html#module-pickle)|shelve によって使われるオブジェクト整列化機構。


