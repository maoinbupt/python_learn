class Student(object):
    # 类属性,类的所有实例都可以访问到
    class_name = 'gaofeng'

    def __init__(self, name, score):
        # 实例属性
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score

    def print_score(self):
        print('%s : %s ' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('bart', 100)
bart.set_score(99)
bart.print_score()
print(bart.get_grade())

print(type(bart))
print(isinstance(bart, Student))

# 获得一个对象的所有属性和方法
print(dir('ABC'))
# __xxx__的属性和方法的特殊用途: 在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的: len('ABC') = 'ABC'.__len__()
# getattr()、setattr()以及hasattr() 类似反射

