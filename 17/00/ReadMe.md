# [11.7. glob — Unix 形式のパス名のパターン展開](https://docs.python.jp/3/library/glob.html)

< [11. ファイルとディレクトリへのアクセス](https://docs.python.jp/3/library/filesys.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/glob.py](https://github.com/python/cpython/tree/3.6/Lib/glob.py)

> The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in arbitrary order. No tilde expansion is done, but *, ?, and character ranges expressed with [] will be correctly matched. This is done by using the os.scandir() and fnmatch.fnmatch() functions in concert, and not by actually invoking a subshell. Note that unlike fnmatch.fnmatch(), glob treats filenames beginning with a dot (.) as special cases. (For tilde and shell variable expansion, use os.path.expanduser() and os.path.expandvars().)

[Google翻訳](https://translate.google.co.jp/?hl=ja#en/ja/The%20glob%20module%20finds%20all%20the%20pathnames%20matching%20a%20specified%20pattern%20according%20to%20the%20rules%20used%20by%20the%20Unix%20shell%2C%20although%20results%20are%20returned%20in%20arbitrary%20order.%20No%20tilde%20expansion%20is%20done%2C%20but%20*%2C%20%3F%2C%20and%20character%20ranges%20expressed%20with%20%5B%5D%20will%20be%20correctly%20matched.%20This%20is%20done%20by%20using%20the%20os.scandir()%20and%20fnmatch.fnmatch()%20functions%20in%20concert%2C%20and%20not%20by%20actually%20invoking%20a%20subshell.%20Note%20that%20unlike%20fnmatch.fnmatch()%2C%20glob%20treats%20filenames%20beginning%20with%20a%20dot%20(.)%20as%20special%20cases.%20(For%20tilde%20and%20shell%20variable%20expansion%2C%20use%20os.path.expanduser()%20and%20os.path.expandvars().))

> globモジュールは、Unixシェルが使用する規則に従って、指定されたパターンに一致するすべてのパス名を検索しますが、結果は任意の順序で返されます。 チルダの展開は行われませんが、[]で表される*、？、および文字の範囲は正しく一致します。 これは、実際にサブシェルを呼び出すのではなく、os.scandir（）とfnmatch.fnmatch（）関数を同時に使用して行います。 fnmatch.fnmatch（）とは異なり、globは特別な場合としてドット（。）で始まるファイル名を扱うことに注意してください。 （ティルドとシェル変数の拡張の場合は、os.path.expanduser（）とos.path.expandvars（）を使用します）。

> リテラルにマッチさせるには、メタ文字を括弧に入れてください。例えば、'[?]' は文字 '?' にマッチします。

> 参考

> pathlib モジュールは高水準のパスオブジェクトを提供します。 

```python
import glob
print(glob.glob('./[0-9].*'))
print(glob.glob('*.py'))
print(glob.glob('?.py'))
print(glob.glob('**/*.py', recursive=True))
print(glob.glob('./**/', recursive=True))
```
```sh
$ python 0.py 
['./0.py', './1.py']
['0.py', '1.py']
['0.py', '1.py']
['0.py', '1.py']
['./']
```

