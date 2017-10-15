# [11.6. tempfile — 一時ファイルやディレクトリの作成](https://docs.python.jp/3/library/tempfile.html)

< [11. ファイルとディレクトリへのアクセス](https://docs.python.jp/3/library/filesys.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/tempfile.py](https://github.com/python/cpython/tree/3.6/Lib/tempfile.py)

> このモジュールは一時ファイルやディレクトリを作成します。 サポートされている全てのプラットフォームで動作します。 TemporaryFile、NamedTemporaryFile、TemporaryDirectory、 SpooledTemporaryFile は自動的に後始末をし、コンテクスト管理者として使うことの出来る高水準のインターフェイスです。 mkstemp() と mkdtemp() は手動で後始末をしなければならない低水準の関数です。

> ユーザが呼び出し可能な全ての関数とコンストラクタは追加の引数を受け取ります。 その引数によって一時ファイルやディレクトリの場所と名前を直接操作することが出来ます。 このモジュールに使用されるファイル名はランダムな文字を含みます。そのためファイルは共有された一時ディレクトリに安全に作成されます。 後方互換性を保つために引数の順序は若干奇妙です。 分かりやすさのためにキーワード引数を使用してください。

> このモジュールではユーザが呼び出し可能な以下の項目を定義しています:

属性|説明
----|----
tempfile.TemporaryFile(mode='w+b', buffering=None, encoding=None, newline=None, suffix=None, prefix=None, dir=None)|一時的な記憶領域として使うことの出来る file-like object を返します。
tempfile.NamedTemporaryFile(mode='w+b', buffering=None, encoding=None, newline=None, suffix=None, prefix=None, dir=None, delete=True)|この関数は、ファイルシステム上でファイルが可視の名前を持つことが保証される (Unix においてはディレクトリエントリが unlink されない) 点以外は TemporaryFile() と正確に同じことを行います。
tempfile.SpooledTemporaryFile(max_size=0, mode='w+b', buffering=None, encoding=None, newline=None, suffix=None, prefix=None, dir=None)|この関数はファイルサイズが max_size を超えるかファイルの fileno() メソッドが呼ばれるまで、データがメモリにスプールされる点以外は TemporaryFile() と正確に同じことを行います。 上記条件を満たすと内容はディスクに書き込まれ、操作は TemporaryFile() と同様に進みます。
tempfile.TemporaryDirectory(suffix=None, prefix=None, dir=None)|この関数は mkdtemp() と同じルールを使用して安全に一時ディレクトリを作成します。 返されたオブジェクトは、コンテクスト管理者として使用することができます (with文とコンテキストマネージャ を参照)。 コンテクストの完了や一時ディレクトリの破壊で新規作成された一時ディレクトリとその中身はファイルシステムから削除されます。
tempfile.mkstemp(suffix=None, prefix=None, dir=None, text=False)|可能な限り最も安全な手段で一時ファイルを生成します。 プラットフォームが os.open() の os.O_EXCL フラグを正しく実装している限り、ファイルの作成で競合が起こることはありません。 作成したユーザのユーザ ID からのみファイルを読み書き出来ます。 プラットフォームがファイルが実行可能かどうかを示す許可ビットを使用している場合、ファイルは誰からも実行不可です。 このファイルのファイル記述子は子プロセスに継承されません。
tempfile.mkdtemp(suffix=None, prefix=None, dir=None)|可能な限り安全な方法で一時ディレクトリを作成します。 ディレクトリの生成で競合は発生しません。 ディレクトリを作成したユーザ ID だけが、このディレクトリに対して内容を読み出したり、書き込んだり、検索したりすることができます。
tempfile.gettempdir()|一時ファイルに用いられるディレクトリの名前を返します。 これはモジュール内の全ての関数の dir 引数のデフォルト値を定義します。
tempfile.gettempdirb()|gettempdir() と同じですが返り値は bytesです。
tempfile.gettempprefix()|一時ファイルを生成する際に使われるファイル名の接頭辞を返します。 これにはディレクトリ部は含まれません。
tempfile.gettempprefixb()|gettempprefix() と同じですが返り値は bytes です。
tempfile.tempdir|None 以外の値に設定された場合、このモジュールで定義されている全ての関数の dir 引数のデフォルト値として定義されます。

## [11.6.1. 使用例](https://docs.python.jp/3/library/tempfile.html#examples)

tempfile モジュールの典型的な使用法のいくつかの例を挙げます:

```python
import tempfile

# create a temporary file and write some data to it
fp = tempfile.TemporaryFile()
fp.write(b'Hello world!')
# read data from file
fp.seek(0)
fp.read()
# close the file, it will be removed
fp.close()

# create a temporary file using a context manager
with tempfile.TemporaryFile() as fp:
    fp.write(b'Hello world!')
    fp.seek(0)
    fp.read()
# file is now closed and removed

# create a temporary directory using the context manager
with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)
# directory and contents have been removed
```

```sh
$ python 0.py 
created temporary directory /tmp/tmpyvawuvvc
```

## [11.6.2. 非推奨の関数と変数](https://docs.python.jp/3/library/tempfile.html#deprecated-functions-and-variables)

> 一時ファイルを作成する歴史的な手法は、まず mktemp() 関数でファイル名を作り、その名前を使ってファイルを作成するというものでした。 残念ながらこの方法は安全ではありません。 なぜなら、mktemp() の呼び出しと最初のプロセスが続いてファイル作成を試みる間に、異なるプロセスがその名前でファイルを同時に作成するかもしれないからです。 解決策は二つのステップを同時に行い、ファイルをすぐに作成するというものです。 この方法は mkstemp() や上述している他の関数で使用されています。

tempfile.mktemp(suffix='', prefix='tmp', dir=None)|バージョン 2.3 で撤廃: 代わりに mkstemp() を使って下さい。

```python
import tempfile
import os
f = tempfile.NamedTemporaryFile(delete=False)
print(f.name)
f.write(b"Hello World!\n")
f.close()
print(os.unlink(f.name))
print(os.path.exists(f.name))
```
```sh
$ python 1.py 
/tmp/tmp0nfrem0r
None
False
```
