# coding=utf-8
__author__ = 'Main'

# 定义属性的快捷方式   a,b,c,d = 0,1,2,3
#       a = 0
#       b = 1
#       c = 2
#       d = 3

class Fib(object):
    def __init__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            c = a
            a = b
            b = c + a
        self.numbers = L

    def __str__(self):
        return str(self.numbers)

    __repr__ = __str__

    def __len__(self):
        return len(self.numbers)

f = Fib(10)
print f
print len(f)
