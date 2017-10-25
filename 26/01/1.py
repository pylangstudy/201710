import dbm
#import dbm.gnu#ModuleNotFoundError: No module named '_gdbm'

with dbm.gnu.open('cache_gnu', 'c') as db:#AttributeError: module 'dbm' has no attribute 'gnu'
    db[b'hello'] = b'there'
    db['www.python.org'] = 'Python Website'
    db['www.cnn.com'] = 'Cable News Network'
    assert db[b'www.python.org'] == b'Python Website'
    assert db['www.cnn.com'] == b'Cable News Network'
    print(db.get('python.org', b'not present'))
#    db['www.yahoo.com'] = 4

    print(db.firstkey())
    k = db.firstkey()
    while k != None:
        print(k)
        k = db.nextkey(k)

    #大量の削除を実行した後、gdbm ファイルの占めるスペースを削減したい場合、このルーチンはデータベースを再組織化します。
#    db.reorganize()
