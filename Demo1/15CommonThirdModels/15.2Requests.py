from pip._vendor import requests
from pip._vendor.requests.packages import chardet

r = requests.get('http://www.douban.com', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})

print(r.status_code)
print(r.headers)
print(r.text)
# content属性获得bytes对象
print(r.content)



r2 = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r2.url)
print(r2.encoding)


r3 = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r3.json())
print(r3.json()['query']['created'])

# POST
# r4 = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
# 传递JSON数据
# params = {'key': 'value'}
# r = requests.post(url, json=params) # 内部自动序列化为JSON

# 上传文件,files参数
# upload_files = {'file': open('report.xls', 'rb')}
# >>> r = requests.post(url, files=upload_files)

# 在请求中传入Cookie，只需准备一个dict传入cookies参数：
# cs = {'token': '12345', 'status': 'working'}
# r = requests.get(url, cookies=cs)

# 要指定超时，传入以秒为单位的timeout参数：
# r = requests.get(url, timeout=2.5) # 2.5秒后超时


# chardet这个第三方库正好就派上了用场。用它来检测编码
print(chardet.detect(b'Hello, world!'))

data = '离离原上草，一岁一枯荣'.encode('utf-8')
print(data)
print(chardet.detect(data))
