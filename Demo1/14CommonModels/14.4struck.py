import struct

# struct模块来解决bytes和其他二进制数据类型的转换

# pack函数把任意数据类型变成bytes
print(struct.pack('>I', 10240099))

# unpack把bytes变成相应的数据类型
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

# 读入bmp前30个字节来分析
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(struct.unpack('<ccIIIIIIHH', s))