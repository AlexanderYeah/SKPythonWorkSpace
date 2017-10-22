#coding=utf-8;

import urllib.request

from bs4 import BeautifulSoup
import os
# 爬去网站目标
url = "http://www.mzitu.com/page/";
# 设置header 头
header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0"}
# 图片存储路径
# 返回当前工作目录
cur_path = os.getcwd() + '/'

# 设置爬去预览页面数量为1
preview_page = 1;

for current_page in range(1,int(preview_page) + 1):
    current_url = url + str(current_page);
    # 请求当前page的网页

    req = urllib.request.Request(current_url);
    req.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0");
    response = urllib.request.urlopen(req);
    current_page_html = response.read().decode('utf-8');

    # 解析网页
    soup = BeautifulSoup(current_page_html,'html.parser');

    # 获取套图的入口链接
    preview_link_list = soup.find(id="pins").find_all(target='_blank');

    for link in preview_link_list:
        # http://www.mzitu.com/105724/5
        # 套图入口处 就是其 id  + 页数
        # 所以现在是提取到其 id 和 套图内部的数量
        link = link['href'];

        req1 = urllib.request.Request(link);
        req1.add_header('Referer', 'http://www.mzitu.com/all/');
        req1.add_header("User-Agent",
                       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0");
        response1 = urllib.request.urlopen(req1);
        html = response1.read().decode('utf-8');
        soup2 = BeautifulSoup(html,'html.parser');

        pic_count = soup2.find("div",class_="pagenavi").find_all('a')[4].get_text();


        # 每一张套图一个目录 创建目录
        dir_name = link.split('/')[-2];


        # 多创建一层目录
        first_path = cur_path + "parrent";

        if os.path.exists(first_path):
            print ("");
        else:
            # 创建目录
            os.mkdir(first_path)

        pic_path = first_path + dir_name;


        if os.path.exists(pic_path):
            print ("")
        else:
            # 创建目录
            os.mkdir(pic_path);

         # 切换到当前的目录 进行下载
        os.chdir(pic_path)


        # 遍历 进行获取每一页图片的地址
        for pic_index in range(1,int(pic_count) + 1):
            pic_link = link + '/' + str(pic_index);

            print (pic_link);

            req2 = urllib.request.Request(pic_link);
            req2.add_header('Referer', 'http://www.mzitu.com/all/');
            req2.add_header("User-Agent",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0");
            response2 = urllib.request.urlopen(req2);
            html2 = response2.read().decode('utf-8');
            soup3 = BeautifulSoup(html2,'html.parser');
            # 到这一步 获取到每一组套图的每一张图片的地址
            pic_src = soup3.find('div',class_="main-image").find('img')['src'];

            pic_name = pic_src.split('/')[-1];


            req3 = urllib.request.Request(pic_src);
            req3.add_header('Referer', 'http://www.mzitu.com/all/');
            req3.add_header("User-Agent",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0");
            response3 = urllib.request.urlopen(req3);
            html3_img = response3.read();


            with open(pic_name,'wb') as f:
                f.write(html3_img);

            # 下载完成 推出当前目录
        os.chdir(first_path);


        print ("下载完成")

