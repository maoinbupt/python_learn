import base64

# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
result = base64.b64encode(b'binary\x00string')
print(result)
source = base64.b64decode(result)
print(source)

