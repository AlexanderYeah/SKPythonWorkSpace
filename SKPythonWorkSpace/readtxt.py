#coding=utf-8

print "读写文件";

# 0 写文件
e = open('test2.txt','w');
e.write('line1\nthe line2\nthe line3\nthe line4\n the line5');

e.close();




# 1 读写文件 w 为 写模式 r为读的模式
d = open('test2.txt','r');
# 这是是只读一行，再次调用，自动换下一行
print d.readline();
print d.readline();
# 将指针移动打第几行
d.seek(0);
#操作完毕 要进行关闭
print d.readline();
d.close();


# 2 使用linecache 模块
import linecache

# 读文件 获取第三行
print "this is we got "+linecache.getline('test2.txt',4);








