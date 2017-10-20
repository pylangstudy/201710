# [11.11. macpath — Mac OS 9 のパス操作関数](https://docs.python.jp/3/library/macpath.html#module-macpath)

< [11. ファイルとディレクトリへのアクセス](https://docs.python.jp/3/library/filesys.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/macpath.py](https://github.com/python/cpython/tree/3.6/Lib/macpath.py)

> このモジュールは os.path モジュールの Macintosh 9 (およびそれ以前) 用の実装です。これを使用すると、古い形式の Macintosh のパス名を Mac OS X (あるいはその他の任意のプラットフォーム) 上で扱うことができます。

> 次の関数がこのモジュールで利用できます。 normcase() 、 normpath() 、 isabs() 、 join() 、 split() 、 isdir() 、 isfile() 、 walk() 、 exists() 。 os.path で利用できる他の関数については、ダミーの関数として相当する物が利用できます。

Mac機は持っていないし知らない。「Macの古いパス形式に対応」とあるが、どんな形式か知らない。不要と判断。

```python
import macpath
macpath.split('/tmp/a.txt')
```

