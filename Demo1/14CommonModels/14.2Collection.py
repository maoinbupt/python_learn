from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

p = (1, 2)
print(p)
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
Point = namedtuple('Point', ['x', 'y'])
# Circle = namedtuple('Circle', ['x', 'y', 'r'])
p = Point(1, 2)
print(p.x)
print(p.y)
print(isinstance(p, tuple))

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
q = deque(['a', 'b', 'c'])
q.append('y')
q.appendleft('x')  # popleft
print(q)

# 如果希望key不存在时，返回一个默认值，就可以用defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'aaaaaa'
print(dd['key1'])
print(dd['key2'])

# OrderedDict的Key是有序的
# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)


# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


fifod = LastUpdatedOrderedDict(3)
fifod['a'] = 'a'
fifod['b'] = 'b'
fifod['c'] = 'c'
fifod['d'] = 'd'
print(fifod)

# Counter是一个简单的计数器，例如，统计字符出现的个数
c = Counter()
for ch in 'Programming':
    c[ch] = c[ch] + 1
print(c)