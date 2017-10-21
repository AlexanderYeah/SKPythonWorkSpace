#coding=utf-8;

# beautifulsoup 模块的学习
# beautiful 是从HTML 文件中提取数据

import  urllib.request
from bs4 import BeautifulSoup
import re
import urllib.parse





def main():
    url = "https://baike.baidu.com/item/%E4%B8%9C%E6%96%B9%E6%98%8E%E7%8F%A0%E5%B9%BF%E6%92%AD%E7%94%B5%E8%A7%86%E5%A1%94/318179?fromtitle=%E4%B8%9C%E6%96%B9%E6%98%8E%E7%8F%A0&fromid=417422";
    response = urllib.request.urlopen(url);
    html = response.read();
    # 需要传递两个参数，第一个参数是提取数据的HTML 或者XML 第二个参数是指定的 解析器
    soup = BeautifulSoup(html, "html.parser");
    # 筛选出所有包含view 关键字的链接
    # 函数re.compile将正则表达式（以字符串书写的）转换为模式对象，可以实现更加有效的匹配
    for item in soup.find_all(href=re.compile("view")):
        print(item.text,"- >",''.join(["http://baike.baidu.com",item["href"]]));


#main()

# demo2  检测词条是否有副标题

def check1():
    keyword = input("input the word you want to google");
    keyword = urllib.parse.urlencode({"word":keyword});

    url3 = "https://baike.baidu.com/search/word?" + keyword;

    resp = urllib.request.urlopen(url3);
    html =  resp.read();
    soup = BeautifulSoup(html,"html.parser");

    for each_item in soup.find_all(href=re.compile("view")):
        content=''.join([each_item.text]);
        # href="/item/%E7%8C%AA%E5%85%AB%E6%88%92/17330461#viewPageContent"
        url2 = ''.join(["http://baike.baidu.com",each_item["href"]]);

        resp2 = urllib.request.urlopen(url2);
        html2 = resp2.read();
        soup2 = BeautifulSoup(html2,"html.parser");
        # 如果有副标题的话，将其打印出来
        if soup2.h2:
            content = ''.join([content,soup2.h2.text]);

        content = ''.join([content,"- >",url2]);

        print(content);


check1();







