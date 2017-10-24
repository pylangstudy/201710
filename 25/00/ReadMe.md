# [12.2. copyreg — pickle サポート関数を登録する](https://docs.python.jp/3/library/copyreg.html)

< [12. データの永続化](https://docs.python.jp/3/library/persistence.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/copyreg.py](https://github.com/python/cpython/tree/3.6/Lib/copyreg.py)

> copyreg モジュールは、特定のオブジェクトを pickle する際に使われる関数を定義する手段を提供します。 pickle モジュールと copy モジュールは、オブジェクトを pickle/コピーする場合にそれらの関数を使用します。このモジュールは、クラスでないオブジェクトコンストラクタに関する設定情報を提供します。そのようなコンストラクタは、ファクトリ関数か、クラスインスタンスかもしれません。

属性|概要
----|----
copyreg.constructor(object)|object を有効なコンストラクタであると宣言します。 object が呼び出し可能でなければ(したがってコンストラクタとして有効でなければ)、 TypeError を発生します。
copyreg.pickle(type, function, constructor=None)|function が型 type のオブジェクトに対する"リダクション"関数として使われるように宣言します。function は文字列か、2要素または3要素を含んだタプルを返さなければなりません。

## [12.2.1. 使用例](https://docs.python.jp/3/library/copyreg.html#example)

> 下記の例は、pickle 関数を登録する方法と、それがどのように使用されるかを示そうとしています:

```python
import copyreg, copy, pickle
class C(object):
    def __init__(self, a):
        self.a = a
def pickle_c(c):
    print("pickling a C instance...")
    return C, (c.a,)

copyreg.pickle(C, pickle_c)
c = C(1)
d = copy.copy(c)
#pickling a C instance...
p = pickle.dumps(c)
#pickling a C instance...
```
```sh
$ python 0.py 
pickling a C instance...
pickling a C instance...
```
