import requests
import os
import sys
import webbrowser

def getHtml(url):
    page = requests.get(url,timeout=20)
    return page.text
#

os.system('cls')
# sys.setdefaultencoding('utf-8')
url = "https://xue.glgoo.com/scholar?hl=zh-CN&q=smooth+particle+hydrodynamic"
# html = getHtml(url)
# webbrowser.register
# webbrowser.open(url)

# data = webbrowser.get()
# print(data)
help(webbrowser)


# filePoint = open('test.txt','w',encoding='utf-8')
# filePoint.write(data)
# filePoint.close()