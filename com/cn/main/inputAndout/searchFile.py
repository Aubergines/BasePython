# coding=utf-8
__author__ = 'Main'

# 查找出给定的目录中的包含指定的字符串的文件，打印该文件的绝对路径

import os

class searchFile(object):

    def searchF(self,p):
        for x in os.listdir(p):
            print x.lower()+"--file--"
            print os.path.isfile(x)
            print x.lower()+"--dir --"
            print os.path.isdir(x)
            if os.path.isfile(x) and x.lower().__contains__("ab"):
                print x
            elif os.path.isdir(x):
                self.searchF(x)

my = searchFile()
my.searchF("D:\\pythonspace")