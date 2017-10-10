# [11.1. pathlib — オブジェクト指向のファイルシステムパス](https://docs.python.jp/3/library/pathlib.html)

< [11. ファイルとディレクトリへのアクセス](https://docs.python.jp/3/library/filesys.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/pathlib.py](https://github.com/python/cpython/tree/3.6/Lib/pathlib.py)

> このモジュールでは様々なオペレーティングシステムに対して適切なセマンティクスでファイルシステムパスを表すクラスを提供しています。 Path クラスは 純粋パス と 具象パス からなります。 純粋パスは I/O を伴わない純粋なコンピューター操作を提供します。 具象パスは純粋パスを継承しますが I/O 操作も提供します。

> あなたが今までこのモジュールを使用したことがない場合や、タスクに適しているのがどのクラスかわからない場合は、 Path はきっとあなたに必要なものでしょう。 Path はコードが実行されているプラットフォーム用の 具象パス のインスタンスを作成します。

> 純粋パスは、以下のようないくつかの特殊なケースで有用です:

>     Unix マシン上で Windows のパスを扱いたいとき (またはその逆)。Unix 上で実行しているときに WindowsPath のインスタンスを作成することはできませんが、PureWindowsPath なら可能になります。

>     実際に OS にアクセスすることなしにパスを操作するだけのコードを確認したいとき。この場合、純粋クラスのインスタンスを一つ作成すれば、それが OS にアクセスすることはないので便利です。

> 参考

[PEP 428](https://www.python.org/dev/peps/pep-0428): The pathlib module – オブジェクト指向のファイルシステムパス。

> 参考

文字列による低水準のパス操作の場合は [os.path](https://docs.python.jp/3/library/os.path.html#module-os.path) も使用できます。 

## [11.1.1. 基本的な使い方](https://docs.python.jp/3/library/pathlib.html#basic-use)

```python
from pathlib import Path
p = Path('.')
print([x for x in p.iterdir() if x.is_dir()])
print(list(p.glob('**/*.py')))

p = Path('/etc')
q = p / 'init.d' / 'reboot'
print(q)
print(q.resolve())

print(q.exists())
print(q.is_dir())
with q.open() as f: f.readline()
```
```sh
$ python 0.py 
[]
[PosixPath('0.py')]
/etc/init.d/reboot
/etc/init.d/reboot
True
False
```

## [11.1.2. 純粋パス](https://docs.python.jp/3/library/pathlib.html#pure-paths)

> 純粋パスオブジェクトは実際にファイルシステムにアクセスしないパス操作処理を提供します。これらのクラスにアクセスするには 3 つの方法があり、それらを フレーバー と呼んでいます:

クラス|説明
------|----
class pathlib.PurePath(*pathsegments)|システムのパスのフレーバーを表すジェネリッククラスです (インスタンスを作成することで PurePosixPath または PureWindowsPath のどちらかが作成されます):
class pathlib.PurePosixPath(*pathsegments)|PurePath のサブクラスです。このパスフレーバーは非 Windows パスを表します:
class pathlib.PureWindowsPath(*pathsegments)|PurePath のサブクラスです。このパスフレーバーは Windows ファイルシステムパスを表します:

```python
from pathlib import *

print(PurePath('setup.py'))
print(PurePath('foo', 'some/path', 'bar'))
print(PurePath(Path('foo'), Path('bar')))
print(PurePath())
print(PurePath('/etc', '/usr', 'lib64'))

print(PureWindowsPath('c:/Windows', 'd:bar'))
print(PureWindowsPath('c:/Windows', '/Program Files'))
print(PurePath('foo//bar'))
print(PurePath('foo/./bar'))
print(PurePath('foo/../bar'))
```
```sh
$ python 1.py 
setup.py
foo/some/path/bar
foo/bar
.
/usr/lib64
d:bar
c:\Program Files
foo/bar
foo/bar
foo/../bar
```

### [11.1.2.1. 全般的な性質](https://docs.python.jp/3/library/pathlib.html#general-properties)

```python
from pathlib import *
print(PurePosixPath('foo') == PurePosixPath('FOO'))
print(PureWindowsPath('foo') == PureWindowsPath('FOO'))
print(PureWindowsPath('FOO') in { PureWindowsPath('foo') })
print(PureWindowsPath('C:') < PureWindowsPath('d:'))
print(PureWindowsPath('foo') == PurePosixPath('foo'))
print(PureWindowsPath('foo') < PurePosixPath('foo'))
```
```sh
$ python 2.py 
False
True
True
True
False
Traceback (most recent call last):
  File "2.py", line 7, in <module>
    print(PureWindowsPath('foo') < PurePosixPath('foo'))
TypeError: '<' not supported between instances of 'PureWindowsPath' and 'PurePosixPath'
```

### [11.1.2.2. 演算子](https://docs.python.jp/3/library/pathlib.html#operators)

```python
import os
from pathlib import *
p = PurePath('/etc')
print(os.fspath(p))
```
```sh
$ python 4.py 
/etc
```

```python
import os
from pathlib import *
p = PurePath('/etc')
print(str(p))
p = PureWindowsPath('c:/Program Files')
print(str(p))
print(bytes(p))
```
```sh
$ python 5.py 
/etc
c:\Program Files
b'c:\\Program Files'
```

> 注釈

> bytes での呼び出しは Unix 上での使用のみ推奨します。Windows では Unicode 形式が標準的なファイルシステムパス表現になります。 

### [11.1.2.3. 個別の構成要素へのアクセス](https://docs.python.jp/3/library/pathlib.html#accessing-individual-parts)

> パスの個別の “構成要素” へアクセスするには、以下のプロパティを使用します:

* `PurePath.parts` : パスのさまざまな構成要素へのアクセス手段を提供するタプルになります

```python
import os
from pathlib import *
p = PurePath('/usr/bin/python3')
print(p.parts)

p = PureWindowsPath('c:/Program Files/PSF')
print(p.parts)
```
```sh
$ python 6.py 
('/', 'usr', 'bin', 'python3')
('c:\\', 'Program Files', 'PSF')
```

### [11.1.2.4. メソッドとプロパティ](https://docs.python.jp/3/library/pathlib.html#methods-and-properties)

> 純粋パスは以下のメソッドとプロパティを提供します:

属性|説明
----|----
PurePath.drive|ドライブ文字または名前を表す文字列があればそれになります
PurePath.root|ローカルまたはグローバルルートを表す文字列があればそれになります
PurePath.anchor|ドライブとルートを結合した文字列になります
PurePath.parents|パスの論理的な上位パスにアクセスできるイミュータブルなシーケンスになります
PurePath.parent|パスの論理的な上位パスになります
PurePath.name|パス要素の末尾を表す文字列があればそれになります。ドライブやルートは含まれません
PurePath.suffix|末尾の要素に拡張子があればそれになります
PurePath.suffixes|パスのファイル拡張子のリストになります
PurePath.stem|パス要素の末尾から拡張子を除いたものになります
PurePath.as_posix()|フォワードスラッシュ (/) を使用したパスを表す文字列を返します
PurePath.as_uri()|file URI で表したパスを返します。絶対パスではない場合に ValueError を送出します。
PurePath.is_absolute()|パスが絶対パスかどうかを返します。パスが絶対パスとみなされるのは、ルートと (フレーバーが許す場合) ドライブとの両方が含まれる場合です
PurePath.is_reserved()|PureWindowsPath の場合はパスが Windows 上で予約されていれば True を返し、そうでなければ False を返します。PurePosixPath の場合は常に False を返します。
PurePath.joinpath(*other)|このメソッドの呼び出しは引数 other を順々に繋げることと等価になります
PurePath.match(pattern)|現在のパスが glob 形式で与えられたパターンと一致したら True を、一致しなければ False を返します。
PurePath.relative_to(*other)|other で表されたパスから現在のパスへの相対パスを返します。それが不可能だった場合はValueError が送出されます
PurePath.with_name(name)|現在のパスの name 部分を変更したパスを返します。オリジナルパスに name 部分がない場合はValueError が送出されます
PurePath.with_suffix(suffix)|現在のパスの suffix 部分を変更したパスを返します。オリジナルパスに suffix 部分がない場合は suffix を付けたものが返されます

```python
import os
from pathlib import *
print(PureWindowsPath('c:/Program Files/').drive)
print(PureWindowsPath('/Program Files/').drive)
print(PurePosixPath('/etc').drive)
print(PureWindowsPath('//host/share/foo.txt').drive)

print(PureWindowsPath('c:/Program Files/').root)
print(PureWindowsPath('c:Program Files/').root)
print(PurePosixPath('/etc').root)
print(PureWindowsPath('//host/share').root)

print(PureWindowsPath('c:/Program Files/').anchor)
print(PureWindowsPath('c:Program Files/').anchor)
print(PurePosixPath('/etc').anchor)
print(PureWindowsPath('//host/share').anchor)

p = PureWindowsPath('c:/foo/bar/setup.py')
print(p.parents[0])
print(p.parents[1])
print(p.parents[2])

p = PurePosixPath('/a/b/c/d')
print(p.parent)

p = PurePosixPath('/')
print(p.parent)
p = PurePosixPath('.')
print(p.parent)

p = PurePosixPath('foo/..')
print(p.parent)

print(PurePosixPath('my/library/setup.py').name)
print(PureWindowsPath('//some/share/setup.py').name)
print(PureWindowsPath('//some/share').name)

print(PurePosixPath('my/library/setup.py').suffix)
print(PurePosixPath('my/library.tar.gz').suffix)
print(PurePosixPath('my/library').suffix)

print(PurePosixPath('my/library.tar.gar').suffixes)
print(PurePosixPath('my/library.tar.gz').suffixes)
print(PurePosixPath('my/library').suffixes)

print(PurePosixPath('my/library.tar.gz').stem)
print(PurePosixPath('my/library.tar').stem)
print(PurePosixPath('my/library').stem)

p = PureWindowsPath('c:\\windows')
print(str(p))
print(p.as_posix())

p = PurePosixPath('/etc/passwd')
print(p.as_uri())
p = PureWindowsPath('c:/Windows')
print(p.as_uri())


print(PurePosixPath('/a/b').is_absolute())
print(PurePosixPath('a/b').is_absolute())

print(PureWindowsPath('c:/a/b').is_absolute())
print(PureWindowsPath('/a/b').is_absolute())
print(PureWindowsPath('c:').is_absolute())
print(PureWindowsPath('//some/share').is_absolute())

print(PureWindowsPath('nul').is_reserved())
print(PurePosixPath('nul').is_reserved())

print(PurePosixPath('/etc').joinpath('passwd'))
print(PurePosixPath('/etc').joinpath(PurePosixPath('passwd')))
print(PurePosixPath('/etc').joinpath('init.d', 'apache2'))
print(PureWindowsPath('c:').joinpath('/Program Files'))

print(PurePath('a/b.py').match('*.py'))
print(PurePath('/a/b/c.py').match('b/*.py'))
print(PurePath('/a/b/c.py').match('a/*.py'))

print(PurePath('/a.py').match('/*.py'))
print(PurePath('a/b.py').match('/*.py'))

print(PureWindowsPath('b.py').match('*.PY'))

p = PurePosixPath('/etc/passwd')
print(p.relative_to('/'))
print(p.relative_to('/etc'))
#p.relative_to('/usr')

p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
print(p.with_name('setup.py'))
p = PureWindowsPath('c:/')
#print(p.with_name('setup.py'))

p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
print(p.with_suffix('.bz2'))
p = PureWindowsPath('README')
print(p.with_suffix('.txt'))
```
```sh
$ python 7.py 
c:


\\host\share
\

/
\
c:\
c:
/
\\host\share\
c:\foo\bar
c:\foo
c:\
/a/b/c
/
.
foo
setup.py
setup.py

.py
.gz

['.tar', '.gar']
['.tar', '.gz']
[]
library.tar
library
library
c:\windows
c:/windows
file:///etc/passwd
file:///c:/Windows
True
False
True
False
False
True
True
False
/etc/passwd
/etc/passwd
/etc/init.d/apache2
c:\Program Files
True
True
False
True
False
True
etc/passwd
passwd
c:\Downloads\setup.py
c:\Downloads\pathlib.tar.bz2
README.txt
```

