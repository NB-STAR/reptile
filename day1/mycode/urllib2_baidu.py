# encoding:utf-8
# print "hello!"  # 中文是否ok
import urllib2


# 方法1 直接读取网页数据
def download1():
    return urllib2.urlopen(url).read()


# 方法2 读取每一行的网页数据，压入列表
def download2():
    return urllib2.urlopen(url).readlines()


# 方法3 逐行读取
def download3():
    response = urllib2.urlopen(url)
    while True:
        line = response.readline()
        if not line:
            break
        print line


url = "http://www.baidu.com"  # urlopen只能处理http请求

# print download1()

print download3()
