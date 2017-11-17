#coding=utf-8;

import json

"""
    json (JavaScript Object Notition) 是一种轻量级的数据交换格式
    python3 中的json 模块，包含了两个函数
    json.dumps(): 对数据进行编码
    json.loads(): 对数据进行解码
"""

# 1 编码
# 将字典转为 JSON 对象
data = {
    "name":"alex",
    "age":"25",
    "desc":"handsome and youcai"
}

json_str = json.dumps(data);
print("Python 原始数据格式：" + repr(data));
print("JSON 对象",json_str);


# 将json 对象转换为Python 字典
data2 = json.loads(json_str);
print("Python 字典"+ data2);


# 如果要处理的是文件 而不是字符串 使用 json.dump 来编码 和 json.load 进行解码
# 写入json 数据
with open('data1.json','w')  as  f:
    json.dump(data,f);

# 读取json 数据
with open('data1.json','r') as  f:
      data3 =  json.load(f);

