# [12.6. sqlite3 — SQLite データベースに対する DB-API 2.0 インタフェース](https://docs.python.jp/3/library/sqlite3.html)

< [12. データの永続化](https://docs.python.jp/3/library/persistence.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## [12.6.3. カーソルオブジェクト](https://docs.python.jp/3/library/sqlite3.html#cursor-objects)

属性|概要
----|----
class sqlite3.Cursor|Cursor インスタンスは以下の属性やメソッドを持ちます。
    execute(sql[, parameters])|    SQL 文を実行します。SQL 文はパラメータ化できます(すなわち SQL リテラルの代わりの場所確保文字 (placeholder) を入れておけます)。 sqlite3 モジュールは2種類の場所確保記法をサポートします。一つは疑問符(qmark スタイル)、もう一つは名前(named スタイル)です。
    executemany(sql, seq_of_parameters)|    Executes an SQL command against all parameter sequences or mappings found in the sequence seq_of_parameters. The sqlite3 module also allows using an iterator yielding parameters instead of a sequence.
    executescript(sql_script)|    これは非標準の便宜メソッドで、一度に複数の SQL 文を実行することができます。メソッドは最初に COMMIT 文を発行し、次いで引数として渡された SQLスクリプトを実行します。
    fetchone()|    クエリ結果から次の row をフェッチして、1つのシーケンスを返します。これ以上データがない場合は None を返します。
    fetchmany(size=cursor.arraysize)|    クエリ結果から次の幾つかの row をフェッチして、リストを返します。これ以上データがない場合は空のリストを返します。
    fetchall()|    全ての(残りの)クエリ結果の row をフェッチして、リストを返します。cursor の arraysize 属性がこの操作のパフォーマンスに影響することに気をつけてください。これ以上の row がない場合は、空のリストが返されます。
    close()|    Close the cursor now (rather than whenever __del__ is called).
    rowcount|    一応 sqlite3 モジュールの Cursor クラスはこの属性を実装していますが、データベースエンジン自身の「影響を受けた行」/「選択された行」の決定方法は少し風変わりです。
    lastrowid|    This read-only attribute provides the rowid of the last modified row. It is only set if you issued an INSERT or a REPLACE statement using the execute() method. For operations other than INSERT or REPLACE or when executemany() is called, lastrowid is set to None.
    arraysize|    Read/write attribute that controls the number of rows returned by fetchmany(). The default value is 1 which means a single row would be fetched per call.
    description|    この読み出し専用の属性は、最後のクエリの結果のカラム名を提供します。 Python DB API との互換性を維持するために、各カラムに対して 7つのタプルを返しますが、タプルの後ろ6つの要素は全て None です。
    connection|    この読み出し専用の属性は、 Cursor オブジェクトが使用する SQLite データベースの Connection を提供します。con.cursor() を呼び出すことにより作成される Cursor オブジェクトは、 con を参照する connection 属性を持ちます:

## [12.6.4. Row オブジェクト](https://docs.python.jp/3/library/sqlite3.html#row-objects)

属性|概要
----|----
class sqlite3.Row|Row インスタンスは、 Connection オブジェクトの row_factory として高度に最適化されています。タプルによく似た機能を持つ row を作成します。
    keys()|    このメソッドはカラム名のリストを返します。クエリ直後から、これは Cursor.description の各タプルの最初のメンバになります。

> Rowの例のために、まずサンプルのテーブルを初期化します:

```python
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute('''create table stocks
(date text, trans text, symbol text,
 qty real, price real)''')
c.execute("""insert into stocks
          values ('2006-01-05','BUY','RHAT',100,35.14)""")
conn.commit()
c.close()
```

> そして、 Row を使ってみます:

```python
>>> conn.row_factory = sqlite3.Row
>>> c = conn.cursor()
>>> c.execute('select * from stocks')
<sqlite3.Cursor object at 0x7f4e7dd8fa80>
>>> r = c.fetchone()
>>> type(r)
<class 'sqlite3.Row'>
>>> tuple(r)
('2006-01-05', 'BUY', 'RHAT', 100.0, 35.14)
>>> len(r)
5
>>> r[2]
'RHAT'
>>> r.keys()
['date', 'trans', 'symbol', 'qty', 'price']
>>> r['qty']
100.0
>>> for member in r:
...     print(member)
...
2006-01-05
BUY
RHAT
100.0
35.14
```


## [12.6.5. 例外](https://docs.python.jp/3/library/sqlite3.html#exceptions)

属性|概要
----|----
exception sqlite3.Warning|A subclass of Exception.
exception sqlite3.Error|このモジュールにおける他の例外クラスの基底クラスです。 Exception のサブクラスです。
exception sqlite3.DatabaseError|Exception raised for errors that are related to the database.
exception sqlite3.IntegrityError|Exception raised when the relational integrity of the database is affected, e.g. a foreign key check fails. It is a subclass of DatabaseError.
exception sqlite3.ProgrammingError|Exception raised for programming errors, e.g. table not found or already exists, syntax error in the SQL statement, wrong number of parameters specified, etc. It is a subclass of DatabaseError.

## [12.6.6. SQLite と Python の型](https://docs.python.jp/3/library/sqlite3.html#sqlite-and-python-types)

### [12.6.6.1. はじめに](https://docs.python.jp/3/library/sqlite3.html#introduction)

> SQLite は以下の型をネイティブにサポートします: NULL, INTEGER, REAL, TEXT, BLOB。

> したがって、次の Python の型は問題なく SQLite に送り込めます:

Python の型|SQLite の型
-----------|-----------
None|NULL
int|INTEGER
float|REAL
str|TEXT
bytes|BLOB

> SQLite の型から Python の型へのデフォルトでの変換は以下の通りです:

SQLite の型|Python の型
-----------|-----------
NULL|None
INTEGER|int
REAL|float
TEXT|text_factory に依存する。デフォルトでは str 。
BLOB|bytes

> sqlite3 モジュールの型システムは二つの方法で拡張できます。一つはオブジェクト適合(adaptation)を通じて追加された Python の型を SQLite に格納することです。もう一つは変換関数(converter)を通じて sqlite3 モジュールに SQLite の型を違った Python の型に変換させることです。

### [12.6.6.2. 追加された Python の型を SQLite データベースに格納するために適合関数を使う](https://docs.python.jp/3/library/sqlite3.html#using-adapters-to-store-additional-python-types-in-sqlite-databases)

#### [12.6.6.2.1. オブジェクト自身で適合するようにする](https://docs.python.jp/3/library/sqlite3.html#letting-your-object-adapt-itself)

> 自分でクラスを書いているならばこの方法が良いでしょう。次のようなクラスがあるとします:

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
```

> さてこの点を SQLite の一つのカラムに収めたいと考えたとしましょう。最初にしなければならないのはサポートされている型の中から点を表現するのに使えるものを選ぶことです。ここでは単純に文字列を使うことにして、座標を区切るのにはセミコロンを使いましょう。次に必要なのはクラスに変換された値を返す __conform__(self, protocol) メソッドを追加することです。引数 protocol は PrepareProtocol になります。

```python
import sqlite3

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            return "%f;%f" % (self.x, self.y)

con = sqlite3.connect(":memory:")
cur = con.cursor()

p = Point(4.0, -3.2)
cur.execute("select ?", (p,))
print(cur.fetchone()[0])
```

#### [12.6.6.2.2. 適合関数を登録する](https://docs.python.jp/3/library/sqlite3.html#registering-an-adapter-callable)

> もう一つの可能性は型を文字列表現に変換する関数を作り register_adapter() でその関数を登録することです。

```python
import sqlite3

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

def adapt_point(point):
    return "%f;%f" % (point.x, point.y)

sqlite3.register_adapter(Point, adapt_point)

con = sqlite3.connect(":memory:")
cur = con.cursor()

p = Point(4.0, -3.2)
cur.execute("select ?", (p,))
print(cur.fetchone()[0])
```

> sqlite3 モジュールには二つの Python 標準型 datetime.date と datetime.datetime に対するデフォルト適合関数があります。いま datetime.datetime オブジェクトを ISO 表現でなく Unix タイムスタンプとして格納したいとしましょう。

```python
import sqlite3
import datetime
import time

def adapt_datetime(ts):
    return time.mktime(ts.timetuple())

sqlite3.register_adapter(datetime.datetime, adapt_datetime)

con = sqlite3.connect(":memory:")
cur = con.cursor()

now = datetime.datetime.now()
cur.execute("select ?", (now,))
print(cur.fetchone()[0])
```

#### [12.6.6.3. SQLite の値を好きな Python 型に変換する](https://docs.python.jp/3/library/sqlite3.html#converting-sqlite-values-to-custom-python-types)

> 適合関数を書くことで好きな Python 型を SQLite に送り込めるようになりました。しかし、本当に使い物になるようにするには Python から SQLite さらに Python へという往還(roundtrip)の変換ができる必要があります。

> そこで変換関数(converter)です。

> Point クラスの例に戻りましょう。x, y 座標をセミコロンで区切った文字列として SQLite に格納したのでした。

> まず、文字列を引数として取り Point オブジェクトをそれから構築する変換関数を定義します。

> 注釈

> 変換関数は SQLite に送り込んだデータ型に関係なく 常に bytes オブジェクトを渡されます。

```python
def convert_point(s):
    x, y = map(float, s.split(b";"))
    return Point(x, y)
```

> 次に sqlite3 モジュールにデータベースから取得したものが本当に点であることを教えなければなりません。二つの方法があります:

    宣言された型を通じて暗黙的に
    カラム名を通じて明示的に

> どちらの方法も モジュールの関数と定数 節の中で説明されています。それぞれ PARSE_DECLTYPES 定数と PARSE_COLNAMES 定数の項目です。

> 以下の例で両方のアプローチを紹介します。

```python
import sqlite3

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return "(%f;%f)" % (self.x, self.y)

def adapt_point(point):
    return ("%f;%f" % (point.x, point.y)).encode('ascii')

def convert_point(s):
    x, y = list(map(float, s.split(b";")))
    return Point(x, y)

# Register the adapter
sqlite3.register_adapter(Point, adapt_point)

# Register the converter
sqlite3.register_converter("point", convert_point)

p = Point(4.0, -3.2)

#########################
# 1) Using declared types
con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
cur = con.cursor()
cur.execute("create table test(p point)")

cur.execute("insert into test(p) values (?)", (p,))
cur.execute("select p from test")
print("with declared types:", cur.fetchone()[0])
cur.close()
con.close()

#######################
# 1) Using column names
con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_COLNAMES)
cur = con.cursor()
cur.execute("create table test(p)")

