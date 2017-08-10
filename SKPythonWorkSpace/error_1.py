#coding=utf-8;
print "异常处理的学习";

# 1 AsseertError 断言语句失败
list1 = [2,8,6];
# 判断条件为false 就会报错
#assert len(list1) > 3;

# 2 AttributeError 尝试访问未知的对象属性
list2 = [];
# 就会报错  因为list 没有asd 这个属性
#list2.asd;

# 3 IndexError 索引超出序列范围 如下 ，就会报IndexError 
#print list1[4];

# 4 KeyError 字典中查找一个不存在的关键子
dic1 = {"one":"orange","two":"apple"};
#print dic1["five"];

# 5 NamaError 尝试访问一个不存在的变量 如下 就会报错
# print ads;

# 6 OSError 操作系统产生异常
# 打开一个不存在的文件就会报FileNotFoundError,这个错误就是OSError 的子类
# d = open('ads.txt','r');

# 7 TypeError 不同类型间的无效操作 错误
# print 1 + '1';

# 8 SyntaxError 语法错误

# 9 ZeroDivisionError 除数为0的错误
# print 5/0;

# 10 try-except 异常捕获语句
# try:
# 	f = open('not-exist.txt','r');

# except OSError:
# 	print "打开文件出错！";

# 11 针对不同的异常设置也可以多个except
# try:
# 	f = open('aaa.txt','r');
# except OSError as reason:
# 	print "系统错误";
# except TypeError:
# 	print "类型错误";

# 12 对多个异常统一处理
# try:
# 	f = open('as.txt','r');
# except (OSError,TypeError):
# 	print "出错了";

# 13 捕获所有异常，不管什么错误，直接捕获
# try:
# 	f = open('dd.txt','r');
# except:
# 	print "出错了";

# 14 try-finally 就算出现异常 也要执行收尾工作

# try:
# 	f = open('dd.txt','r');
# except:
# 	print "出错了";
# finally:
# 	print "收尾工作结束";

# 15 raise语句 自己抛出异常

# raise ZeroDivisionError("除数不能为0");	

# 16 with 语句 打开文件，减少了代码量，并且会自动帮你关闭文件
# try:
# 	with open('abc.txt','r') as f:
# 		for each_line in f:
# 			print each_line;
# except OSError:
# 	print ("出错了")

	




