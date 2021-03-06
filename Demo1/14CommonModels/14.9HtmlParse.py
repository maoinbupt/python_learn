from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print('data:' +data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('entityref: &%s;' % name)

    def handle_charref(self, name):
        print('charref: &#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

print('---------------------')

from html.parser import HTMLParser
from urllib import request
import re

class MyHTMLParser(HTMLParser):
    flag = 0
    res = []
    is_get_data = 0

    def handle_starttag(self, tag, attrs):
        # 首先找到包裹事件的元素
        if tag == 'ul':
            for attr in attrs:
                if re.match(r'list-recent-events', attr[1]):
                    self.flag = 1

        # 处理包裹事件名称的a元素
        if tag == 'a' and self.flag == 1:
            self.is_get_data = 'title'

        # 处理时间的time元素
        if tag == 'time' and self.flag == 1:
            self.is_get_data = 'time'

        # 处理包裹地点的time元素
        if tag == 'span' and self.flag == 1:
            self.is_get_data = 'addr'

    def handle_endtag(self, tag):
        if self.flag == 1 and tag == 'ul':
            self.flag = 0

    # res是一个list，存储所有会议
    # list的元素是dict
    # 每个dict表示一个会议
    #
    # 获得title, 即会议名时，给res添加一个新dict：
    # self.res.append({self.is_get_data: data})
    # res由[]变为[{'title': 'PyCascades 2018'}]
    #
    # 获得addr，time这样的其它属性时, 先把最后一个dict（即当前处理的dict）取出：
    # 即self.res[len(self.res) - 1]
    # 再把新属性加入：
    # self.res[len(self.res) - 1][self.is_get_data] = data
    # [{'title': 'PyCascades 2018', 'time': '22 Jan. – 24 Jan.'}]
    def handle_data(self, data):
        if self.is_get_data and self.flag == 1:
            if self.is_get_data == 'title':
                self.res.append({self.is_get_data: data})
            else:
                self.res[len(self.res) - 1][self.is_get_data] = data
            self.is_get_data = None


parser = MyHTMLParser()

with request.urlopen('https://www.python.org/events/python-events/') as f:
    data = f.read().decode('utf-8')

parser.feed(data)
for item in MyHTMLParser.res:
    print('---------------')
    for k,v in item.items():
        print("%s : %s" % (k,v))