# [11.3. fileinput — 複数の入力ストリームをまたいだ行の繰り返し処理をサポートする](https://docs.python.jp/3/library/fileinput.html)

< [11. ファイルとディレクトリへのアクセス](https://docs.python.jp/3/library/filesys.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/fileinput.py](https://github.com/python/cpython/tree/3.6/Lib/fileinput.py)

> このモジュールは標準入力やファイルの並びにまたがるループを素早く書くためのヘルパークラスと関数を提供しています。単一のファイルを読み書きしたいだけなら、 open() を参照してください。

> 典型的な使い方は以下の通りです:

```python
import fileinput
for line in fileinput.input():
    process(line)
```

> このプログラムは sys.argv[1:] に含まれる全てのファイルをまたいで繰り返します。もし該当するものがなければ、 sys.stdin がデフォルトとして扱われます。ファイル名として '-' が与えられた場合も、 sys.stdin に置き換えられます。別のファイル名リストを使いたい時には、 input() の最初の引数にリストを与えます。単一ファイル名の文字列も受け付けます。

> 全てのファイルはデフォルトでテキストモードでオープンされます。しかし、 input() や FileInput をコールする際に mode パラメータを指定すれば、これをオーバーライドすることができます。オープン中あるいは読み込み中にI/Oエラーが発生した場合には、 OSError が発生します。

> バージョン 3.3 で変更: 以前は IOError が送出されました; それは現在 OSError のエイリアスです。

> sys.stdin が2回以上使われた場合は、2回目以降は行を返しません。ただしインタラクティブに利用している時や明示的にリセット (sys.stdin.seek(0) を使う) を行った場合はその限りではありません。

> 空のファイルは開いた後すぐ閉じられます。空のファイルはファイル名リストの最後にある場合にしか外部に影響を与えません。

> ファイルの各行は、各種改行文字まで含めて返されます。ファイルの最後が改行文字で終っていない場合には、改行文字で終わらない行が返されます。

> ファイルのオープン方法を制御するためのオープン時フックは、 fileinput.input() あるいは FileInput() の openhook パラメータで設定します。このフックは、ふたつの引数 filename と mode をとる関数でなければなりません。そしてその関数の返り値はオープンしたファイルオブジェクトとなります。このモジュールには、便利なフックが既に用意されています。

> 以下の関数がこのモジュールの基本的なインタフェースです:

メソッド|説明
--------|----
fileinput.input(files=None, inplace=False, backup='', bufsize=0, mode='r', openhook=None)|FileInput クラスのインスタンスを作ります。生成されたインスタンスは、このモジュールの関数群が利用するグローバルな状態として利用されます。この関数への引数は FileInput クラスのコンストラクタへ渡されます。
fileinput.filename()|現在読み込み中のファイル名を返します。一行目が読み込まれる前は None を返します。
fileinput.fileno()|現在のファイルの “ファイル記述子” を整数値で返します。ファイルがオープンされていない場合 (最初の行の前、ファイルとファイルの間) は -1 を返します。
fileinput.lineno()|最後に読み込まれた行の、累積した行番号を返します。1行目が読み込まれる前は 0 を返します。最後のファイルの最終行が読み込まれた後には、その行の行番号を返します。
fileinput.filelineno()|現在のファイル中での行番号を返します。1行目が読み込まれる前は 0 を返します。最後のファイルの最終行が読み込まれた後には、その行のファイル中での行番号を返します。
fileinput.isfirstline()|最後に読み込まれた行がファイルの 1 行目なら True、そうでなければ False を返します。
fileinput.isstdin()|最後に読み込まれた行が sys.stdin から読まれていれば True、そうでなければFalseを返します。
fileinput.nextfile()|現在のファイルを閉じます。次の繰り返しでは(存在すれば)次のファイルの最初の行が読み込まれます。閉じたファイルの読み込まれなかった行は、累積の行数にカウントされません。ファイル名は次のファイルの最初の行が読み込まれるまで変更されません。最初の行の読み込みが行われるまでは、この関数は呼び出されても何もしませんので、最初のファイルをスキップするために利用することはできません。最後のファイルの最終行が読み込まれた後にも、この関数は呼び出されても何もしません。
fileinput.close()|シーケンスを閉じます。
class fileinput.FileInput(files=None, inplace=False, backup='', bufsize=0, mode='r', openhook=None)|FileInput クラスはモジュールの関数に対応するメソッド filename() 、 fileno() 、 lineno() 、 filelineno() 、 isfirstline() 、 isstdin() 、 nextfile() および close() を実装しています。それに加えて、次の入力行を返す readline() メソッドと、シーケンスの振舞いの実装をしている __getitem__() メソッドがあります。シーケンスはシーケンシャルに読み込むことしかできません。つまりランダムアクセスと readline() を混在させることはできません。

このモジュールには、次のふたつのオープン時フックが用意されています:

メソッド|説明
--------|----
fileinput.hook_compressed(filename, mode)|gzip や bzip2 で圧縮された (拡張子が '.gz' や '.bz2' の) ファイルを、 gzip モジュールや bz2 モジュールを使って透過的にオープンします。ファイルの拡張子が '.gz' や '.bz2' でない場合は、通常通りファイルをオープンします (つまり、 open() をコールする際に伸長を行いません)。
fileinput.hook_encoded(encoding, errors=None)|指定されたエンコーディングとエラーを使ってファイルを読み込むためにopen（）で各ファイルを開くフックを返します。(Returns a hook which opens each file with open(), using the given encoding and errors to read the file.)

