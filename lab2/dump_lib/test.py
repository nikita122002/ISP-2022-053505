from dump_library.parsers.parser import Parser
from dump_library.parsers.json.json import Json
from dump_library.parsers.yaml.yaml import Yaml
from dump_library.parsers.toml.toml import Toml
from dump_library.dump_service import load, loads, dump, dumps
import inspect
import math

class InnerClass(object):
    qwe = "qwe"


class ParentClass(object):
    def __init__(self):
        self.vint = 123

    v_qwe = InnerClass()
    v_int = 1
    v_float = 1.23
    v_bool = True
    v_tuple = (1, 2, 3)
    v_dict = {'1': 1, '2': 2, '3': 3, '4': 4}
    v_list = [1, [1, 'fsdsd', True], 3, 4, InnerClass]


class ChildClass(ParentClass):
    vstr = "1234567890"
    vint = 1

    def insert_in_method(self, k: int, f):
        self.insert_in_function(k + self.vint, f)

    def insert_in_function(self, k: int, f):
        return f(k + function(1))


def function(a: int):
    return a ** a


test_dict = {
    'v_int': 1,
    'v_float': 1.23,
    'v_bool': True,
    'v_tuple': (1, 2, 3),
    'v_dict': {'1': 1, '2': 2, '3': 3, '4': 4},
    'v_list': [1, [1, 'fsdsd', True], 3, 4]
}

b = Parser()
par = json()
t2 = ChildClass()
dub = b.dump(t2)
aa = t2.insert_in_function.__code__
gl = globals()
s = par.serialization(dub.data, 'Parser_Data')
ss = par.deserialization(s)
k = dub.dump(ss).load()
pass


def abc():
    c = 42


    def f(x):
        a = 123
        return math.sin(x * a * c)
    Json().dump(abc)


pass
