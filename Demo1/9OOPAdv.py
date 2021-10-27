from socketserver import TCPServer, ForkingMixIn


class Student(object):
    # __slots__变量，来限制该class实例能添加的属性
    # __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

    # getter方法变成属性
    @property
    def score(self):
        return self._score

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # 负责把一个setter方法变成属性赋值
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    # 类似toString
    def __str__(self):
        return 'Student object name %s' % self._name

    # __call__()方法，就可以直接对实例进行调用,判断一个对象是否能被调用:callable(s)
    def __call__(self, *args, **kwargs):
        return 'call : my name is %s ' % self._name


s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'
s.score = 99  # 绑定属性'score'

print(s.name)
print(s.age)
print(s.score)
print(s)
print(s())
print(callable(s))


# 多重继承

class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Runnable(object):
    def run(self):
        print('Running ......')


class Dog(Mammal, Runnable):
    pass


class MyTCPServer(TCPServer, ForkingMixIn):
    pass


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    # 实现这个方法使得类可以迭代
    def __iter__(self):
        return self

    # 然后,for循环不断读取类的next方法
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if (self.a > 10):
            raise StopIteration()
        return self.a

    # 按照下标取出元素
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

#实现一个__iter__()方法，该方法返回一个迭代对象
for n in Fib():
    print(n)
# list那样按照下标取出元素，需要实现__getitem__()方法：
print(Fib()[3])

# 动态返回属性实现链式调用
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    # __getattr__()方法，动态返回一个属性, 返回函数也是完全可以的
    def __getattr__(self, item):
        return Chain('%s/%s' % (self._path, item))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain('api.domaintest.com').video.info.list)

'使用枚举类'
from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May'))
Month.Jan
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
    #value属性则是自动赋给成员的int常量，默认从1开始计数。

# 可以从Enum派生出自定义类
# 保证没有重复值
@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tus = 2
    Wed = 3
Weekday.Sun.value

print(type(Student))
print(type(s))


def funHello(self, name='world'):
    print('Hello %s' % name)

#type()函数既可以返回一个对象的类型，又可以创建出新的类型
# 创建Hello.class
#1.class的名称；
#2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
Hello = type('Hello', (object,), dict(hello=funHello))

h = Hello()
h.hello()
