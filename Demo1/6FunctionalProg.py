#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import builtins

# 1.高阶函数
f = abs
print(f(-3))


def add(a, b, f):
    return f(a) + f(b)


print(add(-3, -4, abs))


# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f1(x):
    return x * x


r = map(f1, [1, 2, 3, 4, 5])
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce


def combineNum(x, y):
    return y + x * 10


print(reduce(combineNum, [1, 2, 3, 4, 5]))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2nums(s):
    return DIGITS[s]

def str2num(s):
    return reduce(combineNum, map(char2nums, s))

print(str2num('123456'))


# filter()函数用于过滤序列,filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# sorted函数 它还可以接收一个key函数来实现自定义的排序
print(sorted([36, 5, -12, 9, -21], key=abs))


# 2.返回函数,返回的函数并没有立刻执行，而是直到调用了f()才执行
def lazy_sum(*args):
    def sum():
        x = 0
        for n in args:
            x = x + n
        return x

    return sum


f3 = lazy_sum(1, 3, 5)
print(f3)
print(f3())

# 3.匿名函数
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))

# 4.装饰器.代码运行期间动态增加功能的方式，称之为“装饰器”
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wapper(*args, **kwargs):
            print('%s function %s():' % (text, func.__name__))
            return func(*args, **kwargs)

        return wapper

    return decorator

# 相当于 log(now)
@log('call')
def now():
    print('20170104')

now()


# 5.偏函数
# 通过设定参数的默认值，可以降低函数调用的难度
# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
int2 = functools.partial(int, base = 2)

print(int2('10000'))
# 16

