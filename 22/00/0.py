import pickle
print('pickle.HIGHEST_PROTOCOL:', pickle.HIGHEST_PROTOCOL)
print('pickle.DEFAULT_PROTOCOL:', pickle.DEFAULT_PROTOCOL)

class Human:
    class_var = 0
    def __init__(self):
        self.ins_var = 1
    def ins_method(self):
        print('ins_method')

with open('Human.pickle', 'wb') as f:
    pickle.dump(Human(), f, protocol=4)
print(pickle.dumps(Human(), protocol=4))

with open('Human.pickle', 'rb') as f:
    ins = pickle.load(f, encoding='UTF-8')
    print(ins)
    print(dir(ins))
    print(ins.class_var)
    print(ins.ins_var)
    ins.ins_method()
#    print(pickle.loads(f.read(), encoding='UTF-8'))#EOFError: Ran out of input

with open('Human.pickler', 'wb') as f:
    p = pickle.Pickler(f, protocol=4)
    h = Human()
    p.dump(h)
#    print(p.persistent_id(h))#AttributeError: persistent_id
#    print(p.dispatch_table)#AttributeError: dispatch_table
#    print(pickle.Pickler.persistent_id(h))#TypeError: 'getset_descriptor' object is not callable
    print(pickle.Pickler.dispatch_table)
with open('Human.pickler', 'rb') as f:
    p = pickle.Unpickler(f, encoding='UTF-8')
    ins = p.load()
    print(ins)
#    print(dir(ins))
    print(ins.class_var)
    print(ins.ins_var)
    ins.ins_method()
    #p.persistent_load(pid)
    #p.find_class(module, name)

