# coding=utf-8
__author__ = 'Main'

import os

print os.name
print os.curdir
print os.defpath    #
print os.environ    # 所有的环境变量
print os.environ['PATH']   # 环境变量中PATH的内容为
print os.path.abspath('.') # 当前目录的绝对路径
print(os.path.split(os.path.abspath('.'))) # 拆分文件的目录的路径的正确的方法
print(os.path.join(os.path.abspath('.'),"abc"))

# 创建文件夹的方法
# os.mkdir('/Users/michael/testdir')
# 删除文件夹的方法
# os.rmdir('/Users/michael/testdir')
# 重命名文件
# os.rename('test.txt', 'test.py')
# 删除文件
# os.remove('test.py')



