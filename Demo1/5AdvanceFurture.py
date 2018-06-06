
# 1.切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[:5])
print(L[0:5:2])
print('ABCDEFG'[:3])

# 2.迭代

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
     print(key)

# 3.列表生成式
print([x * x for x in range(1, 11) if x % 2 == 0])

import os
print([d for d in os.listdir('.')])

# 4.列表生成器,一边循环一边计算的机制，称为生成器：generator
g = (x * x for x in range(1,5))
for n in g:
    print(n)
# 斐波拉切函数,定义generator的另一种方法
def fib(max):
    n,a,b,= 0,0,1
    while(n<max):
        yield b
        a,b = b, a+b
        n = n +1
    return "Done"
g2 = fib(6)
for n in g2:
    print(n)


# 5迭代器
# 凡是可作用于for循环的对象都是Iterable类型
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
from collections import Iterable
from collections import Iterator

"""
 key words of comments 
"""
print(isinstance([], Iterable))

print(isinstance((x for x in range(0, 10)), Iterator))
