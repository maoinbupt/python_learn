
# 文件读写
import shutil

try:
    f = open('/Users/reamongao/git/python/Demo1/iotest.txt', 'r') #
    print(f.read())
finally:
    f.close()

# 等同于上面的语句
with open('/Users/reamongao/git/python/Demo1/iotest.txt', 'r') as f:
    print(f.read())



# 内存中读写数据
from io import StringIO, BytesIO

f = StringIO()
f.write('Hello ')
f.write('World!2')
print(f.getvalue())

f2 = StringIO('Hello! \nGoodBye! \n')
while True:
    s = f2.readline()
    if s == '':
        break
    print(s)

b = BytesIO()
b.write('中文'.encode('utf-8'))
print(b.getvalue())

b2 = BytesIO(b.getvalue())
print(b2.read())

# 调用操作系统的接口命令
import os
print(os.uname())
print(os.environ)
print(os.environ.get('PATH'))
# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# 要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符,同理os.path.split()拆分路径
# os.mkdir(os.path.join('/Users/reamongao/git/python/Demo1', 'testDir'))
# os.rmdir('/Users/reamongao/git/python/Demo1/testDir')
print(os.path.splitext('/Users/reamongao/git/python/Demo1/iotest.txt'))

# os.rename('iotest.txt', 'iotest.py')
# os.remove('iotest.py')

shutil.copyfile('iotest.txt', 'iotest.py')

# 列出当前目录文件夹
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列出所以py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

# 序列化和反序列化
import pickle

d = dict(name = 'reamon', age = 20, sex = 'male')
f = open('dump', 'wb')
pickle.dump(d, f)
f.close()

f2 = open('dump', 'rb')
d2 = pickle.load(f2)

print(d2)

print('----------')
import json
json_str = json.dumps(d)
print(json_str)

print(json.loads(json_str))


# 一般的类转json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


# 这个方法使得对象转为dict,就可以json转了
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))

# json转为实例
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
print(json.loads(json_str, object_hook=dict2student))

