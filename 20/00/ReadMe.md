# [11.10. shutil — 高水準のファイル操作](https://docs.python.jp/3/library/shutil.html)

< [11. ファイルとディレクトリへのアクセス](https://docs.python.jp/3/library/filesys.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/shutil.py](https://github.com/python/cpython/tree/3.6/Lib/shutil.py)

> shutil モジュールはファイルやファイルの集まりに対する高水準の操作方法を多数提供します。特にファイルのコピーや削除のための関数が用意されています。個別のファイルに対する操作については、 os モジュールも参照してください。

> 警告

> 高水準のファイルコピー関数 (shutil.copy(), shutil.copy2()) でも、ファイルのメタデータの全てをコピーすることはできません。

> POSIXプラットフォームでは、これはACLやファイルのオーナー、グループが失われることを意味しています。 Mac OSでは、リソースフォーク(resource fork)やその他のメタデータが利用されません。これは、リソースが失われ、ファイルタイプや生成者コード(creator code)が正しくなくなることを意味しています。 Windowsでは、ファイルオーナー、ACL、代替データストリームがコピーされません。

## [11.10.1. ディレクトリとファイルの操作](https://docs.python.jp/3/library/shutil.html#directory-and-files-operations)

属性|意味
----|----
shutil.copyfileobj(fsrc, fdst[, length])|ファイル形式のオブジェクト fsrc の内容を fdst へコピーします。整数値 length は与えられた場合バッファサイズを表します。特に length が負の場合、チャンク内のソースデータを繰り返し操作することなくデータをコピーします。デフォルトでは、制御不能なメモリ消費を避けるためにデータはチャンク内に読み込まれます。 fsrc オブジェクトの現在のファイル位置が0でない場合、現在の位置からファイル終端までの内容のみがコピーされることに注意してください。
shutil.copyfile(src, dst, *, follow_symlinks=True)|src という名前のファイルの内容 (メタデータを含まない) を dst という名前のファイルにコピーし、dst を返します。 src と dst は文字列でパス名を指定します。 dst は完全な対象ファイル名でなければなりません。対象としてディレクトリ名を指定したい場合は shutil.copy() を参照してください。 src と dst が同じファイルだった場合、 SameFileError を送出します。
exception shutil.SameFileError|copyfile() のコピー元と先が同じファイルの場合送出されます。
shutil.copymode(src, dst, *, follow_symlinks=True)|パーミッションを src から dst にコピーします。ファイルの内容、オーナー、グループには影響しません。 src と dst は文字列でファイルのパス名を指定します。 follow_symlinks が偽で、src および dst がシンボリックリンクの場合、 copymode() は (リンク先ではなく) dst 自体のモードを変更します。この機能は全てのプラットフォームで使えるわけではありません。詳しくは copystat() を参照してください。シンボリックリンクの変更をしようとした時、 copymode() がローカルのプラットフォームでシンボリックリンクを変更できない場合は何もしません。
shutil.copystat(src, dst, *, follow_symlinks=True)|パーミッション、最終アクセス時間、最終変更時間、その他のフラグを src から dst にコピーします。 Linux では、 copystat() は可能なら "拡張属性" もコピーします。ファイルの内容、オーナー、グループには影響しません。 src と dst は文字列でファイルのパス名を指定します。
shutil.copy(src, dst, *, follow_symlinks=True)|ファイル src をファイルまたはディレクトリ dst にコピーします。 src と dst は両方共文字列でなければなりません。 dst がディレクトリを指定している場合、ファイルは dst の中に、 src のベースファイル名を使ってコピーされます。新しく作成したファイルのパスを返します。
Zshutil.copy2(src, dst, *, follow_symlinks=True)|copy2() はファイルの全てのメタデータを保持しようとすることを除けば copy() と等価です。
shutil.ignore_patterns(*patterns)|このファクトリ関数は、 copytree() 関数の ignore 引数に渡すための呼び出し可能オブジェクトを作成します。 glob形式の patterns にマッチするファイルやディレクトリが無視されます。下の例を参照してください。
shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False)|src をルートにしたディレクトリツリー全体をコピーして、コピー先ディレクトリを返します。コピー先ディレクトリ dst は事前に存在していてはならず、足りない親ディレクトリと合わせて作成されます。ディレクトリの各種時間やパーミッションは copystat() でコピーし、各ファイルは shutil.copy2() でコピーします。
shutil.rmtree(path, ignore_errors=False, onerror=None)|ディレクトリツリー全体を削除します。 path はディレクトリを指していなければなりません (ただしディレクトリに対するシンボリックリンクではいけません)。ignore_errors が真である場合、削除に失敗したことによるエラーは無視されます。偽や省略された場合はこれらのエラーは onerror で与えられたハンドラを呼び出して処理され、onerror が省略された場合は例外を送出します。
    rmtree.avoids_symlink_attacks|    プラットフォームと実装がシンボリックリンク攻撃に耐性のあるバージョンの rmtree() を提供しているかどうかを示します。現在のところ、この属性は fd ベースのディレクトリアクセス関数をサポートしているプラットフォームでのみ真になります。
shutil.move(src, dst, copy_function=copy2)|ファイルまたはディレクトリ (src) を再帰的に別の場所 (dst) に移動して、移動先を返します。
shutil.disk_usage(path)|指定されたパスについて、ディスクの利用状況を、名前付きタプル (named tuple) で返します。このタプルには total, used, free という属性があり、それぞれトータル、使用中、空きの容量をバイト単位で示します。
shutil.chown(path, user=None, group=None)|指定された path のオーナー user と/または group を変更します。
shutil.which(cmd, mode=os.F_OK | os.X_OK, path=None)|cmd を実行しようとした時に実行される実行ファイルのパスを返します。 cmd を呼び出せない場合は None を返します。
exception shutil.Error|この例外は複数ファイルの操作を行っているときに生じる例外をまとめたものです。 copytree() に対しては例外の引数は3つのタプル(srcname, dstname, exception)からなるリストです。

