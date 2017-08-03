#coding=utf-8;

# 1字符串 获取
b = "AlexanderYeah";
print b;
# 1.1 获取到0位
print "第0位:" + b[0:];
# 1.2 获取区间
print "第3到6位:"+ b[3:6];
# 1.3 获取待末位
print "第末位:" + b[-1];

# 2 字符串的处理
# 2.1 获取指定字符串的索引 进行类型转化
print "Y的索引为:" + str(b.index("Y"));
# 2.2 获取字符串的索引值
print "a 的索引值为:" + str(b.find("a"));
# 2.3 判断字符串是否包含字母
print "是否包含字符串:" + str(b.isalpha());
# 2.4 是否包含数字或者字母
print "是否包含数字:"+ str(b.isalnum());
# 2.5 是否全部为数字
print "是否包含数字:" + str(b.isdigit());
# 2.6 是否全部为空白
print "是否全部为空白:" + str(b.isspace());

# 3 字符串的拼接
e = "this";
d = "is";
f = "smart";
# 用一个空格拼接起来
print " ".join([e,d,f]);

# 4 字符串的替换
f = "this is test";
print f.replace("test","coder");

# 5 长字符串的处理
# 生活不止眼前的苟且 还有诗意的远方 加油吧 carry on
# 上面的话，每一句进行换行,
# 5.1 简便的方法 使用三个" 进行包裹,会保持原有的格式进行输出
print("""
	生活不止眼前的苟且
	还有诗意的远方
	加油吧 
	carry on
""")
# 5.2 不太简便的方法,使用换行符
print("生活不止眼前的苟且\n还有诗意的远方\n加油吧\ncarry on");
# 5.3 
print("i just wanna run\n" *3);


# 6 字符串的拼接
# 6.1 第一种形式。多个参数的情况下，要用元组装参数
print "Alex is so %s and is very %s" %("handsome","nice");
# 6.2 format 的用法 {} 相当于占位符%s的作用
print "Dream big,we can {} {}".format("do","it");
# 6.3 format 比较智能的地方，可以自定义顺序
print "First,wash {1} ,and then eat {0}".format("food","hand");
# 6.4 format 可以用标识符，清晰明了
print "Today,it is {what},and i feel {how}".format(what = " very hot",how ="not good");
# 6.5 %s 的使用
print "you want to de %(what)s %(how)%s".format(what:"smart",how:"person");

