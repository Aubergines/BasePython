# coding=utf-8
__author__ = 'Main'

# 自定义的比较函数

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)
    __repr__ = __str__

    def __cmp__(self, s):
        if self.score < s.score:
            return 1
        elif self.score > s.score:
            return -1
        else:
            if self.name > s.name:
                return 1
            elif self.name < s.name:
                return -1
            else:
                return 0

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print sorted(L)
