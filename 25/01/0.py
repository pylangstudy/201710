#!python3.6
#encoding:utf-8
import shelve
with shelve.open('spam') as db:
    db['eggs'] = 'eggs'
    db['日本語'] = '値'
    print(db)
    print(db['eggs'])
    print(db['日本語'])
