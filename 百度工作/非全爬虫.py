import requests
import json
from bs4 import BeautifulSoup

fo = open("d:/计算机专业非全日制.xlsx", 'w')
colIndex = [0, 4, 5, 6, 8, 9]


def handleTd(trItem):
    for index, tdItem in enumerate(trItem.select('td')):
        if index in colIndex:
            continue
        if index == 7:
            fo.write('| ' + '[详情](https://yz.chsi.com.cn' + tdItem.select('a')[0].attrs['href'] + ')')
            fo.writelines(' |\n')
            continue
        value = tdItem.string if tdItem.string != None else ' '
        fo.writelines(' ' + value)


def getProfession(url):
    professionHtml = requests.post('https://yz.chsi.com.cn' + url)
    professionHtml.encoding = 'utf-8'
    professionSoup = BeautifulSoup(professionHtml.text, 'html.parser')
    trs = professionSoup.select('.more-content tr')
    for trItem in trs: # 抓取专业的详细跳转
        handleTd(trItem)


def getSchool(ssdm):  # ssdm 省市代码 yjxkdm 学科代码 zymc 专业名称 xxfs 学习方式
    r = requests.post('https://yz.chsi.com.cn/zsml/queryAction.do', params={'ssdm': ssdm, 'yjxkdm': '0854', }, )
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    for item in soup.select('.ch-table a'): # 查询学校下的每个专业
        fo.writelines('##' + item.string + '\n')
        fo.writelines('|院系所  | 专业 | 研究方向 | 考试范围 | \n')
        fo.writelines('| - | - | - | - |  \n')
        getProfession(item.attrs['href'])


def main():
    cities = requests.post('https://yz.chsi.com.cn/zsml/pages/getSs.jsp') # 获取城市，for循环，查询每个城市下的学校
    for city in json.loads(cities.text):
        fo.writelines('#' + city['mc'] + '\n')
        getSchool(city['dm'])


if __name__ == '__main__':
    main()
    fo.close()
