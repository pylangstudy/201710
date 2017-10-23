# [12.1. pickle — Python オブジェクトの直列化](https://docs.python.jp/3/library/pickle.html)

< [12. データの永続化](https://docs.python.jp/3/library/persistence.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/pickle.py](https://github.com/python/cpython/tree/3.6/Lib/pickle.py)

## [12.1.4. pickle 化、非 pickle 化できるもの](https://docs.python.jp/3/library/pickle.html#what-can-be-pickled-and-unpickled)

> 以下の型は pickle 化できます:

* None 、 True 、および False
* 整数、浮動小数点数、複素数
* 文字列、バイト列、バイト配列
* pickle 化可能なオブジェクトからなるタプル、リスト、集合および辞書
* モジュールのトップレベルで定義された関数 (def で定義されたもののみで lambda で定義されたものは含まない)
* モジュールのトップレベルで定義されている組込み関数
* モジュールのトップレベルで定義されているクラス
* __dict__ 属性を持つクラス、あるいは __getstate__() メソッドの返り値が pickle 化可能なクラス (詳細は クラスインスタンスの pickle 化 を参照)。

> pickle 化できないオブジェクトを pickle 化しようとすると、PicklingError 例外が送出されます。この例外が起きたとき、すでに元のファイルには未知の長さのバイト列が書き込まれている場合があります。極端に再帰的なデータ構造を pickle 化しようとした場合には再帰の深さ制限を越えてしまうかもしれず、この場合には RecursionError が送出されます。この制限は、sys.setrecursionlimit() で慎重に上げていくことは可能です。

関数 (組込みおよびユーザー定義) は、値ではなく、"完全修飾" された名前参照で pickle 化されます。[2] これは関数が定義されたモジュールをともにした関数名のみが pickle 化されることを意味します。関数のコードやその属性は pickle 化されません。すなわち、非 pickle 化する環境で定義したモジュールがインポート可能な状態になっており、そのモジュール内に関数名のオブジェクトが含まれていなければなりません。この条件を満たさなかった場合は例外が送出されます。[3]

クラスも同様に名前参照で pickle 化されるので、unpickle 化環境には同じ制限が課せられます。クラス中のコードやデータは何も pickle 化されないので、以下の例ではクラス属性 attr が unpickle 化環境で復元されないことに注意してください

```python
class Foo:
    attr = 'A class attribute'

picklestring = pickle.dumps(Foo)
```

> pickle 化可能な関数やクラスがモジュールのトップレベルで定義されていなければならないのはこれらの制限のためです。

つまり、クラスオブジェクトはpickle化しても属性は復元できない。でも、クラスインスタンスなら復元できる。ということか？

```python
import pickle
class Foo:
    attr = 'A class attribute'

picklestring = pickle.dumps(Foo)
print(picklestring)
picklestring = pickle.dumps(Foo())
print(picklestring)
```
```sh
$ python 0.py 
b'\x80\x03c__main__\nFoo\nq\x00.'
b'\x80\x03c__main__\nFoo\nq\x00)\x81q\x01.'
```

> 同様に、クラスのインスタンスが pickle 化された際、そのクラスのコードおよびデータはオブジェクトと一緒に pickle 化されることはありません。インスタンスのデータのみが pickle 化されます。この仕様は、クラス内のバグを修正したりメソッドを追加した後でも、そのクラスの以前のバージョンで作られたオブジェクトを読み出せるように意図的に行われています。あるクラスの多くのバージョンで使われるような長命なオブジェクトを作ろうと計画しているなら、そのクラスの __setstate__() メソッドによって適切な変換が行われるようにオブジェクトのバージョン番号を入れておくとよいかもしれません。

これは気をつけないとバグになりそう。

## [12.1.5. クラスインスタンスの pickle 化](https://docs.python.jp/3/library/pickle.html#pickling-class-instances)

> この節では、クラスインスタンスがどのように pickle 化または非 pickle 化されるのかを定義したり、カスタマイズしたり、コントロールしたりするのに利用可能な一般的機構について説明します。

> ほとんどの場合、インスタンスを pickle 化できるようにするために追加のコードは必要ありません。デフォルトで、pickle はインスタンスのクラスと属性を内省によって検索します。クラスインスタンスが非 pickle 化される場合、通常その __init__() メソッドは実行 されません 。デフォルトの振る舞いは、最初に初期化されていないインスタンスを作成して、次に保存された属性を復元します。次のコードはこの振る舞いの実装を示しています:

```python
def save(obj):
    return (obj.__class__, obj.__dict__)

def load(cls, attributes):
    obj = cls.__new__(cls)
    obj.__dict__.update(attributes)
    return obj
```

> クラスは、いくつかの特殊メソッドを提供することによって、デフォルトの振る舞いを変更することができます:

属性|説明
----|----
object.__getnewargs_ex__()|In protocols 2 and newer, classes that implements the __getnewargs_ex__() method can dictate the values passed to the __new__() method upon unpickling. The method must return a pair (args, kwargs) where args is a tuple of positional arguments and kwargs a dictionary of named arguments for constructing the object. Those will be passed to the __new__() method upon unpickling.(プロトコル2以降では、__getnewargs_ex __（）メソッドを実装しているクラスが、unpickling時に__new __（）メソッドに渡される値を指定することができます。 メソッドは対（args、kwargs）を返す必要があります。argsは位置引数のタプルであり、kwargsはオブジェクトを構築するための名前付き引数の辞書です。 それらは、unpickling時に__new __（）メソッドに渡されます。)
object.__getnewargs__()|This method serve a similar purpose as __getnewargs_ex__(), but supports only positional arguments. It must return a tuple of arguments args which will be passed to the __new__() method upon unpickling.(このメソッドは、__getnewargs_ex __（）と同様の目的を果たしますが、定位置引数だけをサポートします。 それは、引数なしのときに__new __（）メソッドに渡される引数のタプルを返さなければなりません。)
object.__getstate__()|クラスはそのインスタンスをどう pickle 化するかについてさらに影響を与えることができます; クラスに __getstate__() メソッドが定義されていた場合それが呼ばれ、返り値のオブジェクトはインスタンスの辞書ではなく、インスタンスの内容が pickle 化されたものになります。__getstate__() がないときは通常通りインスタンスの __dict__ が pickle 化されます。
object.__setstate__(state)|非 pickle 化に際して、クラスが __setstate__() を定義している場合、それは非 pickle 化された状態とともに呼び出されます。その場合、状態オブジェクトが辞書でなければならないという要求はありません。そうでなければ、 pickle された状態は辞書で、その要素は新しいインスタンスの辞書に割り当てられます。

> 注釈

> __getstate__() が偽値を返す場合、非 pickle 化時に __setstate__() メソッドは呼ばれません。

> __getstate__() および __setstate__() メソッドの使い方に関する詳細な情報については 状態を持つオブジェクトの扱い 節を参照してください。

> 注釈

> 非 pickle 化時、__getattr__()、__getattribute__() あるいは __setattr__() のような一部のメソッドがインスタンス上で呼び出されることがあります。この場合、これらのメソッドはいくつかの内部不変条件が真であることに依存しており、そのような不変条件を立証するために、データ型には __getnewargs__() または __getnewargs_ex__() が実装されていなければなりません; さもなくば、__new__() も __init__() も呼び出されません。

> これらから見るように、pickle は上記のメソッドを直接使用しません。実際には、これらのメソッドは __reduce__() 特殊メソッドを実装するコピープロトコルの一部です。コピープロトコルは、pickle 化とオブジェクトのコピーに必要な、データを取得するための統一されたインタフェースを提供します。 [4]

> 強力ですが、クラスに __reduce__() メソッドを直接実装することはエラーを起こしやすくなります。この理由のため、クラスの設計者は可能なかぎり高レベルインタフェース (__getnewargs_ex__()、__getstate__() および __setstate__()) を使用するべきです。公開はしているものの、__reduce__() の使用は、あくまでオプションとして、より効果的な pickle 化につながる場合、あるいはその両方の場合のみにしてください。

属性|説明
----|----
object.__reduce__()|このインタフェースは現在、以下のように定義されています。 __reduce__() メソッドは引数を取らず、文字列あるいは (こちらの方が好まれますが) タプルのいずれかを返すべきです (返されたオブジェクトは、しばしば "reduce value" と呼ばれます)。
object.__reduce_ex__(protocol)|別の方法として、__reduce_ex__() メソッドを定義することもできます。唯一の違いは、このメソッドは単一の整数引数、プロトコルバージョンを取る必要があるということです。もし定義された場合、pickle は __reduce__() メソッドよりもこのメソッドを優先します。さらに、__reduce__() は自動的に拡張版の同義語になります。このメソッドの主な用途は、古い Python リリースに対して後方互換性のある reduce value を提供することです。

細かい制御まで実装せねばならないなら、pickle化なんて使いたくない。無視。

### [12.1.5.1. 外部オブジェクトの永続化](https://docs.python.jp/3/library/pickle.html#persistence-of-external-objects)

> オブジェクトの永続化のために、pickle モジュールは、pickle データストリーム外のオブジェクトに対する参照の概念をサポートしています。そのようなオブジェクトは永続的 ID によって参照されます。それは、英数文字の文字列 (プロトコル 0 に対して) [5] あるいは単に任意のオブジェクト (より新しい任意のプロトコルに対して) のいずれかです。

> そのような永続的 ID の分解能は pickle モジュールでは定義されていません; これはこの分解能を pickler および unpickler のそれぞれ persistent_id() および persistent_load() 上でのユーザー定義メソッドに移譲します。

> 外部の永続的 ID を持つ pickle オブジェクトの pickler は、引数にオブジェクトを取り、None かオブジェクトの永続的 ID を返すカスタム persistent_id() メソッドを持たなくてはなりません。None を返す場合、pickler は通常通りマーカーとともにオブジェクトを pickle 化するため、unpickler はそれを永続的 ID として認識します。

> 外部オブジェクトを非 pickle 化するには、unpickler は永続的 ID オブジェクトを取り被参照オブジェクトを返すカスタム persistent_load() メソッドを持たなくてはなりません。

> これは、外部のオブジェクトを参照によって pickle 化するために永続的 ID をどのように使用するかを示す包括的な例です。

```python
# Simple example presenting how persistent ID can be used to pickle
# external objects by reference.

import pickle
import sqlite3
from collections import namedtuple

# Simple class representing a record in our database.
MemoRecord = namedtuple("MemoRecord", "key, task")

class DBPickler(pickle.Pickler):

    def persistent_id(self, obj):
        # Instead of pickling MemoRecord as a regular class instance, we emit a
        # persistent ID.
        if isinstance(obj, MemoRecord):
            # Here, our persistent ID is simply a tuple, containing a tag and a
            # key, which refers to a specific record in the database.
            return ("MemoRecord", obj.key)
        else:
            # If obj does not have a persistent ID, return None. This means obj
            # needs to be pickled as usual.
            return None


class DBUnpickler(pickle.Unpickler):

    def __init__(self, file, connection):
        super().__init__(file)
        self.connection = connection

    def persistent_load(self, pid):
        # This method is invoked whenever a persistent ID is encountered.
        # Here, pid is the tuple returned by DBPickler.
        cursor = self.connection.cursor()
        type_tag, key_id = pid
        if type_tag == "MemoRecord":
            # Fetch the referenced record from the database and return it.
            cursor.execute("SELECT * FROM memos WHERE key=?", (str(key_id),))
            key, task = cursor.fetchone()
            return MemoRecord(key, task)
        else:
            # Always raises an error if you cannot return the correct object.
            # Otherwise, the unpickler will think None is the object referenced
            # by the persistent ID.
            raise pickle.UnpicklingError("unsupported persistent object")


def main():
    import io
    import pprint

    # Initialize and populate our database.
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE memos(key INTEGER PRIMARY KEY, task TEXT)")
    tasks = (
        'give food to fish',
        'prepare group meeting',
        'fight with a zebra',
        )
    for task in tasks:
        cursor.execute("INSERT INTO memos VALUES(NULL, ?)", (task,))

    # Fetch the records to be pickled.
    cursor.execute("SELECT * FROM memos")
    memos = [MemoRecord(key, task) for key, task in cursor]
    # Save the records using our custom DBPickler.
    file = io.BytesIO()
    DBPickler(file).dump(memos)

    print("Pickled records:")
    pprint.pprint(memos)

    # Update a record, just for good measure.
    cursor.execute("UPDATE memos SET task='learn italian' WHERE key=1")

    # Load the records from the pickle data stream.
    file.seek(0)
    memos = DBUnpickler(file, conn).load()

    print("Unpickled records:")
    pprint.pprint(memos)


if __name__ == '__main__':
    main()
```
```sh
$ python 1.py 
Pickled records:
[MemoRecord(key=1, task='give food to fish'),
 MemoRecord(key=2, task='prepare group meeting'),
 MemoRecord(key=3, task='fight with a zebra')]
Unpickled records:
[MemoRecord(key=1, task='learn italian'),
 MemoRecord(key=2, task='prepare group meeting'),
 MemoRecord(key=3, task='fight with a zebra')]
```

`type_tag`の名前ハードコーディング実装がダサい。もっと簡単にO/Rマッピングしたい。

## [12.1.5.2. ディスパッチテーブル](https://docs.python.jp/3/library/pickle.html#dispatch-tables)

> pickle 化に依存する他のコードの邪魔をせずに、一部のクラスの pickle 化だけをカスタマイズしたい場合、プライベートのディスパッチテーブルを持つ pickler を作成することができます。

> copyreg モジュールによって管理されるグローバルなディスパッチテーブルは copyreg.dispatch_table として利用可能です。したがって、copyreg.dispatch_table の修正済のコピーをプライベートのディスパッチテーブルとして使用することを選択できます。

例えば

```python
f = io.BytesIO()
p = pickle.Pickler(f)
p.dispatch_table = copyreg.dispatch_table.copy()
p.dispatch_table[SomeClass] = reduce_SomeClass
```

> これは SomeClass クラスを特別に扱うプライベートのディスパッチテーブルを持つ pickle.Pickler のインスタンスを作成します。あるいは、次のコード

```python
class MyPickler(pickle.Pickler):
    dispatch_table = copyreg.dispatch_table.copy()
    dispatch_table[SomeClass] = reduce_SomeClass
f = io.BytesIO()
p = MyPickler(f)
```

> も同じことをしますが、 MyPickler のすべてのインスタンスはデフォルトで同じディスパッチテーブルを共有します。 copyreg モジュールを使用する等価なコードは

```python
copyreg.pickle(SomeClass, reduce_SomeClass)
f = io.BytesIO()
p = pickle.Pickler(f)
```

たぶん同一モジュール内における特定のクラスのpickle化だけをカスタマイズする方法なのだろう。1モジュール1クラスにすればいいだけなので無視。

### [12.1.5.3. 状態を持つオブジェクトの扱い](https://docs.python.jp/3/library/pickle.html#handling-stateful-objects)

> ここでは、クラスを pickle 化する振る舞いの変更手順を紹介しています。TextReader クラスはテキストファイルをオープンし、readline() メソッドが呼ばれると、その度に行番号と行の内容を返します。TextReader インスタンスが pickle 化されるとき、ファイルオブジェクトメンバーを 除く すべての属性が保存されます。インスタンスが非 pickle 化されるとき、ファイルは再びオープンされ、最後に読み込んだ位置から読み込みを再開します。このような振る舞いを実装するには __setstate__() および __getstate__() メソッドを使用します。

```python
import pickle
class TextReader:
    """Print and number lines in a text file."""

    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename)
        self.lineno = 0

    def readline(self):
        self.lineno += 1
        line = self.file.readline()
        if not line:
            return None
        if line.endswith('\n'):
            line = line[:-1]
        return "%i: %s" % (self.lineno, line)

    def __getstate__(self):
        # Copy the object's state from self.__dict__ which contains
        # all our instance attributes. Always use the dict.copy()
        # method to avoid modifying the original state.
        state = self.__dict__.copy()
        # Remove the unpicklable entries.
        del state['file']
        return state

    def __setstate__(self, state):
        # Restore instance attributes (i.e., filename and lineno).
        self.__dict__.update(state)
        # Restore the previously opened file's state. To do so, we need to
        # reopen it and read from it until the line count is restored.
        file = open(self.filename)
        for _ in range(self.lineno):
            file.readline()
        # Finally, save the file.
        self.file = file


if __name__ == '__main__':
    reader = TextReader("hello.txt")
    print(reader.readline())
    print(reader.readline())
    new_reader = pickle.loads(pickle.dumps(reader))
    print(new_reader.readline())
```
```sh
$ python 2.py 
1: one
2: two
3: three
```

hello.txt
```
one
two
three
four
```
