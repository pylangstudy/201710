# [11.8. fnmatch — Unix ファイル名のパターンマッチ](https://docs.python.jp/3/library/fnmatch.html)

< [11. ファイルとディレクトリへのアクセス](https://docs.python.jp/3/library/filesys.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/fnmatch.py](https://github.com/python/cpython/tree/3.6/Lib/fnmatch.py)

> このモジュールは Unix のシェル形式のワイルドカードに対応しています。これらは、 (re モジュールでドキュメント化されている) 正規表現とは 異なります 。シェル形式のワイルドカードで使われる特殊文字は、次のとおりです。

Pattern|意味
-------|----
*|すべてにマッチします
?|任意の一文字にマッチします
[seq]|seq にある任意の文字にマッチします
[!seq]|seq にない任意の文字にマッチします

> リテラルにマッチさせるには、メタ文字を括弧に入れてください。例えば、'[?]' は文字 '?' にマッチします。

> ファイル名の区切り文字 (Unixでは '/') はこのモジュールに固有なものでは ない ことに注意してください。パス名展開については、 glob モジュールを参照してください (glob はパス名の部分にマッチさせるのに fnmatch() を使っています)。同様に、ピリオドで始まるファイル名はこのモジュールに固有ではなくて、 * と ? のパターンでマッチします。

属性|意味
----|----
fnmatch.fnmatch(filename, pattern)|filename の文字列が pattern の文字列にマッチするかテストして、 True 、 False のいずれかを返します。オペレーティングシステムが大文字、小文字を区別しない場合、比較を行う前に、両方のパラメタを全て大文字、または全て小文字に揃えます。オペレーティングシステムが標準でどうなっているかに関係なく、大小文字を区別して比較する場合には、 fnmatchcase() が使えます。
fnmatch.fnmatchcase(filename, pattern)|filename が pattern にマッチするかテストして、 True 、 False を返します。比較は大文字、小文字を区別します。
fnmatch.filter(names, pattern)|pattern にマッチする names のリストの部分集合を返します。[n for n in names if fnmatch(n, pattern)] と同じですが、もっと効率よく実装しています。
fnmatch.translate(pattern)|シェルスタイルの pattern を、re.match() で使用するための正規表現に変換して返します。

> 参考

> glob モジュール
>     Unix シェル形式のパス展開。

```python
import fnmatch
import glob
import os

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.py'):
        print(file)

print(fnmatch.fnmatchcase('0.py','*.py'))
print(fnmatch.filter(['0.py','1.py'], '*.py'))

import re
regex = fnmatch.translate('*.txt')
print(regex)
reobj = re.compile(regex)
print(reobj.match('foobar.txt'))
```
```sh
$ python 0.py 
0.py
True
['0.py', '1.py']
(?s:.*\.txt)\Z
<_sre.SRE_Match object; span=(0, 10), match='foobar.txt'>
```
