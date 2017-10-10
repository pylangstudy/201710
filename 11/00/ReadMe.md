# [11.1. pathlib — オブジェクト指向のファイルシステムパス](https://docs.python.jp/3/library/pathlib.html)

< [11. ファイルとディレクトリへのアクセス](https://docs.python.jp/3/library/filesys.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/pathlib.py](https://github.com/python/cpython/tree/3.6/Lib/pathlib.py)

## [11.1.3.1. メソッド](https://docs.python.jp/3/library/pathlib.html#methods)

> 具象パスは純粋パスに加え、以下のメソッドを提供します。これらメソッドの多くはシステムコールが失敗すると OSError を送出します (例えばパスが存在しない場合):

属性|説明
----|----
classmethod Path.cwd()|(os.getcwd() が返す) 現在のディレクトリを表す新しいパスオブジェクトを返します:
classmethod Path.home()|ユーザーのホームディレクトリ (os.path.expanduser() での ~ の返り値) を表す新しいパスオブジェクトを返します:
Path.stat()|(os.stat() と同様の) 現在のパスに関する情報を返します。値はそれぞれのメソッドを呼び出した時点のものになります。
Path.chmod(mode)|os.chmod() のようにファイルのモードとアクセス権限を変更します:
Path.exists()|パスが既存のファイルかディレクトリを指しているかどうかを返します:
Path.expanduser()|パス要素 ~ および ~user を os.path.expanduser() が返すように展開した新しいパスオブジェクトを返します:
Path.glob(pattern)|現在のパスが表すディレクトリ内で pattern に一致する (あらゆる種類の) すべてのファイルを yield します:
Path.group()|ファイルを所有するグループ名を返します。ファイルの GID がシステムのデータベースに見つからなかった場合は KeyError が送出されます。
Path.is_dir()|パスがディレクトリ (またはディレクトリへのシンボリックリンク) を指していた場合 True を返し、その他の種類のファイルだった場合 False を返します。
Path.is_file()|パスが一般ファイル (または一般ファイルへのシンボリックリンク) を指していた場合 True を返します。その他の種類のファイルを指していた場合 False を返します。
Path.is_symlink()|パスがシンボリックリンクを指していた場合 True を返し、その他の場合は False を返します。
Path.is_socket()|パスが Unix ソケット (または Unix ソケットへのシンボリックリンク) を指していた場合 True を返します。その他の種類のファイルの場合 False を返します。
Path.is_fifo()|パスが FIFO (または FIFO へのシンボリックリンク) を指していた場合 True を返します。その他の種類のファイルの場合は False を返します。
Path.is_block_device()|パスがブロックデバイス (またはブロックデバイスへのシンボリックリンク) を指していた場合 True を返します。その他の種類のファイルの場合は False を返します。
Path.is_char_device()|パスがキャラクターデバイス (またはキャラクターデバイスへのシンボリックリンク) を指していた場合、True を返します。その他の種類のファイルの場合 False を返します。
Path.iterdir()|パスがディレクトリを指していた場合、ディレクトリの内容のパスオブジェクトを yield します:
Path.lchmod(mode)|Path.chmod() のように振る舞いますが、パスがシンボリックリンクを指していた場合、リンク先ではなくシンボリックリンク自身のモードが変更されます。
Path.lstat()|Path.stat() のように振る舞いますが、パスがシンボリックリンクを指していた場合、リンク先ではなくシンボリックリンク自身の情報を返します。
Path.mkdir(mode=0o777, parents=False, exist_ok=False)|与えられたパスに新しくディレクトリを作成します。mode が与えられていた場合、プロセスの umask 値と組み合わせてファイルのモードとアクセスフラグを決定します。パスがすでに存在していた場合 FileExistsError が送出されます。
Path.owner()|ファイルの所有者のユーザー名を返します。ファイルの UID がシステムのデータベースに見つからない場合 KeyError が送出されます。
Path.read_bytes()|指定されたファイルの内容をバイナリオブジェクトで返します:
Path.read_text(encoding=None, errors=None)|指定されたファイルの内容を文字列としてデコードして返します:
Path.rename(target)|このファイルかディレクトリを与えられた target にリネームします。 Unix では target が存在するファイルの場合、ユーザにパーミッションがあれば静かに置換されます。 target は文字列か別のパスオブジェクトです:
Path.replace(target)|現在のファイルまたはディレクトリの名前を target に変更します。target が既存のファイルかディレクトリを指していた場合、無条件に置き換えられます。
Path.resolve(strict=False)|パスを絶対パスにし、あらゆるシンボリックリンクを解決します。新しいパスオブジェクトが返されます:
Path.rglob(pattern)|これは Path.glob() を pattern の先頭に “**” を追加して呼び出した場合と似ています:
Path.rmdir()|現在のディレクトリを削除します。ディレクトリは空でなければなりません。
Path.samefile(other_path)|このパスが参照するファイルが other_path (Path オブジェクトか文字列) と同じであれば True を、異なるファイルであれば False を返します。意味的には os.path.samefile() および os.path.samestat() と同じです。
Path.symlink_to(target, target_is_directory=False)|現在のパスに target へのシンボリックリンクを作成します。Windows では、リンク対象がディレクトリの場合 target_is_directory が真でなければなりません (デフォルトは False)。POSIX では、target_is_directory の値は無視されます。
Path.touch(mode=0o666, exist_ok=True)|与えられたパスにファイルを作成します。mode が与えられた場合、プロセスの umask 値と組み合わせてファイルのモードとアクセスフラグが決定されます。ファイルがすでに存在した場合、exist_ok が真ならばこの関数は正常に終了します (そしてファイルの更新日付が現在の日時に変更されます)。その他の場合は FileExistsError が送出されます。
Path.unlink()|このファイルまたはシンボリックリンクを削除します。パスがディレクトリを指している場合は Path.rmdir() を使用してください。
Path.write_bytes(data)|指定されたファイルをバイトモードで開き、data を書き込み、ファイルを閉じます:
Path.write_text(data, encoding=None, errors=None)|指定されたファイルをテキストモードで開き、data を書き込み、ファイルを閉じます:

```python
from pathlib import Path, PosixPath
print(Path.cwd())
print(Path.home())
p = Path('0.py')
print(p.stat())
print(p.stat().st_mode)
print(p.chmod(p.stat().st_mode))
#print(Path.chmod(p.stat().st_mode))
#print(Path.chmod(oct(p.stat().st_mode)))
print(Path('.').exists())
p = PosixPath('~/films/Monty Python')
print(p.expanduser())
print(sorted(Path('.').glob('*.py')))
print(sorted(Path('.').glob('*/*.py')))
print(sorted(Path('.').glob('**/*.py')))

p = Path('0.py')
print(p.group())
print(p.is_dir())
print(p.is_file())
print(p.is_symlink())
print(p.is_socket())
print(p.is_fifo())
print(p.is_block_device())
print(p.is_char_device())
print(p.iterdir())
#print(p.lchmod())
print(p.lstat())
print(Path('dir').mkdir(mode=0o777, parents=True, exist_ok=True))
print(p.open())
print(p.owner())
print(p.read_bytes())
print(p.read_text())
#print(p.rename(Path('dir')))
#print(p.replace(Path('dir')))
print(p.resolve())
```
```sh
$ python 0.py 
/.../pylangstudy/201710/11/00
/home/user
os.stat_result(st_mode=33188, st_ino=24904715, st_dev=2085, st_nlink=1, st_uid=1000, st_gid=1000, st_size=912, st_atime=1507676653, st_mtime=1507676652, st_ctime=1507676652)
33188
None
True
/home/user/films/Monty Python
[PosixPath('0.py'), PosixPath('1.py'), PosixPath('2.py'), PosixPath('3.py'), PosixPath('4.py'), PosixPath('5.py'), PosixPath('6.py'), PosixPath('7.py')]
[]
[PosixPath('0.py'), PosixPath('1.py'), PosixPath('2.py'), PosixPath('3.py'), PosixPath('4.py'), PosixPath('5.py'), PosixPath('6.py'), PosixPath('7.py')]
mint
False
True
False
False
False
False
False
<generator object Path.iterdir at 0xb707b62c>
os.stat_result(st_mode=33188, st_ino=24904715, st_dev=2085, st_nlink=1, st_uid=1000, st_gid=1000, st_size=912, st_atime=1507676653, st_mtime=1507676652, st_ctime=1507676654)
None
<_io.TextIOWrapper name='0.py' mode='r' encoding='UTF-8'>
mint
b"from pathlib import Path, PosixPath\nprint(Path.cwd())\nprint(Path.home())\np = Path('0.py')\nprint(p.stat())\nprint(p.stat().st_mode)\nprint(p.chmod(p.stat().st_mode))\n#print(Path.chmod(p.stat().st_mode))\n#print(Path.chmod(oct(p.stat().st_mode)))\nprint(Path('.').exists())\np = PosixPath('~/films/Monty Python')\nprint(p.expanduser())\nprint(sorted(Path('.').glob('*.py')))\nprint(sorted(Path('.').glob('*/*.py')))\nprint(sorted(Path('.').glob('**/*.py')))\n\np = Path('0.py')\nprint(p.group())\nprint(p.is_dir())\nprint(p.is_file())\nprint(p.is_symlink())\nprint(p.is_socket())\nprint(p.is_fifo())\nprint(p.is_block_device())\nprint(p.is_char_device())\nprint(p.iterdir())\n#print(p.lchmod())\nprint(p.lstat())\nprint(Path('dir').mkdir(mode=0o777, parents=True, exist_ok=True))\nprint(p.open())\nprint(p.owner())\nprint(p.read_bytes())\nprint(p.read_text())\n#print(p.rename(Path('dir')))\n#print(p.replace(Path('dir')))\nprint(p.resolve())\n\n"
from pathlib import Path, PosixPath
print(Path.cwd())
print(Path.home())
p = Path('0.py')
print(p.stat())
print(p.stat().st_mode)
print(p.chmod(p.stat().st_mode))
#print(Path.chmod(p.stat().st_mode))
#print(Path.chmod(oct(p.stat().st_mode)))
print(Path('.').exists())
p = PosixPath('~/films/Monty Python')
print(p.expanduser())
print(sorted(Path('.').glob('*.py')))
print(sorted(Path('.').glob('*/*.py')))
print(sorted(Path('.').glob('**/*.py')))

p = Path('0.py')
print(p.group())
print(p.is_dir())
print(p.is_file())
print(p.is_symlink())
print(p.is_socket())
print(p.is_fifo())
print(p.is_block_device())
print(p.is_char_device())
print(p.iterdir())
#print(p.lchmod())
print(p.lstat())
print(Path('dir').mkdir(mode=0o777, parents=True, exist_ok=True))
print(p.open())
print(p.owner())
print(p.read_bytes())
print(p.read_text())
#print(p.rename(Path('dir')))
#print(p.replace(Path('dir')))
print(p.resolve())


/.../pylangstudy/201710/11/00/0.py
```

