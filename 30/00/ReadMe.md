# [13.2. gzip — gzip ファイルのサポート](https://docs.python.jp/3/library/gzip.html)

< [13. データ圧縮とアーカイブ](https://docs.python.jp/3/library/archiving.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/gzip.py](https://github.com/python/cpython/tree/3.6/Lib/gzip.py)

> このモジュールは、GNU の gzip や gunzip のようにファイルを圧縮、展開するシンプルなインターフェイスを提供しています。

> データ圧縮は zlib モジュールで提供されています。

> gzip は GzipFile クラスと、簡易関数 open()、compress()、および decompress() を提供しています。GzipFile クラスは通常の ファイルオブジェクト と同様に gzip 形式のファイルを読み書きし、データを自動的に圧縮または展開します。

> compress や pack 等によって作成され、gzip や gunzip が展開できる他のファイル形式についてはこのモジュールは対応していないので注意してください。

> このモジュールは以下の項目を定義しています:

属性|概要
----|----
gzip.open(filename, mode='rb', compresslevel=9, encoding=None, errors=None, newline=None)|gzip 圧縮ファイルをバイナリまたはテキストモードで開き、ファイルオブジェクト を返します。
class gzip.GzipFile(filename=None, mode=None, compresslevel=9, fileobj=None, mtime=None)|GzipFile クラスのコンストラクタです。GzipFile オブジェクトは truncate() メソッドを除くほとんどの ファイルオブジェクト のメソッドをシミュレートします。少なくとも fileobj および filename は有効な値でなければなりません。
    peek(n)|    ファイル内の位置を移動せずに展開した n バイトを読み込みます。呼び出し要求を満たすために、圧縮ストリームに対して最大 1 回の単一読み込みが行われます。返されるバイト数はほぼ要求した値になります。
    mtime|    展開時に、最後に読み取られたヘッダーの最終更新日時フィールドの値は、この属性から整数として読み取ることができます。ヘッダーを読み取る前の初期値は None です。
gzip.compress(data, compresslevel=9)|data を圧縮し、圧縮データを含む bytes オブジェクトを返します。compresslevel の意味は上記 GzipFile コンストラクタと同じです。
gzip.decompress(data)|data を展開し、展開データを含む bytes オブジェクトを返します。

## [13.2.1. 使い方の例](https://docs.python.jp/3/library/gzip.html#examples-of-usage)

> 圧縮されたファイルを読み込む例:

```python
import gzip
with gzip.open('/home/joe/file.txt.gz', 'rb') as f:
    file_content = f.read()
```

GZIP 圧縮されたファイルを作成する例:

```python
import gzip
content = b"Lots of content here"
with gzip.open('/home/joe/file.txt.gz', 'wb') as f:
    f.write(content)
```

既存のファイルを GZIP 圧縮する例:

```python
import gzip
import shutil
with open('/home/joe/file.txt', 'rb') as f_in:
    with gzip.open('/home/joe/file.txt.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
```

バイナリ文字列を GZIP 圧縮する例:

```python
import gzip
s_in = b"Lots of content here"
s_out = gzip.compress(s_in)
```

```python
import gzip
import shutil
with open('0.py', 'rb') as f_in:
    with gzip.open('0.py.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

with gzip.open('0.py.gz', 'rb') as f:
    file_content = f.read()
    print(file_content)
    print(gzip.compress(file_content))
```
```sh
$ python 0.py 
b"import gzip\nimport shutil\nwith open('0.py', 'rb') as f_in:\n    with gzip.open('0.py.gz', 'wb') as f_out:\n        shutil.copyfileobj(f_in, f_out)\n\nwith gzip.open('0.py.gz', 'rb') as f:\n    file_content = f.read()\n    print(file_content)\n    print(gzip.compress(file_content))\n"
b"\x1f\x8b\x08\x00qj\xf6Y\x02\xff}\x8d\xc1\n\x830\x0c\x86\xef}\x8a\xdc\xda\x82\x94\x9d\x07{\x16QW5C\x9b\xd0FD\x9f~\xab\x05\xe7.\xfbO!\xf9\xfe/83E\x81aGVX\xe64.\x82\x93ZQF \xf6\xc1\xe8\x9b\xe3MW\xa0c\xab-4\t\xfa\x1a\xc3]\xc1'\x07\x94\xcb\xeeK\xbaa\xcf\xf0z\xc2\xb4H\xa1s\x8a\xddu\xc4[\x8f\x93\xa7\xf6e\xb2\xae*\x9cU\xea\x8f\xf2\xfc_t\xb9_w\x14\xc4\x07\x81\x07\xf4.\xfa\xe6i\xecq\xe3\x88A\xcc\x95\xb8\xee\x0f}G3G\x9f\xd2/e\xd5\x1b\x1fo\xb4_\x13\x01\x00\x00"
```

### 参考

モジュール|概要
----------|----
[zlib](https://docs.python.jp/3/library/zlib.html#module-zlib)|gzip ファイル形式のサポートを行うために必要な基本ライブラリモジュール。










```python
import zlib

data = b'abc'
print(zlib.adler32(data))
print(zlib.compress(data))
print(zlib.compressobj())
print(zlib.crc32(data))
print(zlib.decompress(zlib.compress(data)))
print(zlib.decompressobj())

c = zlib.compressobj()
print(c.compress(data))
print(c.flush())
#print(c.copy())#ValueError: Inconsistent stream state

d = zlib.decompressobj()
print(d.unused_data)
print(d.unconsumed_tail)
print(d.eof)
print(d.decompress(zlib.compress(data)))
print(d.flush())
#print(d.copy())#ValueError: Inconsistent stream state
print(zlib.ZLIB_VERSION)
print(zlib.ZLIB_RUNTIME_VERSION)
```
```sh
$ python 0.py 
38600999
b"x\x9cKLJ\x06\x00\x02M\x01'"
<zlib.Compress object at 0xb71c5288>
891568578
b'abc'
<zlib.Decompress object at 0xb71c5288>
b'x\x9c'
b"KLJ\x06\x00\x02M\x01'"
b''
b''
False
b'abc'
b''
1.2.8
1.2.8
```

### 参考

モジュール|概要
----------|----
[gzip](https://docs.python.jp/3/library/gzip.html#module-gzip)|gzip 形式ファイルへの読み書きを行うモジュール。
http://www.zlib.net|zlib ライブラリホームページ。
http://www.zlib.net/manual.html|zlib ライブラリの多くの関数の意味と使い方を解説したマニュアル。

