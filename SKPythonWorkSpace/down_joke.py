#coding=utf-8;

# 爬去笑话网的笑话
import urllib.request
from bs4 import BeautifulSoup
import os
import re
# 爬取得url 连接
base_url = "http://www.jokeji.cn/list29_";
get_page_count = 5;


def main():
    for i in range(1,int(get_page_count) + 1):
        # 获取到每一页的html
        page_url = base_url + str(i) +'.htm';
        # 对每一个页面的html 进行数据访问
        req1 = urllib.request.Request(page_url);
        req1.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0');
        response1 = urllib.request.urlopen(req1);
        html1 = response1.read().decode('gbk');



        # 获取到所有的a链接
        joke_list = re.findall(r'/jokehtml/[\w]+/[0-9]+.htm',html1);

        for item in joke_list:
            joke_url = "http://www.jokeji.cn" + item;
            # 获取到所有的笑话链接,在去获取笑话的文本内容
            req2 = urllib.request.Request(joke_url);
            req2.add_header('User-Agent',
                            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0');
            response2 = urllib.request.urlopen(req2);

            html2 = response2.read().decode('gbk');

            joke_content_list = re.findall(r'<P>[0-9].*</P>',html2);

            for joke_single in joke_content_list:
                print (joke_single);
                print ('\n');






if __name__ == "__main__":
    main();

