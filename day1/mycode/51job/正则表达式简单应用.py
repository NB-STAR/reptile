# encoding:utf-8
import re

mystr = """<div class="rt">
                共1547条职位
            </div>"""

restr = "共(\\d+)条职位"  # 正则表达式，()为只要里面的内容

regex = re.compile(restr, re.IGNORECASE)

mylist = regex.findall(mystr)

print mylist[0]
