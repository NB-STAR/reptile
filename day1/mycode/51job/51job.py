# encoding:utf-8

import selenium  # 网页测试框架
import selenium.webdriver

import re
import urllib2


def getnumberbyname(searchname):
    url = "https://search.51job.com/list/070200,000000,0000,00,9,99," + searchname + ",2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="

    driver = selenium.webdriver.Chrome()
    driver.get(url)  # 访问链接
    pagesource = driver.page_source
    restr = u"共(\\d+)条职位"  # 正则表达式，()为只要里面的内容
    regex = re.compile(restr)
    mylist = regex.findall(pagesource)
    driver.close()
    return mylist[0]


pythonlist = ["python", "python 运维", "python 数据", "python 开发"]
# pythonlist = ["python", "python" + urllib2.quote(urllib2.quote("运维")), "python" + urllib2.quote(urllib2.quote("数据")),
#              "python" + urllib2.quote(urllib2.quote("数据")), "python%2520web"]

for pystr in pythonlist:
    print pystr, getnumberbyname(pystr)
