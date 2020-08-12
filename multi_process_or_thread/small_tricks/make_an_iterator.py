import time
from collections import Iterable
from collections import Iterator

class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """一个类的对象想要成为可迭代的，那么必须实现此方法"""
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration

classmate = Classmate()
classmate.add("student 1")
classmate.add("student 2")
classmate.add("student 3")

for name in classmate:
    print(name)
