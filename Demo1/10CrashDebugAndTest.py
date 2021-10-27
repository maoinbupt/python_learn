import logging

logging.basicConfig(level=logging.INFO)

# 异常处理
try:
    print('try:')
    r = 10 / 1
    # debug
    print('result : ', r)
    # assert n != 0, 'n is zero!'
    logging.info('r = %d' % r)


except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('except : ', e)
    logging.exception(e)
else:
    print('no error!')
finally:
    print('finally ---')
print('END')


# unit test
# 下面的注释为"文档测试”（doctest）
# 执行测试: python -m unittest 10CrashDebugAndTest
class Dict(dict):
    '''
        Simple dict but also support access as x.y style.

        >>> d1 = Dict()
        >>> d1['x'] = 100
        >>> d1.x
        100
        >>> d1.y = 200
        >>> d1['y']
        200
        >>> d2 = Dict(a=1, b=2, c='3')
        >>> d2.c
        '3'
        >>> d2['empty']
        Traceback (most recent call last):
            ...
        KeyError: 'empty'
        >>> d2.empty
        Traceback (most recent call last):
            ...
        AttributeError: 'Dict' object has no attribute 'empty'
        '''
    def __init__(self, **kw):
        super().__init__(**kw)

    # 注释掉这个方法,文档测试就会报错
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


import unittest

# 测试类，从unittest.TestCase继承
class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
        print('test_init')

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    # 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    # 这两个方法会分别在每调用一个测试方法的前后分别被执行
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    # 运行单元测试
    # 方法2: python3 -m unittest 10CrashDebugAndTest
    if __name__ == '__main__':
        unittest.main()

import re