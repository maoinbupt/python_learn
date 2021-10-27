#!/usr/bin/env python3

import math


#内置函数
abs(-20)
max(1, 2)
int('123')


# 计算圆面积
def area_sum(i):
    area = math.pi * i * i
    print("面积为:" + str(area))

list1 = [10,20,30]
for i in list1:
    area_sum(i)



# 自定义function
def my_abs(i):
    if not isinstance(i,(float,int)):
        raise TypeError('must be int or float')
    if i>=0:
        return i
    else :
        return -i

print(my_abs(-3))

# 定义个空函数
def nope():
    pass

# 返回多个值
# 定义一个坐标位移函数
def move(x,y,step, angel=0):
    dx = x + step * math.cos(angel)
    dy = y - step * math.sin(angel)
    return dx,dy
x, y = move(100,100,60, math.pi/6)
#返回值是一个tuple
t1 = move(100,100,60, math.pi/6)
print(x, y)


# 默认参数n=2,可以不提供,
# 定义默认参数要牢记一点：默认参数必须指向不变对象
def power(x, n=2):
    s = 1
    while n>0:
        n = n-1
        s = s * x

    print(s)

power(2)

# 可变参数允许你传入0个或任意个参数，前面加*号
# 这些可变参数在函数调用时自动组装为一个tuple
def cal1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = (2,3,4)
print(cal1(1,2,3))
#允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
print(cal1(*nums))


# 关键字参数允许你传入0个或任意个含参数名的参数，
# 这些关键字参数在函数内部自动组装为一个dict
def person(name,age, **kw):
    print('name:',name, 'age:', age, 'others:', kw)

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Bob1', 35, city='Beijing')
person('Bob2', 36, city='Beijing', gender = 'M')
person('Bob3', 37, **extra)

# 限制关键字参数的名字，就可以用命名关键字参数
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person(name, age, *, city, job):
    print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')

'''
# 参数可以组合,但参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
'''
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


#递归函数
def fact(n):
    if n ==1:
        return 1
    return n * fact(n-1)

print(fact(5))
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
#尾递归,避免出现栈溢出的情况,但Python标准的解释器没有针对尾递归做优化
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1, num * product)

def fact2(n):
    return fact_iter(n,1)

print(fact2(5))