# [13.3. bz2 — bzip2 圧縮のサポート](https://docs.python.jp/3/library/bz2.html)

< [13. データ圧縮とアーカイブ](https://docs.python.jp/3/library/archiving.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/bz2.py](https://github.com/python/cpython/tree/3.6/Lib/bz2.py)

> このモジュールは、bzip2 アルゴリズムを用いて圧縮・展開を行う包括的なインターフェイスを提供します。

> bz2 モジュールには以下のクラスや関数があります:

* 圧縮ファイルを読み書きするための open() 関数と BZ2File クラス。
* インクリメンタルにデータを圧縮・展開するための BZ2Compressor および BZ2Decompressor クラス。
* 一度に圧縮・展開を行う compress() および decompress() 関数。

> このモジュールのクラスはすべて、複数のスレッドから安全にアクセスできます。

## [13.3.1. ファイルの圧縮/解凍](https://docs.python.jp/3/library/bz2.html#de-compression-of-files)

属性|概要
----|----
bz2.open(filename, mode='r', compresslevel=9, encoding=None, errors=None, newline=None)|bzip2 圧縮されたファイルを、バイナリモードかテキストモードでオープンし、ファイルオブジェクト を返します。
class bz2.BZ2File(filename, mode='r', buffering=None, compresslevel=9)|bzip2 圧縮ファイルをバイナリモードでオープンします。
    peek([n])|    ファイル上の現在位置を変更せずにバッファのデータを返します。このメソッドは少なくとも 1 バイトのデータを返します (EOF の場合を除く)。返される正確なバイト数は規定されていません。

## [13.3.2. 逐次圧縮および展開](https://docs.python.jp/3/library/bz2.html#incremental-de-compression)

属性|概要
----|----
class bz2.BZ2Compressor(compresslevel=9)|新しくコンプレッサオブジェクトを作成します。このオブジェクトはデータの逐次的な圧縮に使用できます。一度に圧縮したい場合は、compress() 関数を使ってください。
    compress(data)|    データをコンプレッサオブジェクトに渡します。戻り値は圧縮されたデータですが、圧縮データを返すことができない場合は空のバイト文字列を返します。
    flush()|    圧縮プロセスを完了させ、内部バッファに残っている圧縮済みデータを返します。
class bz2.BZ2Decompressor|新しくデコンプレッサオブジェクトを作成します。このオブジェクトは逐次的なデータ展開に使用できます。一度に展開したい場合は、decompress() 関数を使ってください。
    decompress(data, max_length=-1)|    data (bytes-like object) を展開し、未圧縮のデータを bytes で返します。 data の一部は、後で decompress() の呼び出しに使用するため内部でバッファされている場合があります。 返すデータは以前の decompress() 呼び出しの出力を全て連結したものです。
    eof|    ストリーム終端記号に到達した場合 True を返します。
    unused_data|    圧縮ストリームの末尾以降に存在したデータを表します。
    needs_input|    decompress() メソッドが、新しい非圧縮入力を必要とせずにさらに展開データを提供できる場合、 False です。

## [13.3.3. 一括圧縮/解凍](https://docs.python.jp/3/library/bz2.html#one-shot-de-compression)

属性|概要
----|----
bz2.compress(data, compresslevel=9)|data を圧縮します。
bz2.decompress(data)|data を展開します。

