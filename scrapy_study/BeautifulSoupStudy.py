#coding=utf-8
'''
Created on 2017年4月19日

@author: Administrator
'''
from bs4 import BeautifulSoup
import codecs
import urllib2
import re

def crawl(url):
    page=urllib2.urlopen(url)
    contents = page.read()
    soup = BeautifulSoup(contents,"html.parser")
    print u'豆瓣电影250：序号\t影片名\t 评分\t 评价人数'
    for tag in soup.find_all(attrs={"class":'item'}):
        ###find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
        num = tag.find('em').get_text()
        print num
        name = tag.find(attrs={"class":'hd'}).a.get_text()
        link_path = tag.find(attrs={"class":'hd'}).a.get('href')
        print link_path
        name = name.replace("\n",' ')
        print "smile:"+name
        title = tag.find_all(attrs={"class":"title"})  
#         print "sunshine:"+title
        i = 0  
        for n in title:  
            text = n.get_text()  
            text = text.replace('/','')  
            text = text.lstrip()  
            if i==0:  
                print u'[中文标题]', text  
                infofile.write(u"[中文标题]" + text + "\r\n")  
            elif i==1:  
                print u'[英文标题]', text  
                infofile.write(u"[英文标题]" + text + "\r\n")  
            i = i + 1  
        #爬取评分和评论数  
        info = tag.find(attrs={"class":"star"}).get_text()  
        info = info.replace('\n',' ')  
        info = info.lstrip()  
        print info  
        mode = re.compile(r'\d+\.?\d*')  
        print mode.findall(info)  
        i = 0  
        for n in mode.findall(info):  
            if i==0:  
                print u'[分数]', n  
                infofile.write(u"[分数]" + n + "\r\n")  
            elif i==1:  
                print u'[评论]', n  
                infofile.write(u"[评论]" + n + "\r\n")  
            i = i + 1  
        #获取评语  
        info = tag.find(attrs={"class":"inq"})  
        if(info): # 132部电影 [消失的爱人] 没有影评  
            content = info.get_text()  
            print u'[影评]', content  
            infofile.write(u"[影评]" + content + "\r\n")  
        print ''   
         
if __name__ == '__main__':
    infofile = codecs.open(r'f:\result_douban.txt', "w", "utf-8")
    url = 'http://movie.douban.com/top250?format=text'  
    i = 0  
    while i<10:  
        print u'页码', (i+1)  
        num = i*25 #每次显示25部 URL序号按25增加  
        url = 'https://movie.douban.com/top250?start=' + str(num) + '&filter='  
        crawl(url)  
        infofile.write("\r\n\r\n\r\n")  
        i = i + 1  
    infofile.close()  

  
  
# html_doc = """ 
# <html><head><title>The Dormouse's story</title></head> 
# <body> 
# <p class="title"><b>The Dormouse's story</b></p> 
# <p class="story">Once upon a time there were three little sisters; and their names were 
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>, 
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; 
# and they lived at the bottom of a well.</p> 
# <p class="story">...</p> 
# """  
#   
# #获取BeautifulSoup对象并按标准缩进格式输出  
# soup = BeautifulSoup(html_doc)  
# print(soup.prettify())  
    