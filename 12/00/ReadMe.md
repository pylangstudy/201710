# [11.2. os.path — 共通のパス名操作](https://docs.python.jp/3/library/os.path.html)

< [11. ファイルとディレクトリへのアクセス](https://docs.python.jp/3/library/filesys.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/posixpath.py](https://github.com/python/cpython/tree/3.6/Lib/posixpath.py) (POSIX), [Lib/ntpath.py](https://github.com/python/cpython/tree/3.6/Lib/ntpath.py) (Windows NT), [Lib/macpath.py](https://github.com/python/cpython/tree/3.6/Lib/macpath.py) (Mac)

> このモジュールには、パス名を操作する便利な関数が実装されています。ファイルの読み書きに関しては open() を、ファイルシステムへのアクセスに関しては os モジュールを参照してください。パスパラメータは文字列またはバイト列で渡すことができます。アプリケーションは、ファイル名を Unicode 文字列で表すことが推奨されています。残念ながら、Unix では文字列で表すことのできないファイル名があるため、Unix 上で任意のファイル名をサポートする必要のあるアプリケーションは、そのパス名にバイト列を使用すべきです。逆に、バイト列オブジェクトを使用すると Windows (標準の mbcs エンコーディング) 上ではすべてのファイル名を表すことができないため、Windows アプリケーションはファイルアクセスのために文字列オブジェクトを使用するべきです。

> Unix シェルとは異なり、Python はあらゆるパス展開を 自動的には 行いません。アプリケーションがシェルのようなパス展開を必要とした場合は、 expanduser() や expandvars() といった関数を明示的に呼び出すことで行えます。(glob モジュールも参照してください)

> 参考

> pathlib モジュールは高水準のパスオブジェクトを提供します。

> 注釈

> 以下のすべての関数は、そのパラメータにバイト列のみ、あるいは文字列のみ受け付けます。パスまたはファイル名を返す場合、返り値は同じ型のオブジェクトになります。

> 注釈

> OS によって異なるパス名の決まりがあるため、標準ライブラリにはこのモジュールのいくつかのバージョンが含まれています。 os.path モジュールは常に現在 Python が動作している OS に適したパスモジュールであるため、ローカルのパスを扱うのに適しています。各々のモジュールをインポートして 常に 一つのフォーマットを利用することも可能です。これらはすべて同じインタフェースを持っています:

>    posixpath UNIX スタイルのパス用

>    ntpath Windows パス用

>    macpath 古いスタイルの MacOS パス用

メソッド|説明
--------|----
os.path.abspath(path)|パス名 path の正規化された絶対パスを返します。ほとんどのプラットフォームでは、これは関数 normpath() を次のように呼び出した時と等価です: normpath(join(os.getcwd(), path))。
os.path.basename(path)|パス名 path の末尾のファイル名部分を返します。これは関数 split() に path を渡した時に返されるペアの 2 番めの要素です。この関数が返すのは Unix の basename とは異なります; Unix の basename は '/foo/bar/' に対して 'bar' を返しますが、関数 basename() は空文字列 ('') を返します。
os.path.commonpath(paths)|シーケンス paths 中の各パス名に共通するサブパスのうち、最も長いものを返します。paths に絶対パス名と相対パス名の両方が含まれているか、paths が空の場合、 ValueError を送出します。commonprefix() とは異なり、有効なパスを返します。
os.path.commonprefix(list)|list 内のすべてのパスに共通する接頭辞のうち、最も長いものを (パス名の 1 文字 1 文字を判断して) 返します。list が空の場合、空文字列 ('') を返します。
os.path.dirname(path)|パス名 path のディレクトリ名を返します。これは関数 split() に path を渡した時に返されるペアの 1 番めの要素です。
os.path.exists(path)|path が実在するパスかオープンしているファイル記述子を参照している場合 True を返します。壊れたシンボリックリンクについては False を返します。一部のプラットフォームでは、たとえ path が物理的に存在していたとしても、要求されたファイルに対する os.stat() の実行権がなければこの関数が False を返すことがあります。
os.path.lexists(path)|path が実在するパスなら True を返します。壊れたシンボリックリンクについては True を返します。 os.lstat() がない環境では exists() と等価です。
os.path.expanduser(path)|Unix および Windows では、与えられた引数の先頭のパス要素 ~ 、または ~user を、 user のホームディレクトリのパスに置き換えて返します。
os.path.expandvars(path)|引数のパスの環境変数を展開して返します。引数の中の $name または ${name} のような形式の文字列は環境変数、 name の値に置き換えられます。不正な変数名や存在しない変数名の場合には変換されず、そのまま返します。
os.path.getatime(path)|path に最後にアクセスした時刻を、エポック (time モジュールを参照) からの経過時間を示す秒数で返します。ファイルが存在しない、あるいはアクセスできなかった場合は OSError を送出します。
os.path.getmtime(path)|path を最後に更新した時刻を、エポック (time モジュールを参照) からの経過時間を示す秒数で返します。ファイルが存在しない、あるいはアクセスできなかった場合は OSError を送出します。
os.path.getctime(path)|システムの ctime、Unix系など一部のシステムでは最後にメタデータが変更された時刻、Windows などその他のシステムでは path の作成時刻を返します。返り値はエポック (time モジュールを参照) からの経過時間を示す秒数になります。ファイルが存在しない、あるいはアクセスできなかった場合は OSError を送出します。
os.path.getsize(path)|path のサイズをバイト数で返します。ファイルが存在しない、あるいはアクセスできなかった場合は OSError を送出します。
os.path.isabs(path)|path が絶対パスなら True を返します。すなわち、 Unix ではスラッシュで始まり、 Windows ではドライブレターに続く (バック) スラッシュで始まる場合です。
os.path.isfile(path)|path が実在する一般ファイルなら True を返します。シンボリックリンクの場合にはその実体をチェックするので、同じパスに対して islink() と isfile() の両方が True を返すことがあります。
os.path.isdir(path)|path が実在するディレクトリなら True を返します。シンボリックリンクの場合にはその実体をチェックするので、同じパスに対して islink() と isdir() の両方が True を返すことがあります。
os.path.islink(path)|path がシンボリックリンクなら True を返します。Python ランタイムでシンボリックリンクがサポートされていないプラットフォームでは、常に False を返します。
os.path.ismount(path)|パス名 path がマウントポイント mount point (ファイルシステムの中で異なるファイルシステムがマウントされているところ) なら、 True を返します。POSIX では、この関数は path の親ディレクトリである path/.. が path と異なるデバイス上にあるか、あるいは path/.. と path が同じデバイス上の同じ i-node を指しているかをチェックします — これによって全ての Unix 系システムと POSIX 標準でマウントポイントが検出できます。Windows では、ドライブレターを持つルートと共有 UNC は常にマウントポイントであり、また他のパスでは、入力のパスが異なるデバイスからのものか見るために GetVolumePathName が呼び出されます。
os.path.join(path, *paths)|1 つあるいはそれ以上のパスの要素を賢く結合します。戻り値は path、ディレクトリの区切り文字 (os.sep) を *paths の各パートの(末尾でない場合の空文字列を除いて)頭に付けたもの、これらの結合になります。最後の部分が空文字列の場合に限り区切り文字で終わる文字列になります。付け加える要素に絶対パスがあれば、それより前の要素は全て破棄され、以降の要素を結合します。
os.path.normpath(path)|パスを正規化します。余分な区切り文字や上位レベル参照を除去し、A//B、A/B/、A/./B や A/foo/../B などはすべて A/B になります。この文字列操作は、シンボリックリンクを含むパスの意味を変えてしまう場合があります。Windows では、スラッシュをバックスラッシュに変換します。大文字小文字の正規化には normcase() を使用してください。
os.path.realpath(path)|パスの中のシンボリックリンク (もしそれが当該オペレーティングシステムでサポートされていれば) を取り除いて、指定されたファイル名を正規化したパスを返します。
os.path.relpath(path, start=os.curdir)|カレントディレクトリあるいはオプションの start ディレクトリからの path への相対パスを返します。これはパス計算で行っており、ファイルシステムにアクセスして path や start の存在や性質を確認することはありません。
os.path.samefile(path1, path2)|引数の両パス名が同じファイルまたはディレクトリを参照している場合、 True を返します。これは、デバイス番号と i-node 番号で決定されます。どちらかのパス名への os.stat() 呼び出しが失敗した場合、例外が送出されます。
os.path.sameopenfile(fp1, fp2)|ファイル記述子 fp1 と fp2 が同じファイルを参照していたら True を返します。
os.path.samestat(stat1, stat2)|stat タプル stat1 と stat2 が同じファイルを参照していれば True を返します。これらのタプルは os.fstat() 、 os.lstat() あるいは os.stat() の返り値で構いません。この関数は samefile() と sameopenfile() を使用した比較に基いて実装しています。
os.path.split(path)|パス名 path を (head, tail) のペアに分割します。 tail はパス名の構成要素の末尾で、 head はそれより前の部分です。 tail はスラッシュを含みません; もし path がスラッシュで終わっていれば tail は空文字列になります。もし path にスラッシュがなければ、 head は空文字になります。 path が空文字なら、 head と tail の両方が空文字になります。 head の末尾のスラッシュは head がルートディレクトリ (または 1 個以上のスラッシュだけ) でない限り取り除かれます。 join(head, tail) は常に path と同じ場所を返しますが、文字列としては異なるかもしれません。関数 dirname(), basename() も参照してください。
os.path.splitdrive(path)|パス名 path を (drive, tail) のペアに分割します。drive はマウントポイントか空文字列になります。ドライブ指定をサポートしていないシステムでは、drive は常に空文字になります。どの場合でも、drive + tail は path と等しくなります。
os.path.splitext(path)|パス名 path を (root, ext) のペアに分割します。 root + ext == path になります。 ext は空文字列か 1 つのピリオドで始まり、多くても 1 つのピリオドを含みます。ベースネームを導出するピリオドは無視されます; splitext('.cshrc') は ('.cshrc', '') を返します。
os.path.splitunc(path)|バージョン 3.1 で撤廃: 代わりに splitdrive を使ってください。
os.path.supports_unicode_filenames|ファイル名に任意の Unicode 文字列を (システムの制限内で) 使用できる場合は True になります。

```python
import os
print(os.path.abspath('.'))
print(os.path.basename('/tmp/abc.py'))
print(os.path.commonpath(['/tmp/abc.py', '/tmp/def.py']))
print(os.path.commonprefix(['/usr/lib', '/usr/local/lib']))
print(os.path.dirname('/tmp/abc.py'))
print(os.path.exists('./0.py'))
print(os.path.lexists('./0.py'))
print(os.path.expanduser('./0.py'))
print(os.path.expandvars('./0.py'))
print(os.path.getatime('./0.py'))
print(os.path.getmtime('./0.py'))
print(os.path.getctime('./0.py'))
print(os.path.getsize('./0.py'))
print(os.path.isabs('./0.py'))
print(os.path.isfile('./0.py'))
print(os.path.isdir('./0.py'))
print(os.path.islink('./0.py'))
print(os.path.ismount('./0.py'))
print(os.path.join('./0.py'))
print(os.path.normcase('./0.py'))
print(os.path.normpath('./0.py'))
print(os.path.realpath('./0.py'))
print(os.path.relpath('./0.py'))
print(os.path.samefile('./0.py', './0.py'))
#    print(os.path.sameopenfile(os.open('./0.py'), os.open('./0.py')))
#with open('./0.py') as f:
#    print(os.path.sameopenfile(f, f))
#print(os.path.sameopenfile(open('./0.py'), open('./0.py')))
#print(os.path.sameopenfile('./0.py', './0.py'))
#print(os.path.samestat('./0.py'))
print(os.path.split('./0.py'))
print(os.path.splitdrive('./0.py'))
print(os.path.splitext('./0.py'))
#print(os.path.splitunc('./0.py'))#バージョン 3.1 で撤廃: 代わりに splitdrive を使ってください。
print(os.path.supports_unicode_filenames)
```
```sh
$ python 0.py 
/.../pylangstudy/201710/12/00
abc.py
/tmp
/usr/l
/tmp
True
True
./0.py
./0.py
1507766495.9202373
1507766486.5361907
1507766490.2762094
1416
False
True
False
False
False
./0.py
./0.py
0.py
/.../pylangstudy/201710/12/00/0.py
0.py
True
('.', '0.py')
('', './0.py')
('./0', '.py')
False
```
