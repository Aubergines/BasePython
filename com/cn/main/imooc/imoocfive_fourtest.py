# coding=utf-8
__author__ = 'Main'
import json


class Student(object):

    def __init__(self, name):
        self.name = name

    def read(self):
        print("我的名字是:" + self.name)
        return r'["Tim", "Bob", "Alice"]'

s = Student("XiaoMing")

print json.load(s)