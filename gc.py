import requests
import os
import sys
import time
from selenium import webdriver
import xlrd
import xlwt
from xlutils.copy import copy

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
    a = s.split(' - ')
    year = GetIntFromString(a[1])
    return a[0]
#
def GetYearFromString(s):
    a = s.split(' - ')
    year = a[1].split(',')
    year = year[len(year)-1]
    year = GetIntFromString(year)
    return year
#
def GetResultsFromOnePage(resultsPart):
    results = []
    for resultC in resultsPart:
        #class gs_ggs gs_fl : 下载链接
        #class gs_ri : result information
        #class gs_rt : result title
        #class gs_a : result auther
        #class gs_rs : result 摘要
        #class gs_fl : 引用信息
        result = resultC.find_element_by_class_name("gs_ri")
        resultTitle = result.find_element_by_class_name("gs_rt")
        title = resultTitle.text.split(']')
        title = title[len(title)-1]
        resultAuther = result.find_element_by_class_name("gs_a")
        resultCite = result.find_element_by_class_name("gs_fl")
        resultCiteControl = resultCite.find_element_by_tag_name("a")
        paperInformation = PaperInformation()
        paperInformation.title = title
        paperInformation.cites = GetIntFromString(resultCiteControl.text)
        paperInformation.auther = GetAutherFromString(resultAuther.text)
        paperInformation.year = GetYearFromString(resultAuther.text)
        results.append(paperInformation)
    return results
#
def GetResultsToPage(url, endPage):
    driver = webdriver.Chrome()
    driver.get(url)
    results = []
    pageNow = 1
    while pageNow < (endPage + 1):
        resultsPart = driver.find_elements_by_class_name("gs_r")
        pageResults = GetResultsFromOnePage(resultsPart)
        for result in pageResults:
            results.append(result)
        bottomPart = driver.find_elements_by_id("gs_ccl_bottom")
        if len(bottomPart) == 0:
            break
        bottomPart = driver.find_element_by_id("gs_ccl_bottom").find_element_by_id("gs_nm")
        links = bottomPart.find_elements_by_tag_name("button")
        link = links[len(links)-1]
        if link.is_enabled():
            link.click()
        else:
            break
        pageNow = pageNow + 1
    driver.close()
    return results

os.system('cls')
# sys.setdefaultencoding('utf-8')
url = "https://xue.glgoo.com/scholar?hl=zh-CN&q=smooth+particle+hydrodynamic"
# driver = webdriver.Chrome()
# driver.get(url)
# resultsPart = driver.find_elements_by_class_name("gs_r")
results = GetResultsToPage(url, 20)
print(len(results))

# filePoint = open('test.txt','w',encoding='utf-8')
# for result in results:
#     filePoint.write(result.title + "\n")
#     filePoint.write(result.auther + "\n")
#     filePoint.write(str(result.year) + "\n")
#     filePoint.write("引用：" + str(result.cites) + "\n")
#     filePoint.write("\n")
# filePoint.close()

myFile = xlrd.open_workbook('articles.xls')
print(myFile.sheet_by_index(0).nrows)
newFile = copy(myFile)
table = newFile.get_sheet(0)
i = 0
for result in results:
    table.write(i,0,i)
    table.write(i,1,result.title)
    table.write(i,2,result.auther)
    table.write(i,3,result.year)
    table.write(i,4,result.cites)
    i = i + 1
newFile.save('articles.xls')
