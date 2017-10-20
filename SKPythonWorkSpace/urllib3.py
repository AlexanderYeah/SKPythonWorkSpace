#coding=utf-8;

#修改User-Agent
# 修改head 参数的方法有两种，一种是实例化Request 的时候 将header 参数传递进去  另外一种是通过add_header()方法 往Request 中添加
import urllib.request
import urllib.parse
import json

content = input("input the world you need to translate---");
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc";
# 方式1 ：
head = {};
head['Referer'] = 'http://fanyi.youdao.com/';
head['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0";
data = {};
data['doctype'] = 'json';
data['i'] = content;
data['version'] = '2.1';
data['keyfrom'] = 'fanyi.web';
data['typoResult'] = 'true';
data['type'] = 'AUTO';
data['ue'] = 'UTF-8';


data = urllib.parse.urlencode(data).encode('utf-8');
# 方式一: 实例化一个请求对象，将head 放进去
# request = urllib.request.Request(url,data,head);
# response = urllib.request.urlopen(request);
# html = response.read().decode('utf-8');
# target = json.loads(html);

# 方式二: 用add_header() 方法追加进去
req = urllib.request.Request(url,data);
req.add_header('Referer','http://fanyi.youdao.com/');
req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0');

response = urllib.request.urlopen(req);
html = response.read().decode('utf-8');
target = json.loads(html);


# 输出翻译的结果
print ("Result:---" + target['translateResult'][0][0]["tgt"]);

print (req.headers);





