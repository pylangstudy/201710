# [12.1. pickle — Python オブジェクトの直列化](https://docs.python.jp/3/library/pickle.html)

< [12. データの永続化](https://docs.python.jp/3/library/persistence.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/pickle.py](https://github.com/python/cpython/tree/3.6/Lib/pickle.py)

## [12.1.6. グローバル変数を制限する](https://docs.python.jp/3/library/pickle.html#restricting-globals)

> デフォルトで、非 pickle 化は pickle データ内で見つけたあらゆるクラスや関数をインポートします。多くのアプリケーションでは、この振る舞いは受け入れられません。なぜなら、それによって unpickler が任意のコードをインポートして実行することが可能になるからです。この手の巧妙に作られた pickle データストリームがロードされたときに何を行うかをちょっと考えてみてください:

```python
import pickle
pickle.loads(b"cos\nsystem\n(S'echo hello world'\ntR.")
```
```sh
$ python 0.py 
hello world
```

> この例において、unpickler は os.system() 関数をインポートして、次に文字列の引数 "echo hello world" を適用しています。この例は無害ですが、システムを破壊する例を想像するのは難しくありません。

> この理由のため、Unpickler.find_class() をカスタマイズすることで非 pickle 化で何を得るかを制御したくなるかもしれません。その名前が示唆するのと異なり、Unpickler.find_class() はグローバル (クラスや関数) が必要とした時にはいつでも呼びだされます。したがって、グローバルを完全に禁止することも安全なサブセットに制限することも可能です。

> これは、一部の安全なクラスについてのみ builtins モジュールからロードすることを許可する unpickler の例です:

```python
import builtins
import io
import pickle

safe_builtins = {
    'range',
    'complex',
    'set',
    'frozenset',
    'slice',
}

class RestrictedUnpickler(pickle.Unpickler):

    def find_class(self, module, name):
        # Only allow safe classes from builtins.
        if module == "builtins" and name in safe_builtins:
            return getattr(builtins, name)
        # Forbid everything else.
        raise pickle.UnpicklingError("global '%s.%s' is forbidden" %
                                     (module, name))

def restricted_loads(s):
    """Helper function analogous to pickle.loads()."""
    return RestrictedUnpickler(io.BytesIO(s)).load()
```

この unpickler が働く使用例は次のように意図されます:


```python
>>> restricted_loads(pickle.dumps([1, 2, range(15)]))
[1, 2, range(0, 15)]
>>> restricted_loads(b"cos\nsystem\n(S'echo hello world'\ntR.")
Traceback (most recent call last):
  ...
pickle.UnpicklingError: global 'os.system' is forbidden
>>> restricted_loads(b'cbuiltins\neval\n'
...                  b'(S\'getattr(__import__("os"), "system")'
...                  b'("echo hello world")\'\ntR.')
Traceback (most recent call last):
  ...
pickle.UnpicklingError: global 'builtins.eval' is forbidden
```

> この例が示すように、非 pickle 化を認めるものに注意しなければなりません。したがって、セキュリティが重要な場合は xmlrpc.client の marshal API や、サードパーティのソリューションのような別の選択肢を考慮した方がよいでしょう。

## [12.1.7. 性能](https://docs.python.jp/3/library/pickle.html#performance)

> pickle プロトコルの最近のバージョン (プロトコル 2 以降) は一部の一般的な機能と組み込みデータ型を効率的にバイナリにエンコードするよう考慮されています。また、pickle モジュールは C 言語で書かれた透過的オプティマイザーを持っています。

## [12.1.8. 使用例](https://docs.python.jp/3/library/pickle.html#examples)

> 最も単純なコードでは、dump() および load() 関数を使用してください。

```python
import pickle

# An arbitrary collection of objects supported by pickle.
data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

with open('data.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
```

> 次の例は、pickle 化されたデータを読み込みます。

```python
import pickle

with open('data.pickle', 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    data = pickle.load(f)
```

### 参考

モジュール|概要
----------|----
[copyreg](https://docs.python.jp/3/library/copyreg.html#module-copyreg)|拡張型を登録するための Pickle インタフェース構成機構。
[pickletools](https://docs.python.jp/3/library/pickletools.html#module-pickletools)|pickle データの処理や分析を行うためのツール。
[shelve](https://docs.python.jp/3/library/shelve.html#module-shelve)|オブジェクトのインデクス付きデータベース; pickle を使います。
[copy](https://docs.python.jp/3/library/copy.html#module-copy)|オブジェクトの浅いコピーおよび深いコピー。
[marshal](https://docs.python.jp/3/library/marshal.html#module-marshal)|組み込み型の高性能な直列化。