cur.execute("insert into test(p) values (?)", (p,))
cur.execute('select p as "p [point]" from test')
print("with column names:", cur.fetchone()[0])
cur.close()
con.close()
```

### [12.6.6.4. デフォルトの適合関数と変換関数](https://docs.python.jp/3/library/sqlite3.html#default-adapters-and-converters)

> datetime モジュールの date 型および datetime 型のためのデフォルト適合関数があります。これらの型は ISO 日付 / ISO タイムスタンプとして SQLite に送られます。

> デフォルトの変換関数は datetime.date 用が "date" という名前で、 datetime.datetime 用が "timestamp" という名前で登録されています。

> これにより、多くの場合特別な細工無しに Python の日付 / タイムスタンプを使えます。適合関数の書式は実験的な SQLite の date/time 関数とも互換性があります。

> 以下の例でこのことを確かめます。

```python
import sqlite3
import datetime

con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cur = con.cursor()
cur.execute("create table test(d date, ts timestamp)")

today = datetime.date.today()
now = datetime.datetime.now()

cur.execute("insert into test(d, ts) values (?, ?)", (today, now))
cur.execute("select d, ts from test")
row = cur.fetchone()
print(today, "=>", row[0], type(row[0]))
print(now, "=>", row[1], type(row[1]))

