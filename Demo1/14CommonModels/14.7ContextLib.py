from contextlib import contextmanager, closing
from urllib.request import urlopen

# 要想使用with xxxx() as x:这种格式，可以用@contextmanager 装饰一个生成器xxxx() 这个生成器里包含相关的上下文处理

#
# try:
#     f = open('/path/to/file', 'r')
#     f.read()
# finally:
#     if f:
#         f.close()

# with语句允许我们非常方便地使用资源，而不必担心资源没有关闭
# 任何对象，只要正确实现了上下文管理，就可以用于with语句

# with open('/path/to/file', 'r') as f:
#     f.read()

# 实现上下文管理是通过__enter__和__exit__这两个方法实现的
class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)


with Query('Bob') as q:
    q.query()

print('----------------')


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query2 info about %s...' % self.name)


# contextlib提供了更简单的写法
# @contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去
@contextmanager
def create_query(name):
    print('Begin2')
    q = Query(name)
    yield q
    print('End2')


with create_query('Bob') as q:
    q.query()

print('---------------------')


# 很多时候，我们希望在某段代码执行前后自动执行特定代码
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("hello")
    print("world")

print('---------------------')

# 以用closing()来把该对象变为上下文对象,它的作用就是把任意对象变为上下文对象，并支持with语句
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
