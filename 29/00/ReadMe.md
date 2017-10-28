# [13.1. zlib — gzip 互換の圧縮](https://docs.python.jp/3/library/zlib.html)

< [13. データ圧縮とアーカイブ](https://docs.python.jp/3/library/archiving.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> このモジュールは、データ圧縮を必要とするアプリケーションが zlib ライブラリを使って圧縮および展開を行えるようにします。zlib ライブラリ自身の Webページは http://www.zlib.net です。Python モジュールと zlib ライブラリの 1.1.3 より前のバージョンには互換性のない部分があることが知られています。1.1.3 にはセキュリティホールが存在するため、1.1.4 以降のバージョンを利用することを推奨します。

> zlib の関数にはたくさんのオプションがあり、場合によっては特定の順番で使わなければなりません。このドキュメントではそれら順番についてすべてを説明しようとはしていません。詳細は公式サイト http://www.zlib.net/manual.html にある zlib のマニュアルを参照してください。

> .gz ファイルの読み書きのためには、 gzip モジュールを参照してください。

> このモジュールで利用可能な例外と関数を以下に示します:

属性|概要
----|----
exception zlib.error|圧縮および展開時のエラーによって送出される例外です。
zlib.adler32(data[, value])|data の Adler-32 チェックサムを計算します (Adler-32 チェックサムは、おおむね CRC32 と同等の信頼性を持ちながら、はるかに高速に計算できます)。結果は、符号のない 32 ビットの整数です。 value が与えられている場合、チェックサム計算の初期値として使われます。与えられていない場合、デフォルト値の 1 が使われます。 value を与えることで、複数の入力を結合したデータ全体にわたり、通しのチェックサムを計算できます。このアルゴリズムは暗号論的には強力ではなく、認証やデジタル署名などに用いるべきではありません。また、チェックサムアルゴリズムとして設計されているため、汎用のハッシュアルゴリズムには向きません。
zlib.compress(data, level=-1)|Compresses the bytes in data, returning a bytes object containing compressed data. level is an integer from 0 to 9 or -1 controlling the level of compression; 1 is fastest and produces the least compression, 9 is slowest and produces the most. 0 is no compression. The default value is -1 (Z_DEFAULT_COMPRESSION). Z_DEFAULT_COMPRESSION represents a default compromise between speed and compression (currently equivalent to level 6). Raises the error exception if any error occurs.(データ内のバイトを圧縮し、圧縮データを含むバイトオブジェクトを返します。 levelは、圧縮レベルを制御する0〜9または-1の整数です。 1は最も速く最も圧縮率が低く、9は最も遅く、最も多く発生します。 0は圧縮なしです。 デフォルト値は-1（Z_DEFAULT_COMPRESSION）です。 Z_DEFAULT_COMPRESSIONは、速度と圧縮の間のデフォルトの妥協点を表します（現在、レベル6と同等です）。 エラーが発生した場合にエラー例外を発生させます。)
zlib.compressobj(level=-1, method=DEFLATED, wbits=15, memLevel=8, strategy=Z_DEFAULT_STRATEGY[, zdict])|一度にメモリ上に置くことができないようなデータストリームを圧縮するための圧縮オブジェクトを返します。level は圧縮レベルです。0 から 9 、または -1 の整数を取り、1 は最も高速で最小限の圧縮を行い、9 は最も低速で最大限の圧縮を行います。0 は圧縮しません。デフォルトは -1 です (Z_DEFAULT_COMPRESSION)。Z_DEFAULT_COMPRESSION は、速度と圧縮の間のデフォルトの妥協点 (現在、レベル 6 に対応します) を表します。
zlib.crc32(data[, value])|data の CRC (Cyclic Redundancy Check, 巡回冗長検査) チェックサムを計算します。結果は、符号のない 32 ビットの整数です。 value が与えられている場合、チェックサム計算の初期値として使われます。与えられていない場合、デフォルト値の 1 が使われます。 value を与えることで、複数の入力を結合したデータ全体にわたり、通しのチェックサムを計算できます。このアルゴリズムは暗号論的には強力ではなく、認証やデジタル署名などに用いるべきではありません。また、チェックサムアルゴリズムとして設計されているため、汎用のハッシュアルゴリズムには向きません。
zlib.decompress(data, wbits=MAX_WBITS, bufsize=DEF_BUF_SIZE)|Decompresses the bytes in data, returning a bytes object containing the uncompressed data. The wbits parameter depends on the format of data, and is discussed further below. If bufsize is given, it is used as the initial size of the output buffer. Raises the error exception if any error occurs.
zlib.decompressobj(wbits=15[, zdict])|一度にメモリ上に置くことができないようなデータストリームを展開するための展開オブジェクトを返します。
Compress.compress(data)|data を圧縮し、圧縮されたデータを含むバイト列オブジェクトを返します。この文字列は少なくとも data の一部分のデータに対する圧縮データを含みます。このデータは以前に呼んだ compress() が返した出力と結合することができます。入力の一部は以後の処理のために内部バッファに保存されることもあります。
Compress.flush([mode])|未処理の全入力データが処理され、この未処理部分を圧縮したデータを含むバイト列オブジェクトが返されます。mode は定数 Z_SYNC_FLUSH、Z_FULL_FLUSH、または Z_FINISH のいずれかをとり、デフォルト値は Z_FINISH です。Z_SYNC_FLUSH および Z_FULL_FLUSH はこれ以後にもデータバイト文字列を圧縮できるモードです。一方、Z_FINISH は圧縮ストリームを閉じ、これ以後のデータの圧縮を停止します。mode に Z_FINISH を指定して flush() メソッドを呼び出した後は、compress() メソッドを再び呼ぶべきではありません。唯一の現実的な操作はこのオブジェクトを削除することだけです。
Compress.copy()|圧縮オブジェクトのコピーを返します。これを使うと先頭部分が共通している複数のデータを効率的に圧縮することができます。

> 展開オブジェクトは以下のメソッドと属性をサポートしています:

属性|概要
----|----
Decompress.unused_data|圧縮データの末尾より後のバイト列が入ったバイト列オブジェクトです。すなわち、この値は圧縮データの入っているバイト列の最後の文字が利用可能になるまでは b"" のままとなります。入力バイト文字列すべてが圧縮データを含んでいた場合、この属性は b"" 、すなわち空バイト列になります。
Decompress.unconsumed_tail|展開されたデータを収めるバッファの長さ制限を超えたために、直近の decompress() 呼び出しで処理しきれなかったデータを含むバイト列オブジェクトです。このデータはまだ zlib 側からは見えていないので、正しい展開出力を得るには以降の decompress() メソッド呼び出しに (場合によっては後続のデータが追加された) データを差し戻さなければなりません。
Decompress.eof|圧縮データストリームの終了に達したかどうかを示すブール値です。
Decompress.decompress(data, max_length=0)|data を展開し、少なくとも string の一部分に対応する展開されたデータを含むバイト列オブジェクトを返します。このデータは以前に decompress() メソッドを呼んだ時に返された出力と結合することができます。入力データの一部分が以後の処理のために内部バッファに保存されることもあります。
Decompress.flush([length])|未処理の入力データをすべて処理し、最終的に圧縮されなかった残りの出力バイト列オブジェクトを返します。flush() を呼んだ後、decompress() を再度呼ぶべきではありません。このときできる唯一の現実的な操作はオブジェクトの削除だけです。
Decompress.copy()|展開オブジェクトのコピーを返します。これを使うとデータストリームの途中にある展開オブジェクトの状態を保存でき、未来のある時点で行なわれるストリームのランダムなシークをスピードアップするのに利用できます。
zlib.ZLIB_VERSION|モジュールのビルド時に使用された zlib ライブラリのバージョン文字列です。これは ZLIB_RUNTIME_VERSION で確認できる、実行時に使用している実際の zlib ライブラリのバージョンとは異なる場合があります。
zlib.ZLIB_RUNTIME_VERSION|インタプリタが読み込んだ実際の zlib ライブラリのバージョン文字列です。


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

