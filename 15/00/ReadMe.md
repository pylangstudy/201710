# [11.5. filecmp — ファイルおよびディレクトリの比較](https://docs.python.jp/3/library/filecmp.html)

< [11. ファイルとディレクトリへのアクセス](https://docs.python.jp/3/library/filesys.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/filecmp.py](https://github.com/python/cpython/tree/3.6/Lib/filecmp.py)

> filecmp モジュールでは、ファイルおよびディレクトリを比較するため、様々な時間／正確性のトレードオフに関するオプションを備えた関数を定義しています。ファイルの比較については、 difflib モジュールも参照してください。

> filecmp モジュールでは以下の関数を定義しています:

属性|説明
----|----
filecmp.cmp(f1, f2, shallow=True)|名前が f1 および f2 のファイルを比較し、二つのファイルが同じらしければ True を返し、そうでなければ False を返します。
filecmp.cmpfiles(dir1, dir2, common, shallow=True)|dir1 と dir2 ディレクトリの中の、common で指定されたファイルを比較します。
filecmp.clear_cache()|filecmp のキャッシュをクリアします。背後のファイルシステムの mtime 分解能未満でのファイル変更後にすぐに比較するような場合に有用です。

## [11.5.1. dircmp クラス](https://docs.python.jp/3/library/filecmp.html#the-dircmp-class)

属性|説明
----|----
class filecmp.dircmp(a, b, ignore=None, hide=None)|ディレクトリ a および b を比較するための新しいディレクトリ比較オブジェクトを生成します。
report()|a と b の比較を (sys.stdout に) 表示します。
report_partial_closure()|a および b およびそれらの直下にある共通のサブディレクトリ間での比較結果を出力します。
report_full_closure()|a および b およびそれらの共通のサブディレクトリ間での比較結果を (再帰的に比較して) 出力します。
left|ディレクトリ a です。
right|ディレクトリ b です。
left_list|a にあるファイルおよびサブディレクトリです。hide および ignore でフィルタされています。
right_list|b にあるファイルおよびサブディレクトリです。hide および ignore でフィルタされています。
common|a および b の両方にあるファイルおよびサブディレクトリです。
left_only|a だけにあるファイルおよびサブディレクトリです。
right_only|b だけにあるファイルおよびサブディレクトリです。
common_dirs|a および b の両方にあるサブディレクトリです。
common_files|a および b の両方にあるファイルです。
common_funny|a および b の両方にあり、ディレクトリ間でタイプが異なるか、 os.stat() がエラーを報告するような名前です。
same_files|クラスのファイル比較オペレータを用いて a と b の両方において同一のファイルです。
diff_files|a と b の両方に存在し、クラスのファイル比較オペレータに基づいて内容が異なるファイルです。
funny_files|a および b 両方にあるが、比較されなかったファイルです。
subdirs|common_dirs のファイル名を dircmp オブジェクトに対応付けた辞書です。
filecmp.DEFAULT_IGNORES|デフォルトで dircmp に無視されるディレクトリのリストです。


```python
import os
import stat
import filecmp
print(filecmp.cmp('a.txt','b.txt'))
print(filecmp.cmpfiles('a','b','a.txt'))
print(filecmp.clear_cache())

d = filecmp.dircmp('a','b')
print(d)
print(d.report())
print(d.report_partial_closure())
print(d.report_full_closure())
print(d.left)
print(d.right)
print(d.left_list)
print(d.right_list)
print(d.common)
print(d.left_only)
print(d.right_only)
print(d.common_dirs)
print(d.common_files)
print(d.common_funny)
print(d.same_files)
print(d.diff_files)
print(d.funny_files)
print(d.subdirs)
print(filecmp.DEFAULT_IGNORES)
```

```sh
$ python 0.py 
True
([], ['.'], ['a', 't', 'x', 't'])
None
<filecmp.dircmp object at 0xb71571ec>
diff a b
Identical files : ['a.txt']
None
diff a b
Identical files : ['a.txt']
None
diff a b
Identical files : ['a.txt']
None
a
b
['a.txt']
['a.txt']
['a.txt']
[]
[]
[]
['a.txt']
[]
['a.txt']
[]
[]
{}
['RCS', 'CVS', 'tags', '.git', '.hg', '.bzr', '_darcs', '__pycache__']
```

