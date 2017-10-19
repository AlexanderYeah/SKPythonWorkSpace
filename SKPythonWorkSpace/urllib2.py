#coding=utf-8;

# Demo 2  翻译文本

# 1 导入依赖库
import urllib.request
import urllib.parse
# 有道翻译 通过审查元素查到的链接 下面的链接不是在网站上找到的，这个链接是自己在网上找的

content = input("pls input the word you need to translate---");

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc";
# 传递的数据 按照审查元素中网络中的参数	
data = {};
data['doctype'] = 'json';
data['i'] = content;
data['version'] = '2.1';
data['keyfrom'] = 'fanyi.web';
data['typoResult'] = 'true';
data['type'] = 'AUTO';
data['ue'] = 'UTF-8';

# 先将提交到服务器的数据进行转码
data = urllib.parse.urlencode(data).encode('utf-8');
response = urllib.request.urlopen(url,data);

html = response.read().decode('utf-8');


# 2 将爬到的json进行优化展示
import json
# target 是个 字典 ，直接取到翻译的内容
target = json.loads(html);

# 输出翻译的结果
print ("Result:---" + target['translateResult'][0][0]["tgt"]);