cur.execute('select current_date as "d [date]", current_timestamp as "ts [timestamp]"')
row = cur.fetchone()
print("current_date", row[0], type(row[0]))
print("current_timestamp", row[1], type(row[1]))
```

> SQLite に格納されているタイムスタンプが6桁より長い小数部を持っている場合、タイムスタンプの変換関数によってマイクロ秒精度に丸められます。

### [12.6.7. トランザクション制御](https://docs.python.jp/3/library/sqlite3.html#controlling-transactions)

> By default, the sqlite3 module opens transactions implicitly before a Data Modification Language (DML) statement (i.e. INSERT/UPDATE/DELETE/REPLACE).

> sqlite3 が暗黙のうちに実行する BEGIN 文の種類(またはそういうものを使わないこと)を connect() 呼び出しの isolation_level パラメータを通じて、または接続の isolation_level プロパティを通じて、制御することができます。

> 自動コミットモード を使いたい場合は、 isolation_level は None にしてください。

> そうでなければデフォルトのまま BEGIN 文を使い続けるか、SQLite がサポートする分離レベル "DEFERRED", "IMMEDIATE" または "EXCLUSIVE" を設定してください。

> The current transaction state is exposed through the Connection.in_transaction attribute of the connection object.

> バージョン 3.6 で変更: sqlite3 used to implicitly commit an open transaction before DDL statements. This is no longer the case.

### [12.6.8. sqlite3 の効率的な使い方](https://docs.python.jp/3/library/sqlite3.html#using-sqlite3-efficiently)

#### [12.6.8.1. ショートカットメソッドを使う](https://docs.python.jp/3/library/sqlite3.html#using-shortcut-methods)

> Connection オブジェクトの非標準的なメソッド execute(), executemany(), executescript() を使うことで、 (しばしば余計な) Cursor オブジェクトをわざわざ作り出さずに済むので、コードをより簡潔に書くことができます。 Cursor オブジェクトは暗黙裡に生成されショートカットメソッドの戻り値として受け取ることができます。この方法を使えば、 SELECT 文を実行してその結果について反復することが、 Connection オブジェクトに対する呼び出し一つで行なえます。

```python
import sqlite3

