# [9.4. decimal — 十進固定及び浮動小数点数の算術演算](https://docs.python.jp/3/library/decimal.html#module-decimal)

< [9. 数値と数学モジュール](https://docs.python.jp/3/library/numeric.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/decimal.py](https://github.com/python/cpython/tree/3.6/Lib/decimal.py)

## [9.4.4. 定数](https://docs.python.jp/3/library/decimal.html#constants)

> この節の定数は C モジュールにのみ意味があります。互換性のために、pure Python 版も含まれます。

属性|32bit|64-bit
----|-----|------
decimal.MAX_PREC|425000000|999999999999999999
decimal.MAX_EMAX|425000000|999999999999999999
decimal.MIN_EMIN|-425000000|-999999999999999999
decimal.MIN_ETINY|-849999999|-1999999999999999997

* decimal.HAVE_THREADS

> デフォルト値は True です。Python がスレッド無しでコンパイルされている場合、C 版は自動的にコストがかかるスレッドローカルなコンテキスト機構を使用不可にします。この場合、値は False です。

## [9.4.5. 丸めモード](https://docs.python.jp/3/library/decimal.html#rounding-modes)

属性|説明
----|----
decimal.ROUND_CEILING|Infinity 方向に丸めます。
decimal.ROUND_DOWN|ゼロ方向に丸めます。
decimal.ROUND_FLOOR|-Infinity 方向に丸めます。
decimal.ROUND_HALF_DOWN|近い方に、引き分けはゼロ方向に向けて丸めます。
decimal.ROUND_HALF_EVEN|近い方に、引き分けは偶数整数方向に向けて丸めます。
decimal.ROUND_HALF_UP|近い方に、引き分けはゼロから遠い方向に向けて丸めます。
decimal.ROUND_UP|ゼロから遠い方向に丸めます。
decimal.ROUND_05UP|ゼロ方向に丸めた後の最後の桁が 0 または 5 ならばゼロから遠い方向に、そうでなければゼロ方向に丸めます。

## [9.4.6. シグナル](https://docs.python.jp/3/library/decimal.html#signals)

> シグナルは、計算中に生じた様々なエラー条件を表現します。各々のシグナルは一つのコンテキストフラグと一つのトラップイネーブラに対応しています。

> コンテキストフラグは、該当するエラー条件に遭遇するたびにセットされます。演算後にフラグを調べれば、演算に関する情報 (例えば計算が厳密だったかどうか) がわかります。フラグを調べたら、次の計算を始める前にフラグを全てクリアするようにしてください。

> あるコンテキストのトラップイネーブラがあるシグナルに対してセットされている場合、該当するエラー条件が生じると Python の例外を送出します。例えば、 DivisionByZero が設定されていると、エラー条件が生じた際に DivisionByZero 例外を送出します。

属性|説明
----|----
class decimal.Clamped|値の表現上の制限に沿わせるために指数部が変更されたことを通知します。
class decimal.DecimalException|他のシグナルの基底クラスで、 ArithmeticError のサブクラスです。
class decimal.DivisionByZero|有限値をゼロで除算したときのシグナルです。
class decimal.Inexact|値の丸めによって演算結果から厳密さが失われたことを通知します。
class decimal.InvalidOperation|無効な演算が実行されたことを通知します。
class decimal.Overflow|数値オーバフローを示すシグナルです。
class decimal.Rounded|情報が全く失われていない場合も含み、値丸めが起きたときのシグナルです。
class decimal.Subnormal|値丸めを行う前に指数部が Emin より小さかったことを示すシグナルです。
class decimal.Underflow|演算結果が値丸めによってゼロになった場合に生じる数値アンダフローです。
class decimal.FloatOperation|float と Decimal の混合の厳密なセマンティクスを有効にします。

