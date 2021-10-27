import itertools

natuals = itertools.count(1)
# 无限
# for c in natuals:
#     print(c)

cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
    # for c in cs:
    #     print(c)

nsr = itertools.repeat('A', 3)
for n in nsr:
    print(n)

# takewhile()等函数根据条件判断来截取出一个有限的序列
ns = itertools.takewhile(lambda x: x<10, natuals)
print(list(ns))

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

print('-------------------')
# 就可以让元素'A'和'a'都返回相同的key
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))