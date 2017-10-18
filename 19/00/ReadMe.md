# [11.9. linecache — テキストラインにランダムアクセスする](https://docs.python.jp/3/library/linecache.html)

< [11. ファイルとディレクトリへのアクセス](https://docs.python.jp/3/library/filesys.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/linecache.py](https://github.com/python/cpython/tree/3.6/Lib/linecache.py)

> linecache モジュールは、キャッシュ (一つのファイルから何行も読んでおくのが一般的です) を使って、内部で最適化を図りつつ、Python ソースファイルの任意の行を取得するのを可能にします。 traceback モジュールは、整形されたトレースバックにソースコードを含めるためにこのモジュールを利用しています。

> tokenize.open() 関数は、ファイルを開くために使用されます。この関数は、 tokenize.detect_encoding() を使用してファイルのエンコーディングを取得します。エンコーディングトークンが存在しない場合、デフォルトの UTF-8 になります。

> linecache モジュールでは次の関数が定義されています:

属性|意味
----|----
linecache.getline(filename, lineno, module_globals=None)|filename という名前のファイルから lineno 行目を取得します。この関数は決して例外を発生させません — エラーの際には '' を返します (行末の改行文字は、見つかった行に含まれます)。
linecache.clearcache()|キャッシュをクリアします。それまでに getline() を使って読み込んだファイルの行が必要でなくなったら、この関数を使ってください。
linecache.checkcache(filename=None)|キャッシュが有効かどうかを確認します。キャッシュしたファイルがディスク上で変更された可能性があり、更新後のバージョンが必要な場合にこの関数を使用します。 filename が与えられない場合、全てのキャッシュエントリを確認します。
linecache.lazycache(filename, module_globals)|Capture enough detail about a non-file-based module to permit getting its lines later via getline() even if module_globals is None in the later call. This avoids doing I/O until a line is actually needed, without having to carry the module globals around indefinitely.(後の呼び出しでmodule_globalsがNoneであってもgetline（）で後でその行を取得できるように、ファイルベースではないモジュールについての詳細を十分にキャプチャします。 これにより、モジュールのグローバルを無期限に運ぶ必要なく、実際に回線が必要になるまでI / Oを実行することがなくなります。)

```python
import linecache
print(linecache.getline(linecache.__file__, 8))
```

