# coding=utf-8
__author__ = 'Main'

import sys
import os
import logging

logging.basicConfig(level = logging.INFO)

def search(abs_path, arg):
    # 消除开头的原始目录绝对路径（包括分隔符）
    abs_len = len(abs_path) + 1
    for f in os.listdir('.'):
        if os.path.isfile(f):
            if f.find(arg) >= 0:
                abs_path_of_f = os.path.abspath(f)
                print abs_path_of_f[abs_len:]
        elif os.path.isdir(f):
            os.chdir(f)
            search(abs_path, arg)
            os.chdir('..')

if __name__ == '__main__':
    args = sys.argv
    print u'输入参数为：%s' % str(args)
    if len(args) != 2:
        logging.error(u'输入参数错误！')
    else:
        arg = args[1]
        print 'Searching for %s...' % arg
        print '------------------------'
        abs_path = os.path.abspath('.')
        search(abs_path, arg)
        print '------------------------'
        print 'End.'