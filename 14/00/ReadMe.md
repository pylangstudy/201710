# [11.4. stat — stat() の結果を解釈する](https://docs.python.jp/3/library/stat.html)

< [11. ファイルとディレクトリへのアクセス](https://docs.python.jp/3/library/filesys.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/stat.py](https://github.com/python/cpython/tree/3.6/Lib/stat.py)

stat モジュールでは、 os.stat() 、 os.lstat() 、および os.fstat() が存在する場合に、これらの関数が返す内容を解釈するための定数や関数を定義しています。 stat() 、 fstat() 、および lstat() の関数呼び出しについての完全な記述はシステムのドキュメントを参照してください。

バージョン 3.4 で変更: stat モジュールは、C 実装に裏付けされるようになりました。

stat モジュールでは、特殊なファイル型を判別するための以下の関数を定義しています:

> stat モジュールでは、 os.stat() 、 os.lstat() 、および os.fstat() が存在する場合に、これらの関数が返す内容を解釈するための定数や関数を定義しています。 stat() 、 fstat() 、および lstat() の関数呼び出しについての完全な記述はシステムのドキュメントを参照してください。

> バージョン 3.4 で変更: stat モジュールは、C 実装に裏付けされるようになりました。

> stat モジュールでは、特殊なファイル型を判別するための以下の関数を定義しています:

属性|説明
----|----
stat.S_ISDIR(mode)|ファイルのモードがディレクトリの場合にゼロでない値を返します。
stat.S_ISCHR(mode)|ファイルのモードがキャラクタ型の特殊デバイスファイルの場合にゼロでない値を返します。
stat.S_ISBLK(mode)|ファイルのモードがブロック型の特殊デバイスファイルの場合にゼロでない値を返します。
stat.S_ISREG(mode)|ファイルのモードが通常ファイルの場合にゼロでない値を返します。
stat.S_ISFIFO(mode)|ファイルのモードが FIFO (名前つきパイプ) の場合にゼロでない値を返します。
stat.S_ISLNK(mode)|ファイルのモードがシンボリックリンクの場合にゼロでない値を返します。
stat.S_ISSOCK(mode)|ファイルのモードがソケットの場合にゼロでない値を返します。
stat.S_ISDOOR(mode)|ファイルのモードがドアの場合にゼロでない値を返します。
stat.S_ISPORT(mode)|ファイルのモードがイベントポートの場合にゼロでない値を返します。
stat.S_ISWHT(mode)|ファイルのモードがホワイトアウトの場合にゼロでない値を返します。
stat.S_IMODE(mode)|os.chmod() で設定することのできる一部のファイルモード — すなわち、ファイルの許可ビット (permission bits) に加え、 (サポートされているシステムでは) スティッキービット (sticky bit)、実行グループ ID 設定 (set-group-id) および実行ユーザ ID 設定 (set-user-id) ビット — を返します。
stat.S_IFMT(mode)|ファイルの形式を記述しているファイルモードの一部 (上記の S_IS*() 関数で使われます) を返します。
stat.filemode(mode)|ファイルのモードを ‘-rwxrwxrwx’ 形式の文字列に変換します。
stat.ST_MODE|Iノードの保護モード。
stat.ST_INO|Iノード番号。
stat.ST_DEV|Iノードが存在するデバイス。
stat.ST_NLINK|該当する Iノードへのリンク数。
stat.ST_UID|ファイルの所持者のユーザ ID。
stat.ST_GID|ファイルの所持者のグループ ID。
stat.ST_SIZE|通常ファイルではバイトサイズ; いくつかの特殊ファイルでは処理待ちのデータ量。
stat.ST_ATIME|最後にアクセスした時刻。
stat.ST_MTIME|最後に変更された時刻。
stat.ST_CTIME|オペレーティングシステムから返される”ctime”。あるOS(Unixなど)では最後にメタデータが更新された時間となり、別のOS(Windowsなど)では作成時間となります(詳細については各プラットフォームのドキュメントを参照してください)。
stat.S_IFSOCK|ソケット。
stat.S_IFLNK|シンボリックリンク。
stat.S_IFREG|通常のファイル。
stat.S_IFBLK|ブロックデバイス。
stat.S_IFDIR|ディレクトリ。
stat.S_IFCHR|キャラクターデバイス。
stat.S_IFIFO|FIFO。
stat.S_IFDOOR|ドア。
stat.S_IFPORT|イベントポート。
stat.S_IFWHT|ホワイトアウト。
stat.S_ISUID|UID ビットを設定する。
stat.S_ISGID|グループIDビットを設定する。
stat.S_ISVTX|スティッキービット。
stat.S_IRWXU|ファイルオーナーの権限に対するマスク。
stat.S_IRUSR|オーナーがリード権限を持っている。
stat.S_IWUSR|オーナーがライト権限を持っている。
stat.S_IXUSR|オーナーが実行権限を持っている。
stat.S_IRWXG|グループの権限に対するマスク。
stat.S_IRGRP|グループがリード権限を持っている。
stat.S_IWGRP|グループがライト権限を持っている。
stat.S_IXGRP|グループが実行権限を持っている。
stat.S_IRWXO|その他 (グループ外) の権限に対するマスク。
stat.S_IROTH|その他はリード権限を持っている。
stat.S_IWOTH|その他はライト権限を持っている。
stat.S_IXOTH|その他は実行権限を持っている。
stat.S_ENFMT|System V ファイルロック強制。
stat.S_IREAD|S_IRUSR の、 Unix V7 のシノニム。
stat.S_IWRITE|S_IWUSR の、 Unix V7 のシノニム。
stat.S_IEXEC|S_IXUSR の、 Unix V7 のシノニム。
stat.UF_NODUMP|ファイルをダンプしない。
stat.UF_IMMUTABLE|ファイルは変更されない。
stat.UF_APPEND|ファイルは追記しかされない。
stat.UF_OPAQUE|ユニオンファイルシステムのスタックを通したとき、このディレクトリは不透明です。
stat.UF_NOUNLINK|ファイルはリネームや削除されない。
stat.UF_COMPRESSED|ファイルは圧縮して保存される (Mac OS X 10.6+)。
stat.UF_HIDDEN|ファイルは GUI で表示されるべきでない (Mac OS X 10.5+)。
stat.SF_ARCHIVED|ファイルはアーカイブされているかもしれません。
stat.SF_IMMUTABLE|ファイルは変更されない。
stat.SF_APPEND|ファイルは追記しかされない。
stat.SF_NOUNLINK|ファイルはリネームや削除されない。
stat.SF_SNAPSHOT|このファイルはスナップショットファイルです。

* stat.FILE_ATTRIBUTE_ARCHIVE
* stat.FILE_ATTRIBUTE_COMPRESSED
* stat.FILE_ATTRIBUTE_DEVICE
* stat.FILE_ATTRIBUTE_DIRECTORY
* stat.FILE_ATTRIBUTE_ENCRYPTED
* stat.FILE_ATTRIBUTE_HIDDEN
* stat.FILE_ATTRIBUTE_INTEGRITY_STREAM
* stat.FILE_ATTRIBUTE_NORMAL
* stat.FILE_ATTRIBUTE_NOT_CONTENT_INDEXED
* stat.FILE_ATTRIBUTE_NO_SCRUB_DATA
* stat.FILE_ATTRIBUTE_OFFLINE
* stat.FILE_ATTRIBUTE_READONLY
* stat.FILE_ATTRIBUTE_REPARSE_POINT
* stat.FILE_ATTRIBUTE_SPARSE_FILE
* stat.FILE_ATTRIBUTE_SYSTEM
* stat.FILE_ATTRIBUTE_TEMPORARY
* stat.FILE_ATTRIBUTE_VIRTUAL

```python
import os
import stat
s = os.stat('0.py')
print(s)
print(stat.S_ISDIR(s.st_mode))
print(stat.S_ISCHR(s.st_mode))
print(stat.S_ISBLK(s.st_mode))
print(stat.S_ISREG(s.st_mode))
print(stat.S_ISFIFO(s.st_mode))
print(stat.S_ISLNK(s.st_mode))
print(stat.S_ISSOCK(s.st_mode))
print(stat.S_ISDOOR(s.st_mode))
print(stat.S_ISPORT(s.st_mode))
print(stat.S_ISWHT(s.st_mode))
print(stat.S_IMODE(s.st_mode))
print(stat.S_IFMT(s.st_mode))
print(stat.filemode(s.st_mode))
print(stat.ST_MODE)
print(stat.ST_INO)
print(stat.ST_DEV)
print(stat.ST_NLINK)
print(stat.ST_UID)
print(stat.ST_GID)
print(stat.ST_SIZE)
print(stat.ST_ATIME)
print(stat.ST_MTIME)
print(stat.ST_CTIME)
print(stat.S_IFSOCK)
print(stat.S_IFLNK)
print(stat.S_IFREG)
print(stat.S_IFBLK)
print(stat.S_IFDIR)
print(stat.S_IFCHR)
print(stat.S_IFIFO)
print(stat.S_IFDOOR)
print(stat.S_IFPORT)
print(stat.S_IFWHT)
print(stat.S_ISUID)
print(stat.S_ISGID)
print(stat.S_ISVTX)
print(stat.S_IRWXU)
print(stat.S_IRUSR)
print(stat.S_IWUSR)
print(stat.S_IXUSR)
print(stat.S_IRWXG)
print(stat.S_IRGRP)
print(stat.S_IWGRP)
print(stat.S_IXGRP)
print(stat.S_IRWXO)
print(stat.S_IROTH)
print(stat.S_IWOTH)
print(stat.S_IXOTH)
print(stat.S_ENFMT)
print(stat.S_IREAD)
print(stat.S_IWRITE)
print(stat.S_IEXEC)
print(stat.UF_NODUMP)
print(stat.UF_IMMUTABLE)
print(stat.UF_APPEND)
print(stat.UF_OPAQUE)
print(stat.UF_NOUNLINK)
print(stat.UF_COMPRESSED)
print(stat.UF_HIDDEN)
print(stat.SF_ARCHIVED)
print(stat.SF_IMMUTABLE)
print(stat.SF_APPEND)
print(stat.SF_NOUNLINK)
print(stat.SF_SNAPSHOT)
print(stat.FILE_ATTRIBUTE_ARCHIVE)
print(stat.FILE_ATTRIBUTE_COMPRESSED)
print(stat.FILE_ATTRIBUTE_DEVICE)
print(stat.FILE_ATTRIBUTE_DIRECTORY)
print(stat.FILE_ATTRIBUTE_ENCRYPTED)
print(stat.FILE_ATTRIBUTE_HIDDEN)
print(stat.FILE_ATTRIBUTE_INTEGRITY_STREAM)
print(stat.FILE_ATTRIBUTE_NORMAL)
print(stat.FILE_ATTRIBUTE_NOT_CONTENT_INDEXED)
print(stat.FILE_ATTRIBUTE_NO_SCRUB_DATA)
print(stat.FILE_ATTRIBUTE_OFFLINE)
print(stat.FILE_ATTRIBUTE_READONLY)
print(stat.FILE_ATTRIBUTE_REPARSE_POINT)
print(stat.FILE_ATTRIBUTE_SPARSE_FILE)
print(stat.FILE_ATTRIBUTE_SYSTEM)
print(stat.FILE_ATTRIBUTE_TEMPORARY)
print(stat.FILE_ATTRIBUTE_VIRTUAL)
```
```sh
$ python 0.py 
os.stat_result(st_mode=33188, st_ino=28443562, st_dev=2085, st_nlink=1, st_uid=1000, st_gid=1000, st_size=2162, st_atime=1507939974, st_mtime=1507939972, st_ctime=1507939972)
False
False
False
True
False
False
False
False
False
False
420
32768
-rw-r--r--
0
1
2
3
4
5
6
7
8
9
49152
40960
32768
24576
16384
8192
4096
0
0
0
2048
1024
512
448
256
128
64
56
32
16
8
7
4
2
1
1024
256
128
64
1
2
4
8
16
32
32768
65536
131072
262144
1048576
2097152
32
2048
64
16
16384
2
32768
128
8192
131072
4096
1
1024
512
4
256
65536
```
