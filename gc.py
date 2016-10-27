import requests
import os
import sys
import time
from selenium import webdriver

class PaperInformation:
    def __init__(self):
        self.title = ''
        self.auther = ''
        self.year = 0
        self.cites = 0
#


def GetIntFromString(s):
    a = list(filter(str.isdigit,s))
    if len(a) == 0:
        return 0
    else:
        result = "".join(a)
        return int(result)
#
def GetAutherFromString(s):
    a = s.split('-')
    year = GetIntFromString(a[1])
    return a[0]
#
def GetYearFromString(s):
    a = s.split('-')
    year = GetIntFromString(a[1])
    return year
#

os.system('cls')
# sys.setdefaultencoding('utf-8')
url = "https://xue.glgoo.com/scholar?hl=zh-CN&q=smooth+particle+hydrodynamic"
driver = webdriver.Chrome()
driver.get(url)
resultsPart = driver.find_elements_by_class_name("gs_r")
results = []
for result in resultsPart:
    #class gs_ggs gs_fl : 下载链接
    #class gs_ri : result information
    #class gs_rt : result title
    #class gs_a : result auther
    #class gs_rs : result 摘要
    #class gs_fl : 引用信息
    resultTitle = result.find_element_by_class_name("gs_rt")
    title = resultTitle.find_element_by_tag_name("a")
    resultAuther = result.find_element_by_class_name("gs_a")
    resultCite = result.find_element_by_class_name("gs_fl")
    resultCiteControl = resultCite.find_element_by_tag_name("a")
    paperInformation = PaperInformation()
    paperInformation.title = title.text
    paperInformation.cites = GetIntFromString(resultCiteControl.text)
    paperInformation.auther = GetAutherFromString(resultAuther.text)
    paperInformation.year = GetYearFromString(resultAuther.text)
    results.append(paperInformation)
driver.close()

filePoint = open('test.txt','w',encoding='utf-8')
for result in results:
    filePoint.write(result.title + "\n")
    filePoint.write(result.auther + "\n")
    filePoint.write(str(result.year) + "\n")
    filePoint.write("引用：" + str(result.cites) + "\n")
    filePoint.write("\n")
filePoint.close()
