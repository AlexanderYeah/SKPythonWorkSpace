#coding=utf-8;

# 延迟提交数据的必要性，同一个IP地址在短时间连续的进行网页访问，服务器会返回一个验证码的页面，要求用户填写数据。
# 所以解决方案1： 延时访问，这样使得程序效率较低
# 解决方案2： 使用代理。就是将你要访问的网址 告知代理，代理进行访问，然后代理将内容接着转发过来。

# 方案 1 ： 就是在程序的末尾，加一个time.sleep(5);
# 方案 2 ： 进行自定制opener
# 使用代理步骤
# 1 参数字典，将代理的IP地址 和 对应的端口号 放进去
#proxy_support = urllib.request.ProxyHandler({});
# 2 定制opener 
#opener = urllib.request.build_opener(proxy_support);
# 3 将定制的opener 安装到系统中，以后每次使用urlopen进行访问，就是使用自己定制的opener 在访问
#urllib.request.install_opener(opener);

# 在网上搜索一个免费的代理IP

import urllib.request

url1= 'http://www.whatismyip.com.tw/'

proxy_sup1 = urllib.request.ProxyHandler({'http':'121.31.77.107:8123'});
open1 = urllib.request.build_opener(proxy_sup1);
urllib.request.install_opener(open1);

# 看看访问的ip 地址有没有改变
res1 = urllib.request.urlopen(url1);
html1 = res1.read().decode('utf-8');
print (html1);





