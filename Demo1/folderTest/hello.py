#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'reamongao'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# private function
def _private_func1(name):
    return 'hello %s' % name

if __name__ == '__main__':
    test()
