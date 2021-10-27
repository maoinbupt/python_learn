# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import numpy
import sys

numpy.abs(-1)
# 模块搜索路径
print(sys.path)



def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

#运行测试用
if __name__ == '__main__':
    test()

#mycompany
# ├─ __init__.py
# ├─ abc.py
# └─ xyz.py
# 引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，abc.py模块的名字就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz。


#类似_xxx和__xxx这样的函数或变量就是非公开的（private）
#类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途

