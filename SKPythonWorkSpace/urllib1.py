#coding=utf-8

#ulrlib 是 包含四个模块 包含了对服务器的请求 跳转 代理 和安全等各个方面
import urllib. request
# 1 使用urlopen() 函数访问互联网
#response = urllib.request.urlopen("http://www.baidu.com");
#html = response.read();

#html = html.decode("utf-8");
#print(html);


#2 下载一只猫
# wb 是写入二进制文件 从网络上下载一个毛的图片
response2 = urllib.request.urlopen("http://placekitten.com/g/200/300");
cat_img = response2.read();

with open('cat_200_300.jpg','wb') as f:
	f.write(cat_img);

# urlopen 返回的是一个类文件对象，还有3个函数 
# 获取HTTP 状态码
statusCode = response2.getcode();
# 返回请求的url
resUrl = response2.geturl();
# 返回一个httplib HTTPMessage对象 包含远程服务器返回的头信息
httpInfo =  response2.info();
print ("请求响应的状态码----" + str(statusCode));	
print ("返回请求的url----" +  resUrl);
#print ("返回一个HTTPMessage对象 --" + httpInfo);



