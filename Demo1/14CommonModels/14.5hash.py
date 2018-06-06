import hashlib
import hmac

md51 = hashlib.md5()
md51.update('how to use md5 in python hashlib?'.encode('utf-8'))

# 数据量很大，可以分块多次调用update()，最后计算的结果是一样
md52 = hashlib.md5()
md52.update('how to use md5 in '.encode('utf-8'))
md52.update('python hashlib?'.encode('utf-8'))

print(md51.hexdigest())
print(md52.hexdigest())

# 通常我们计算MD5时采用md5(message + salt)
# Hmac算法：Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中
message = b'Hello, world!'
key = b'secrite'
h = hmac.new(key,message, digestmod='MD5')
print(h.hexdigest())