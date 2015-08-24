# coding=utf-8
__author__ = 'Main'

f = open('./abc.txt', 'r')
for i in f.readlines():
    print i.strip() + "*"
print f.read()
print "-----------------"
print f.readlines().__len__()

f.close()
