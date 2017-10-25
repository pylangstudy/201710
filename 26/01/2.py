import dbm
#import dbm.gnu#ModuleNotFoundError: No module named '_gdbm'
import dbm.dumb
with dbm.dumb.open('cache_gnu', 'c') as db:#AttributeError: module 'dbm' has no attribute 'dumb'
    db[b'hello'] = b'there'
    db['www.python.org'] = 'Python Website'
    db['www.cnn.com'] = 'Cable News Network'
    assert db[b'www.python.org'] == b'Python Website'
    assert db['www.cnn.com'] == b'Cable News Network'
    print(db.get('python.org', b'not present'))
#    db['www.yahoo.com'] = 4

    print(db)
    for k in db: print(k, db[k])
