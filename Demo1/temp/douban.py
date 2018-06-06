# import urllib2
import urllib.request
from bs4 import BeautifulSoup

start = 0
end = 100
page_size = 25
key_words = ["上地", "龙泽", "回龙观", "新龙城", "龙腾苑", "龙博苑"]
# key_words.extend(["古荡湾新村", "枫华府第", "天苑花园", "益乐新村", "古荡新村", "世纪新城", "金色蓝庭", "龙湖唐宁", "康新花园", "南都银座"])
# key_words.extend(["嘉绿北苑", "嘉绿青苑", "景城花园", "嘉绿南苑", "嘉绿福苑", "华门世家", "嘉绿莲苑", "古荡湾", "中兴文都苑"])
# key_words.extend(["华星公寓", "通普大楼"])

href_start = 18
href_end = 63
title_start = 72

out_file = open("/Users/reamongao/git/python/Demo1/temp/result.txt", "w+")


def crawl_douban_room():
    for i in range(end):
        url = "https://www.douban.com/group/beijingzufang/discussion?start=" + str(i * 25)
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(response, "html5lib")
        info = soup.select("table.olt tbody tr")
        for child in info[1:]:
            content = child.select("td.title a")[0].prettify().encode('utf-8')
            href = content[href_start:href_end]
            title_end = content.find(b'">')
            title = content[title_start:title_end]
            for key_word in key_words:
                if title.find(bytes(key_word, encoding="utf8")) != -1:
                    print('title: %s  , url:  %s' % (bytes.decode(title,'utf-8'),href))
                    break


if __name__ == "__main__":
    crawl_douban_room()
