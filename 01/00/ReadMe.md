# [9.4. decimal — 十進固定及び浮動小数点数の算術演算](https://docs.python.jp/3/library/decimal.html#module-decimal)

< [9. 数値と数学モジュール](https://docs.python.jp/3/library/numeric.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/decimal.py](https://github.com/python/cpython/tree/3.6/Lib/decimal.py)

## [9.4.2.1. 論理引数](https://docs.python.jp/3/library/decimal.html#logical-operands)

論理引数 とは Decimal インスタンスで指数と符号は共にゼロであり、各桁の数字が 0 か 1 であるものです。

* logical_and()
* logical_invert()
* logical_or()
* logical_xor()

## [9.4.3. Context オブジェクト](https://docs.python.jp/3/library/decimal.html#context-objects)

> コンテキスト (context) とは、算術演算における環境設定です。コンテキストは計算精度を決定し、値丸めの方法を設定し、シグナルのどれが例外になるかを決め、指数の範囲を制限しています。

> 多重スレッドで処理を行う場合には各スレッドごとに現在のコンテキストがあり、 getcontext() や setcontext() といった関数でアクセスしたり設定変更できます:

属性|説明
----|----
decimal.getcontext()|アクティブなスレッドの現在のコンテキストを返します。
decimal.setcontext(c)|アクティブなスレッドのコンテキストを c に設定します。
decimal.localcontext(ctx=None)|with 文の入口でアクティブなスレッドのコンテキストを ctx のコピーに設定し、with 文を抜ける時に元のコンテキストに復旧する、コンテキストマネージャを返します。コンテキストが指定されなければ、現在のコンテキストのコピーが使われます。
class decimal.BasicContext|汎用十進演算仕様で定義されている標準コンテキストの一つです。精度は 9 桁に設定されています。丸め規則は ROUND_HALF_UP です。すべての演算結果フラグはクリアされています。 Inexact, Rounded, Subnormal を除く全ての演算エラートラップが有効 (例外として扱う) になっています。
class decimal.ExtendedContext|汎用十進演算仕様で定義されている標準コンテキストの一つです。精度は 9 桁に設定されています。丸め規則は ROUND_HALF_EVEN です。すべての演算結果フラグはクリアされています。トラップは全て無効(演算中に一切例外を送出しない) になっています。
class decimal.DefaultContext|Context コンストラクタが新たなコンテキストを作成するさいに雛形にするコンテキストです。このコンテキストのフィールド (精度の設定など) を変更すると、 Context コンストラクタが生成する新たなコンテキストに影響を及ぼします。
clear_flags()|フラグを全て 0 にリセットします。
clear_traps()|トラップを全て 0 にリセットします。
copy()|コンテキストの複製を返します。
copy_decimal(num)|Decimal インスタンス num のコピーを返します。
create_decimal(num)|self をコンテキストとする新たな Decimal インスタンスを num から生成します。 Decimal コンストラクタと違い、数値を変換する際にコンテキストの精度、値丸め方法、フラグ、トラップを適用します。
create_decimal_from_float(f)|浮動小数点数 f から新しい Decimal インスタンスを生成しますが、 self をコンテキストとして丸めます。 Decimal.from_float() クラスメソッドとは違い、変換にコンテキストの精度、丸めメソッド、フラグ、そしてトラップが適用されます。
Etiny()|Emin - prec + 1 に等しい値を返します。演算結果の劣化が起こる桁の最小値です。アンダーフローが起きた場合、指数は Etiny に設定されます。
Etop()|Emax - prec + 1 に等しい値を返します。
abs(x)|x の絶対値を返します。
add(x, y)|x と y の和を返します。
canonical(x)|同じ Decimal オブジェクト x を返します。
compare(x, y)|x と y を数値として比較します。
compare_signal(x, y)|二つの演算対象の値を数値として比較します。
compare_total(x, y)|二つの演算対象を抽象的な表現を使って比較します。
compare_total_mag(x, y)|二つの演算対象を抽象的な表現を使い符号を無視して比較します。
copy_abs(x)|x のコピーの符号を 0 にセットして返します。
copy_negate(x)|x のコピーの符号を反転して返します。
copy_sign(x, y)|y から x に符号をコピーします。
divide(x, y)|x を y で除算した値を返します。
divide_int(x, y)|x を y で除算した値を整数に切り捨てて返します。
divmod(x, y)|二つの数値間の除算を行い、結果の整数部を返します。
exp(x)|e ** x を返します。
fma(x, y, z)|x を y 倍したものに z を加えて返します。
is_canonical(x)|x が標準的(canonical)ならば True を返します。そうでなければ False です。
is_finite(x)|x が有限ならば True を返します。そうでなければ False です。
is_infinite(x)|x が無限ならば True を返します。そうでなければ False です。
is_nan(x)|x が qNaN か sNaN であれば True を返します。そうでなければ False です。
is_normal(x)|x が通常の数ならば True を返します。そうでなければ False です。
is_qnan(x)|x が無言 NaN であれば True を返します。そうでなければ False です。
is_signed(x)|x が負の数であれば True を返します。そうでなければ False です。
is_snan(x)|x が発信 NaN であれば True を返します。そうでなければ False です。
is_subnormal(x)|x が非正規数であれば True を返します。そうでなければ False です。
is_zero(x)|x がゼロであれば True を返します。そうでなければ False です。
ln(x)|x の自然対数(底 e の対数)を返します。
log10(x)|x の底 10 の対数を返します。
logb(x)|演算対象の MSD の大きさの指数部を返します。
logical_and(x, y)|それぞれの桁に論理演算 and を当てはめます。
logical_invert(x)|x の全ての桁を反転させます。
logical_or(x, y)|それぞれの桁に論理演算 or を当てはめます。
logical_xor(x, y)|それぞれの桁に論理演算 xor を当てはめます。
max(x, y)|二つの値を数値として比較し、大きいほうを返します。
max_mag(x, y)|値を符号を無視して数値として比較します。
min(x, y)|二つの値を数値として比較し、小さいほうを返します。
min_mag(x, y)|値を符号を無視して数値として比較します。
minus(x)|Python における単項マイナス演算子に対応する演算です。
multiply(x, y)|x と y の積を返します。
next_minus(x)|x より小さい最大の表現可能な数を返します。
next_plus(x)|x より大きい最小の表現可能な数を返します。
next_toward(x, y)|x に y の方向に向かって最も近い数を返します。
normalize(x)|x をもっとも単純な形にします。
number_class(x)|x のクラスを指し示すものを返します。
plus(x)|Python における単項のプラス演算子に対応する演算です。コンテキストにおける精度や値丸めを適用するので、等値 (identity) 演算とは 違います。
power(x, y, modulo=None)|x の y 乗を計算します。modulo が指定されていればモジュロを取ります。
quantize(x, y)|x に値丸めを適用し、指数を y にした値を返します。
radix()|単に 10 を返します。何せ十進ですから :)
remainder(x, y)|整数除算の剰余を返します。
remainder_near(x, y)|x - y * n を返します。ここで n は x / y の正確な値に一番近い整数です (この結果が 0 ならばその符号は x の符号と同じです)。
rotate(x, y)|x の y 回巡回したコピーを返します。
same_quantum(x, y)|2つの演算対象が同じ指数を持っている場合に True を返します。
scaleb(x, y)|一つめの演算対象の指数部に二つめの値を加えたものを返します。
shift(x, y)|x を y 回シフトしたコピーを返します。
sqrt(x)|x の平方根を精度いっぱいまで求めます。
subtract(x, y)|x と y の間の差を返します。
to_eng_string(x)|文字列に変換します。指数が必要なら工学表記が使われます。
to_integral_exact(x)|最近傍の整数に値を丸めます。
to_sci_string(x)|数値を科学表記で文字列に変換します。