```python
import shutil
fnma = 'a.txt'
fnmb = 'b.txt'
with open(fnma) as a:
    with open(fnmb, 'w') as b:
        shutil.copyfileobj(a, b)

#shutil.copyfile(fnma, fnma)#shutil.SameFileError: 'a.txt' and 'a.txt' are the same file
shutil.copyfile(fnma, fnmb)
shutil.copymode(fnma, fnmb)
shutil.copystat(fnma, fnmb)

shutil.copy(fnma, fnmb)
shutil.copy2(fnma, fnmb)

p = shutil.ignore_patterns('*.txt')
print(p)
shutil.copytree('a', 'b', ignore=p)
#shutil.rmtree(path)
print(shutil.rmtree.avoids_symlink_attacks)
#shutil.move(src, dst)
print(shutil.disk_usage('.'))
shutil.chown('a.txt', 'mint')
print(shutil.which('python'))
```
```sh
$ python 0.py 
<function ignore_patterns.<locals>._ignore_patterns at 0xb7252614>
True
usage(total=492019548160, used=12310695936, free=454692048896)
/home/mint/.pyenv/versions/3.6.1/bin/python
```

### [11.10.1.1. copytree の例](https://docs.python.jp/3/library/shutil.html#rmtree-example)

> 以下は前述の copytree() 関数のドキュメント文字列を省略した実装例です。本モジュールで提供される他の関数の使い方を示しています。

```python
def copytree(src, dst, symlinks=False):
    names = os.listdir(src)
    os.makedirs(dst)
    errors = []
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                copytree(srcname, dstname, symlinks)
            else:
                copy2(srcname, dstname)
            # XXX What about devices, sockets etc.?
        except OSError as why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except Error as err:
            errors.extend(err.args[0])
    try:
        copystat(src, dst)
    except OSError as why:
        # can't copy file access times on Windows
        if why.winerror is None:
            errors.extend((src, dst, str(why)))
    if errors:
        raise Error(errors)
```

ignore_patterns() ヘルパ関数を利用する、もう1つの例です。

```python
from shutil import copytree, ignore_patterns

copytree(source, destination, ignore=ignore_patterns('*.pyc', 'tmp*'))
```

この例では、 .pyc ファイルと、 tmp で始まる全てのファイルやディレクトリを除いて、全てをコピーします。

ignore 引数にロギングさせる別の例です。

```python
from shutil import copytree
import logging

def _logpath(path, names):
    logging.info('Working in %s', path)
    return []   # nothing will be ignored

copytree(source, destination, ignore=_logpath)
```

### [11.10.1.2. rmtree の例](https://docs.python.jp/3/library/shutil.html#rmtree-example)

> 次の例は、Windows で一部のファイルが読み取り専用のビットセットを含む場合に、ディレクトリツリーを削除する方法を示します。onerror コールバックを使用して、読み取り専用のビットを消去し、削除を再試行します。結果として失敗が発生した場合、それらは伝搬されます:

```python
import os, stat
import shutil

def remove_readonly(func, path, _):
    "Clear the readonly bit and reattempt the removal"
    os.chmod(path, stat.S_IWRITE)
    func(path)

shutil.rmtree(directory, onerror=remove_readonly)
```

## [11.10.2. アーカイブ化操作](https://docs.python.jp/3/library/shutil.html#archiving-operations)

> バージョン 3.2 で追加.

> バージョン 3.5 で変更: xztar 形式のサポートが追加されました。

> 圧縮とアーカイブ化されているファイルの読み書きの高水準なユーティリティも提供されています。これらは zipfile 、 tarfile モジュールに依拠しています。

属性|説明
----|----
shutil.make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]])|アーカイブファイル (zip や tar) を作成してその名前を返します。
shutil.register_archive_format(name, function[, extra_args[, description]])|アーカイバをフォーマット name に登録します。
shutil.unregister_archive_format(name)|アーカイブフォーマット name を、サポートされているフォーマットのリストから取り除きます。
shutil.unpack_archive(filename[, extract_dir[, format]])|アーカイブをアンパックします。 filename はアーカイブのフルパスです。
shutil.register_unpack_format(name, extensions, function[, extra_args[, description]])|アンパック用のフォーマットを登録します。 name はフォーマット名で、 extensions はそのフォーマットに対応する拡張子 (例えば Zip ファイルに対して .zip) のリストです。
shutil.unregister_unpack_format(name)|アンパックフォーマットを登録解除します。 name はフォーマットの名前です。
shutil.get_unpack_formats()|登録されているすべてのアンパックフォーマットをリストで返します。戻り値のリストの各要素は (name, extensions, description) の形のタプルです。

### [11.10.2.1. アーカイブ化の例](https://docs.python.jp/3/library/shutil.html#archiving-example)

```python
>>> from shutil import make_archive
>>> import os
>>> archive_name = os.path.expanduser(os.path.join('~', 'myarchive'))
>>> root_dir = os.path.expanduser(os.path.join('~', '.ssh'))
>>> make_archive(archive_name, 'gztar', root_dir)
'/Users/tarek/myarchive.tar.gz'
```

### [11.10.3. 出力ターミナルのサイズの取得](https://docs.python.jp/3/library/shutil.html#querying-the-size-of-the-output-terminal)

属性|説明
----|----
shutil.get_terminal_size(fallback=(columns, lines))|ターミナルウィンドウのサイズを取得します。

