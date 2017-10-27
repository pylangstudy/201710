# [12.6. sqlite3 — SQLite データベースに対する DB-API 2.0 インタフェース](https://docs.python.jp/3/library/sqlite3.html)

< [12. データの永続化](https://docs.python.jp/3/library/persistence.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/sqlite3/](https://github.com/python/cpython/tree/3.6/Lib/sqlite3/)

> SQLite は、軽量なディスク上のデータベースを提供する C ライブラリです。別のサーバプロセスを用意する必要なく、 SQL クエリー言語の非標準的な一種を使用してデータベースにアクセスできます。一部のアプリケーションは内部データ保存に SQLite を使えます。また、SQLite を使ってアプリケーションのプロトタイプを作り、その後そのコードを PostgreSQL や Oracle のような大規模データベースに移植するということも可能です。

> sqlite3 モジュールの著者は Gerhard Häring です。 PEP 249 で記述されている DB-API 2.0 に準拠した SQL インターフェイスを提供します。

> このモジュールを使うには、最初にデータベースを表す Connection オブジェクトを作ります。ここではデータはファイル example.db に格納されているものとします:

```python
import sqlite3
conn = sqlite3.connect('example.db')
```

> 特別な名前である :memory: を使うと RAM 上にデータベースを作ることもできます。

> Connection があれば、 Cursor オブジェクトを作りその execute() メソッドを呼んで SQL コマンドを実行することができます:

```python
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
```

> 保存されたデータは永続的であり、次回のセッションでもそのまま使用できます:

```python
import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
```

> たいてい、SQL 操作では Python 変数の値を使う必要があります。この時、クエリーを Python の文字列操作を使って構築することは安全とは言えないので、すべきではありません。そのようなことをするとプログラムが SQL インジェクション攻撃に対し脆弱になります (https://xkcd.com/327/ ではどうなってしまうかをユーモラスに描いています)。

> 代わりに、DB-API のパラメータ割り当てを使います。 ? を変数の値を使いたいところに埋めておきます。その上で、値のタプルをカーソルの execute() メソッドの第2引数として引き渡します。(他のデータベースモジュールでは変数の場所を示すのに %s や :1 などの異なった表記を用いることがあります。) 例を示します:

```python
# Never do this -- insecure!
symbol = 'RHAT'
c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# Do this instead
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
```

> SELECT 文を実行した後データを取得する方法は3つありどれを使っても構いません。一つはカーソルをイテレータ (iterator) として扱う、一つはカーソルの fetchone() メソッドを呼んで一致した内の一行を取得する、もう一つは fetchall() メソッドを呼んで一致した全ての行のリストとして受け取る、という3つです。

以下の例ではイテレータの形を使います:

```python
>>> for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)

('2006-01-05', 'BUY', 'RHAT', 100, 35.14)
('2006-03-28', 'BUY', 'IBM', 1000, 45.0)
('2006-04-06', 'SELL', 'IBM', 500, 53.0)
('2006-04-05', 'BUY', 'MSFT', 1000, 72.0)
```

### 参考

URL|概要
---|----
[https://github.com/ghaering/pysqlite](https://github.com/ghaering/pysqlite)|pysqlite のウェブページ – sqlite3 は「pysqlite」という名の下、外部で開発されています。
[https://www.sqlite.org](https://www.sqlite.org)|SQLite のウェブページ。ここの文書ではサポートされる SQL 方言の文法と使えるデータ型を説明しています。
[http://www.w3schools.com/sql/](http://www.w3schools.com/sql/)|SQL 学習に効くチュートリアル、リファレンス、実例集。
[PEP 249](https://www.python.org/dev/peps/pep-0249) - Database API Specification 2.0|Marc-Andre Lemburg により書かれた PEP。

## [12.6.1. モジュールの関数と定数](https://docs.python.jp/3/library/sqlite3.html#module-functions-and-constants)

属性|概要
----|----
sqlite3.version|文字列で表現されたモジュールのバージョン番号です。これは SQLite ライブラリのバージョンではありません。
sqlite3.version_info|整数のタプルで表現されたモジュールのバージョン番号です。これは SQLite ライブラリのバージョンではありません。
sqlite3.sqlite_version|文字列で表現された SQLite ランタイムライブラリのバージョン番号です。
sqlite3.sqlite_version_info|整数のタプルで表現された SQLite ランタイムライブラリのバージョン番号です。
sqlite3.PARSE_DECLTYPES|この定数は connect() 関数の detect_types パラメータとして使われます。この定数を設定すると sqlite3 モジュールは戻り値のカラムの宣言された型を読み取るようになります。意味を持つのは宣言の最初の単語です。すなわち、"integer primary key" においては "integer" が読み取られます。また、 "number(10)" では、 "number" が読み取られます。そして、そのカラムに対して、変換関数の辞書を探してその型に対して登録された関数を使うようにします。
sqlite3.PARSE_COLNAMES|この定数は connect() 関数の detect_types パラメータとして使われます。この定数を設定すると SQLite のインタフェースは戻り値のそれぞれのカラムの名前を読み取るようになります。文字列の中の [mytype] といった形の部分を探し、'mytype' がそのカラムの名前であると判断します。そして 'mytype' のエントリを変換関数辞書の中から見つけ、見つかった変換関数を値を返す際に用います。 Cursor.description で見つかるカラム名はその最初の単語だけです。すなわち、もし 'as "x [datetime]"' のようなものを SQL の中で使っていたとすると、読み取るのはカラム名の中の最初の空白までの全てですので、カラム名として使われるのは単純に "x" ということになります。

属性|概要
----|----
sqlite3.connect(database[, timeout, detect_types, isolation_level, check_same_thread, factory, cached_statements, uri])|ファイル database の SQLite データベースへの接続を開きます。":memory:" という名前を使うことでディスクの代わりに RAM 上のデータベースへの接続を開くこともできます。
sqlite3.register_converter(typename, callable)|データベースから得られるバイト列を希望する Python の型に変換する呼び出し可能オブジェクト (callable) を登録します。その呼び出し可能オブジェクトは型が typename である全てのデータベース上の値に対して呼び出されます。型検知がどのように働くかについては connect() 関数の detect_types パラメータの説明も参照してください。注意が必要なのは typename はクエリの中の型名と大文字小文字も一致しなければならないということです！
sqlite3.register_adapter(type, callable)|自分が使いたい Python の型 type を SQLite がサポートしている型に変換する呼び出し可能オブジェクト (callable) を登録します。その呼び出し可能オブジェクト callable はただ一つの引数に Python の値を受け取り、int, float, str または bytes のいずれかの型の値を返さなければなりません。
sqlite3.complete_statement(sql)|文字列 sql がセミコロンで終端された一つ以上の完全な SQL 文を含んでいる場合、 True を返します。判定は SQL 文として文法的に正しいかではなく、閉じられていない文字列リテラルが無いことおよびセミコロンで終端されていることだけで行われます。
sqlite3.enable_callback_tracebacks(flag)|デフォルトでは、ユーザ定義の関数、集計関数、変換関数、認可コールバックなどはトレースバックを出力しません。デバッグの際にはこの関数を flag に True を指定して呼び出します。そうした後は先に述べたような関数のトレースバックが sys.stderr に出力されます。元に戻すには False を使います。

## [12.6.2. Connection オブジェクト](https://docs.python.jp/3/library/sqlite3.html#connection-objects)

属性|概要
----|----
class sqlite3.Connection|SQLite データベースコネクション。以下の属性やメソッドを持ちます
    isolation_level|    現在の分離レベルを取得または設定します。 None で自動コミットモードまたは "DEFERRED", "IMMEDIATE", "EXLUSIVE" のどれかです。より詳しい説明は トランザクション制御 節を参照してください。
    in_transaction|    トランザクションがアクティブなら (未コミットの変更があるなら) True 、そうでなければ False 。リードオンリー属性です。
    cursor(factory=Cursor)|    cursor メソッドはオション引数 factory を 1 つだけ受け付けます。 渡された場合は、 Cursor またはそのサブクラスのインスタンスを返す呼び出し可能オブジェクトでなければなりません。
    commit()|    このメソッドは現在のトランザクションをコミットします。このメソッドを呼ばないと、前回 commit() を呼び出してから行ったすべての変更は、他のデータベースコネクションから見ることができません。もし、データベースに書き込んだはずのデータが見えなくて悩んでいる場合は、このメソッドの呼び出しを忘れていないかチェックしてください。
    rollback()|    このメソッドは最後に行った commit() 後の全ての変更をロールバックします。
    close()|    このメソッドはデータベースコネクションを閉じます。このメソッドが自動的に commit() を呼び出さないことに注意してください。 commit() をせずにコネクションを閉じると、変更が消えてしまいます！
    execute(sql[, parameters])|    This is a nonstandard shortcut that creates a cursor object by calling the cursor() method, calls the cursor’s execute() method with the parameters given, and returns the cursor.(これは非標準のショートカットで、cursor（）メソッドを呼び出してカーソルオブジェクトを作成し、与えられたパラメータでカーソルのexecute（）メソッドを呼び出してカーソルを返します。)
    executemany(sql[, parameters])|    This is a nonstandard shortcut that creates a cursor object by calling the cursor() method, calls the cursor’s executemany() method with the parameters given, and returns the cursor.(これは非標準のショートカットで、cursor（）メソッドを呼び出してカーソルオブジェクトを作成し、与えられたパラメータでカーソルのexecutemany（）メソッドを呼び出してカーソルを返します。)
    executescript(sql_script)|    This is a nonstandard shortcut that creates a cursor object by calling the cursor() method, calls the cursor’s executescript() method with the given sql_script, and returns the cursor.(これは非標準のショートカットで、cursor（）メソッドを呼び出してカーソルオブジェクトを作成し、指定されたsql_scriptを使用してカーソルのstartscript（）メソッドを呼び出し、カーソルを返します。)
    create_function(name, num_params, func)|    Creates a user-defined function that you can later use from within SQL statements under the function name name. num_params is the number of parameters the function accepts (if num_params is -1, the function may take any number of arguments), and func is a Python callable that is called as the SQL function.(後で関数名nameのSQL文の中から使用できるユーザー定義関数を作成します。 num_paramsは、関数が受け入れるパラメータの数です（num_paramsが-1の場合、関数は任意の数の引数を取ります）。funcはSQL関数として呼び出されるPython呼び出し可能です。)
    create_aggregate(name, num_params, aggregate_class)|    ユーザ定義の集計関数を作成します。
    create_collation(name, callable)|    name と callable で指定される照合順序を作成します。呼び出し可能オブジェクトには二つの文字列が渡されます。一つめのものが二つめのものより低く順序付けられるならば -1 を返し、等しければ 0 を返し、一つめのものが二つめのものより高く順序付けられるならば 1 を返すようにしなければなりません。この関数はソート(SQL での ORDER BY)をコントロールするもので、比較を行なうことは他の SQL 操作には影響を与えないことに注意しましょう。
    interrupt()|    このメソッドを別スレッドから呼び出して接続上で現在実行中であろうクエリを中断させられます。クエリが中断されると呼び出し元は例外を受け取ります。
    set_authorizer(authorizer_callback)|    このルーチンはコールバックを登録します。コールバックはデータベースのテーブルのカラムにアクセスしようとするたびに呼び出されます。コールバックはアクセスが許可されるならば SQLITE_OK を、SQL 文全体がエラーとともに中断されるべきならば SQLITE_DENY を、カラムが NULL 値として扱われるべきなら SQLITE_IGNORE を返さなければなりません。これらの定数は sqlite3 モジュールに用意されています。
    set_progress_handler(handler, n)|    このメソッドはコールバックを登録します。コールバックは SQLite 仮想マシン上の n 個の命令を実行するごとに呼び出されます。これは、GUI 更新などのために、長時間かかる処理中に SQLite からの呼び出しが欲しい場合に便利です。
    set_trace_callback(trace_callback)|    各 SQL 文が SQLite バックエンドによって実際に実行されるたびに呼び出される trace_callback を登録します。
    enable_load_extension(enabled)|    このメソッドは SQLite エンジンが共有ライブラリから SQLite 拡張を読み込むのを許可したり、禁止したりします。SQLite 拡張は新しい関数や集計関数や仮想テーブルの実装を定義できます。1つの有名な拡張は SQLite によって頒布されている全テキスト検索拡張です。
    load_extension(path)|    このメソッドは共有ライブラリから SQLite 拡張を読み込みます。このメソッドを使う前に enable_load_extension() で拡張の読み込みを許可しておかなくてはなりません。
    row_factory|    この属性を変更して、カーソルと元の行をタプル形式で受け取り、本当の結果の行を返す呼び出し可能オブジェクトにすることができます。これによって、より進んだ結果の返し方を実装することができます。例えば、各列に列名でもアクセスできるようなオブジェクトを返すことができます。
    text_factory|    この属性を使って TEXT データ型をどのオブジェクトで返すかを制御できます。デフォルトではこの属性は str に設定されており、 sqlite3 モジュールは TEXT を Unicode オブジェクトで返します。もしバイト列で返したいならば、 bytes に設定してください。
    total_changes|    データベース接続が開始されて以来の行の変更・挿入・削除がなされた行の総数を返します。
    iterdump()|    データベースをSQL testフォーマットでダンプするためのイテレータを返します。 メモリ内のデータベースの内容を、後で復元するために保存する場合に便利です。この関数には、 sqlite3 シェルの中の .dump コマンドと同じ機能があります。