persons = [
    ("Hugo", "Boss"),
    ("Calvin", "Klein")
    ]

con = sqlite3.connect(":memory:")

# Create the table
con.execute("create table person(firstname, lastname)")

# Fill the table
con.executemany("insert into person(firstname, lastname) values (?, ?)", persons)

# Print the table contents
for row in con.execute("select firstname, lastname from person"):
    print(row)

print("I just deleted", con.execute("delete from person").rowcount, "rows")
```

#### [12.6.8.2. 位置ではなく名前でカラムにアクセスする](https://docs.python.jp/3/library/sqlite3.html#accessing-columns-by-name-instead-of-by-index)

> sqlite3 モジュールの有用な機能の一つに、行生成関数として使われるための sqlite3.Row クラスがあります。

> このクラスでラップされた行は、位置インデクス(タプルのような)でも大文字小文字を区別しない名前でもアクセスできます:

```python
import sqlite3

con = sqlite3.connect(":memory:")
con.row_factory = sqlite3.Row

cur = con.cursor()
cur.execute("select 'John' as name, 42 as age")
for row in cur:
    assert row[0] == row["name"]
    assert row["name"] == row["nAmE"]
    assert row[1] == row["age"]
    assert row[1] == row["AgE"]
```

#### [12.6.8.3. コネクションをコンテキストマネージャーとして利用する](https://docs.python.jp/3/library/sqlite3.html#using-the-connection-as-a-context-manager)

> Connection オブジェクトはコンテキストマネージャーとして利用して、トランザクションを自動的にコミットしたりロールバックすることができます。例外が発生したときにトランザクションはロールバックされ、それ以外の場合、トランザクションはコミットされます:

```python
import sqlite3

con = sqlite3.connect(":memory:")
con.execute("create table person (id integer primary key, firstname varchar unique)")

# Successful, con.commit() is called automatically afterwards
with con:
    con.execute("insert into person(firstname) values (?)", ("Joe",))

# con.rollback() is called after the with block finishes with an exception, the
# exception is still raised and must be caught
try:
    with con:
        con.execute("insert into person(firstname) values (?)", ("Joe",))
except sqlite3.IntegrityError:
    print("couldn't add Joe twice")
```

### [12.6.9. 既知の問題](https://docs.python.jp/3/library/sqlite3.html#common-issues)

#### [12.6.9.1. マルチスレッド](https://docs.python.jp/3/library/sqlite3.html#multithreading)

> 古いバージョンの SQLite はスレッド間でのコネクションの共有に問題がありました。その理由は、Python のモジュールではスレッド間のコネクションとカーソルの共有ができないためです。依然としてそのようなことをしようとすると、実行時に例外を受け取るでしょう。

> 唯一の例外は interrupt() メソッドで、これだけが異なるスレッドから呼び出せます。

