# [12.1. pickle — Python オブジェクトの直列化](https://docs.python.jp/3/library/pickle.html)

< [12. データの永続化](https://docs.python.jp/3/library/persistence.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/pickle.py](https://github.com/python/cpython/tree/3.6/Lib/pickle.py)

> pickle モジュールは Python オブジェクトの直列化および直列化されたオブジェクトの復元のためのバイナリプロトコルを実装しています。"Pickle 化" は Python オブジェクト階層をバイトストリームに変換する処理、"非 pickle 化" は (バイナリファイル または バイトライクオブジェクト から) バイトストリームをオブジェクト階層に復元する処理を意味します。pickle 化 (および非 pickle 化) は "直列化 (serialization)"、"整列化 (marshalling)"、あるいは [1] "平坦化 (flattening)" とも呼ばれますが、混乱を避けるため、ここでは "Pickle 化"、"非 pickle 化" で統一します。

C#でいうシリアライズ、デシリアライズのこと。

> 警告

> pickle モジュールはエラーや不正に生成されたデータに対して安全ではありません。信頼できない、あるいは認証されていないソースから受け取ったデータを非 pickle 化してはいけません。

## [12.1.1. 他の Python モジュールとの関係](https://docs.python.jp/3/library/pickle.html#relationship-to-other-python-modules)

### [12.1.1.1. marshal との比較](https://docs.python.jp/3/library/pickle.html#comparison-with-marshal)

> Python には marshal と呼ばれるより原始的な直列化モジュールがありますが、一般的に Python オブジェクトを直列化する方法としては pickle を選ぶべきです。 marshal は基本的に .pyc ファイルをサポートするために存在しています。

> pickle モジュールはいくつかの点で marshal と明確に異なります:

>     pickle モジュールでは、同じオブジェクトが再度直列化されることのないよう、すでに直列化されたオブジェクトについて追跡情報を保持します。 marshal はこれを行いません。

>     この機能は再帰的オブジェクトと共有オブジェクトの両方に重要な関わりをもっています。再帰的オブジェクトとは自分自身に対する参照を持っているオブジェクトです。再帰的オブジェクトは marshal で扱うことができず、実際、再帰的オブジェクトを marshal 化しようとすると Python インタプリタをクラッシュさせてしまいます。共有オブジェクトは、直列化しようとするオブジェクト階層の異なる複数の場所で同じオブジェクトに対する参照が存在する場合に生じます。共有オブジェクトを共有のままにしておくことは、変更可能なオブジェクトの場合には非常に重要です。

>     marshal はユーザ定義クラスやそのインスタンスを直列化するために使うことができません。 pickle はクラスインスタンスを透過的に保存したり復元したりすることができますが、クラス定義をインポートすることが可能で、かつオブジェクトが保存された際と同じモジュールで定義されていなければなりません。

>     marshal の直列化フォーマットは Python の異なるバージョンで可搬性があることを保証していません。 marshal の本来の仕事は .pyc ファイルのサポートなので、Python を実装する人々には、必要に応じて直列化フォーマットを以前のバージョンと互換性のないものに変更する権限が残されています。 pickle 直列化フォーマットには、全ての Python リリース間で以前のバージョンとの互換性が保証されています。

モジュール|概要
----------|----
pickle|classインスタンスの永続化
marshal|.pycファイルサポート

### [12.1.1.2. json との比較](https://docs.python.jp/3/library/pickle.html#comparison-with-json)

> pickle プロトコルと JSON (JavaScript Object Notation) との基本的な違いは以下のとおりです:

>     JSON はテキストの直列化フォーマット (大抵の場合 utf-8 にエンコードされますが、その出力は Unicode 文字列です) で、pickle はバイナリの直列化フォーマットです;

>     JSON は人間が読める形式ですが、pickle はそうではありません;

>     JSON は相互運用可能で Python 以外でも広く使用されていますが、pickle は Python 固有です;

>     JSON は、デフォルトでは Python の組み込み型の一部しか表現することができず、カスタムクラスに対しても行えません; pickle は極めて多くの Python 組み込み型を表現できます (その多くは賢い Python 内省機構によって自動的に行われます; 複雑なケースでは 固有のオブジェクト API によって対応できます)。

> 参考

> json モジュール: JSON への直列化および復元を行うための標準ライブラリモジュール。 

形式|データ|汎用性
----|------|------
pickle|binary|Python固有
json|text|汎用

## [12.1.2. データストリームの形式](https://docs.python.jp/3/library/pickle.html#data-stream-format)

> pickle によって使用されるデータフォーマットは Python 固有です。これは、JSON や XDR のような外部標準によって (例えばポインター共有を表わすことができないといったような) 制限を受けることがないという利点があります; ただし、これは非 Python プログラムが pickle された Python オブジェクトを再構成することができないということも意味します。

> デフォルトでは、pickle データフォーマットは比較的コンパクトなバイナリ表現を使用します。サイズの抑制目的の最適化が必要なら、pickel されたデータを効率的に 圧縮する ことができます。

> pickletools モジュールには pickle によって生成されたデータストリームを解析するためのツールが含まれます。pickletools のソースコードには、pickle プロトコルで使用される命令コードに関する詳細なコメントがあります。

> 現在 pickle 化には 5 種類のプロトコルを使用できます。より高いプロトコルを使用するほど、作成された pickle を読み込むためにより高い Python のバージョンが必要になります。

>     プロトコルバージョン 0 はオリジナルの「人間に判読可能な」プロトコルで、Python の初期のバージョンとの後方互換性を持ちます。

>     プロトコルバージョン 1 は旧形式のバイナリフォーマットで、これも Python の初期バージョンと互換性があります。

>     プロトコルバージョン 2 は Python 2.3 で導入されました。このバージョンでは 新方式のクラス のより効率的な pickle 化を提供しました。プロトコル 2 による改良に関する情報は PEP 307 を参照してください。

>     プロトコルバージョン 3 は Python 3.0 で追加されました。このバージョンで bytes オブジェクトをサポートしました。これは Python 2.x では非 pickle 化できません。これはデフォルトのプロトコルで、他の Python 3 バージョンとの互換性が求められる場合の推奨プロトコルです。

>     プロトコルバージョン 4 は Python 3.4 で追加されました。このバージョンでは巨大なオブジェクトのサポート、より多くの種類のオブジェクトの pickle 化、および一部のデータ形式の最適化が行われました。プロトコル 4 による改良に関する情報は PEP 3154 を参照してください。

> 注釈

> 直列化は永続性より原始的な概念です。 pickle はファイルオブジェクトの読み書きを行いますが、永続オブジェクトの命名に関する問題にも、(さらに困難な) 永続オブジェクトへの並列アクセスに関する問題にも対応しません。pickle モジュールは複雑なオブジェクトをバイトストリームに変換し、バイトストリームから同じ内部構造のオブジェクトに復元することができます。これらのバイトストリームはファイルに出力されることが多いでしょうが、ネットワークを介して送信したり、データベースに格納することもありえます。shelve モジュールは、オブジェクトを DBM 方式のデータベースファイル上で pickle 化および非 pickle 化するシンプルなインターフェイスを提供します。

pickle ver|python ver
----------|----------
0|初期
1|初期
2|2.3
3|3.0
4|3.4

あまりにもバージョン差が多すぎる。pickleはPython限定だけでなく、Pythonバージョンをも限定する。かなり限られた条件下でしか使えない……。

## [12.1.3. モジュールインタフェース]()

> オブジェクト階層を直列化するには、dumps() 関数を呼ぶだけです。同様に、データストリームを復元するには、loads() 関数を呼びます。しかし、直列化および復元に対してより多くのコントロールを行いたい場合、それぞれ Pickler または Unpickler オブジェクトを作成することができます。

> pickle モジュールは以下の定数を提供しています:

定数|概要
----|----
pickle.HIGHEST_PROTOCOL|利用可能なうち最も高い プロトコルバージョン (整数)。この値は protocol 値として関数 dump() および dumps() と、Pickler コンストラクターに渡すことができます。
pickle.DEFAULT_PROTOCOL|pickle 化で使用されるデフォルトの プロトコルバージョン (整数)。HIGHEST_PROTOCOL より低い値になる場合があります。現在のデフォルトプロトコルは Python 3 用に設計された 3 です。

> この pickle 化の手続きを便利にするために、 pickle モジュールでは以下の関数を提供しています:

関数|概要
----|----
pickle.dump(obj, file, protocol=None, *, fix_imports=True)|obj を pickle 化し、すでにオープンしている ファイルオブジェクト file に書き込みます。Pickler(file, protocol).dump(obj) と等価です。
pickle.dumps(obj, protocol=None, *, fix_imports=True)|ファイルに書く代わりに、bytes オブジェクトとしてオブジェクトの pickle 表現を返します。
pickle.loads(bytes_object, *, fix_imports=True, encoding="ASCII", errors="strict")|bytes オブジェクトから pickle 化されたオブジェクト階層を読み込んで、その中で指定されたオブジェクト階層に再構成して返します。

> pickle モジュールでは 3 つの例外を定義しています:

例外|概要
----|----
exception pickle.PickleError|他の pickle 化例外の共通基底クラス。Exception を継承しています。
exception pickle.PicklingError|Pickler が pickle 化不可能なオブジェクトに遭遇したときに送出されるエラー。PickleError を継承しています。
exception pickle.UnpicklingError|データ破損やセキュリティ違反のような、オブジェクトを非 pickle 化するのに問題がある場合に送出されるエラー。PickleError を継承します。

> pickle モジュールでは、2 つのクラス Pickler および Unpickler を提供しています:

属性|概要
----|----
class pickle.Pickler(file, protocol=None, *, fix_imports=True)|pickle 化されたオブジェクトのデータストリームを書き込むためのバイナリファイルを引数にとります。
    dump(obj)|    obj の pickle 化表現を、コンストラクターで与えられた、すでにオープンしているファイルオブジェクトに書き込みます。
    persistent_id(obj)|    デフォルトでは何もしません。このメソッドはサブクラスがオーバーライドできるように存在します。
    dispatch_table|    pickler オブジェクトのディスパッチテーブルは copyreg.pickle() を使用して宣言できる種類の reduction functions のレジストリです。これはキーがクラスでその値が減少関数のマッピング型オブジェクトです。減少関数は関連するクラスの引数を 1 個とり、__reduce__() メソッドと同じインタフェースでなければなりません。
    fast|    廃止予定です。真値が設定されれば高速モードを有効にします。高速モードは、メモの使用を無効にします。それにより余分な PUT 命令コードを生成しなくなるので pickle 化処理が高速化します。自己参照オブジェクトに対しては使用すべきではありません。さもなければ Pickler に無限再帰を起こさせるでしょう。

属性|概要
----|----
class pickle.Unpickler(file, *, fix_imports=True, encoding="ASCII", errors="strict")|これは pickle データストリームの読み込みのためにバイナリファイルをとります。
    load()|    コンストラクターで与えられたオープンしたファイルオブジェクトから pickle 化オブジェクト表現を読み込み、その中で指定されたオブジェクト階層に再構成して返します。pickle 化オブジェクト表現より後のバイト列は無視されます。
    persistent_load(pid)|    デフォルトで UnpicklingError を送出します。
    find_class(module, name)|    必要なら module をインポートして、そこから name という名前のオブジェクトを返します。ここで module および name 引数は str オブジェクトです。その名前が示唆することに反して find_class() は関数を探すためにも使われることに注意してください。

```python
import pickle
print('pickle.HIGHEST_PROTOCOL:', pickle.HIGHEST_PROTOCOL)
print('pickle.DEFAULT_PROTOCOL:', pickle.DEFAULT_PROTOCOL)

class Human:
    class_var = 0
    def __init__(self):
        self.ins_var = 1
    def ins_method(self):
        print('ins_method')

with open('Human.pickle', 'wb') as f:
    pickle.dump(Human(), f, protocol=4)
print(pickle.dumps(Human(), protocol=4))

with open('Human.pickle', 'rb') as f:
    ins = pickle.load(f, encoding='UTF-8')
    print(ins)
    print(dir(ins))
    print(ins.class_var)
    print(ins.ins_var)
    ins.ins_method()
#    print(pickle.loads(f.read(), encoding='UTF-8'))#EOFError: Ran out of input

with open('Human.pickler', 'wb') as f:
    p = pickle.Pickler(f, protocol=4)
    h = Human()
    p.dump(h)
#    print(p.persistent_id(h))#AttributeError: persistent_id
#    print(p.dispatch_table)#AttributeError: dispatch_table
#    print(pickle.Pickler.persistent_id(h))#TypeError: 'getset_descriptor' object is not callable
    print(pickle.Pickler.dispatch_table)
with open('Human.pickler', 'rb') as f:
    p = pickle.Unpickler(f, encoding='UTF-8')
    ins = p.load()
    print(ins)
#    print(dir(ins))
    print(ins.class_var)
    print(ins.ins_var)
    ins.ins_method()
    #p.persistent_load(pid)
    #p.find_class(module, name)
```
```sh
$ python 0.py 
pickle.HIGHEST_PROTOCOL: 4
pickle.DEFAULT_PROTOCOL: 3
b'\x80\x04\x95)\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x05Human\x94\x93\x94)\x81\x94}\x94\x8c\x07ins_var\x94K\x01sb.'
<__main__.Human object at 0xb70b890c>
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slotnames__', '__str__', '__subclasshook__', '__weakref__', 'class_var', 'ins_method', 'ins_var']
0
1
ins_method
<member 'dispatch_table' of '_pickle.Pickler' objects>
<__main__.Human object at 0xb70c3e6c>
0
1
ins_method
```

