# coding=utf-8
__author__ = 'Main'

# 官方文档给出的关于编码的例子这里使用的时候会在运行的时候报错
# f = open("myfile.txt", "r", encoding="utf-8")

# 最基本的读取文件的方法

try:
    f = open('./abc.txt', 'r')
    for i in f.readlines():
        print i.strip() + "*"
    print f.read()
    print "-----------------"
    print f.readlines().__len__()
finally:
    if f:
        f.close()


# 使用python提供的with的方法，捕获异常

with open('./abc.txt','r') as f:
    for i in f.readlines():
        print i.strip()
    print f.read()
    print "------------------"


# 读取其他的非文本文件的时候，使用的是 rb

with open('./QRCode.png','rb') as f:
    print f.read()

