#coding=utf-8;
print "how to use os module";

# 1 第一步导入模块
import os
# 1.1 getcwd() 获取程序当前工作目录
print os.getcwd();
# 1.2 chdir() 改变当前工作目录
# 1.3 listdir() 列出指定目录的文件夹
# 1.4 mkdir() 在当前目录创建一个os_make 的问价夹，如果已经存在，则会抛出异常
#os.mkdir('os_make');
# 1.5 makedirs(path) 创建多层文件夹目录
#os.makedirs(r".\a\b\c");
# 1.6 remove(path) 用于删除指定的文件
# 1.7 rmdir() 用于删除指定的文件夹
# 1.8 removedirs() 则是用于删除多层目录
# 1.9 rename 用来重命名文件或者文件夹
#os.rename('os_make','os_change');
# 2 system(command) 几乎每一个操作系统都会提供小工具 进行命令操作
# 打开window 的计算器命令
#os.system('calc');

# 2.1 walk() 函数，遍历传入指定参数路径内的所有子目录
# 并将结果返回一个三元组（路径，[包含目录],[包含文件]）;

for i in os.walk('../SKPythonWorkSpace'):
	print (i);
# 另外path 模块很实用的定义 os.curdir 当前的目录 os.pardir 上一层目录
# os.name 表示当前使用的操作系统的名字
print os.name;

# 3 os.path 模块 很多方法
# 3.1 basename(path) 去掉目录路径 单独返回文件名 直接返回txt
# exists(path) 指定路径目录文件是否存在
# isabs(path) 判断路径是否为绝对路径
# 等方法

# 4 pickle 模块，泡菜 保存对象类型的数据 列表 字典
import pickle

list1 = ['orange',6.88,999,[2,3,4]];
# 写入 必须以二进制形式打开文件
pickle_file = open('my_list.pkl','wb');
# 使用dump 方法来保存数据,就会多一个my_list.pkl的文件 
pickle.dump(list1,pickle_file);
pickle_file.close();

# 文件的读取 同样的以二进制的形式读
pickle_read_path = open('my_list.pkl','rb');
# 使用load 加载数据 就可以了
list2 = pickle.load(pickle_read_path);
print list2;










