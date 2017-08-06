#coding= utf-8
print "函数的定义";

# 1 函数的定义
def function():
	pass
# 2 函数的参数
#2.1 形参 和 实参
def func1(arg1):
		print arg1;
# 形参就是定义函数的时候形式参数 实参就是传递到函数内部的实际参数
func1("aaa");

# 2.2 函数文档
def func2 (arg1,arg2):
	""" 
		这是两个数求和的运算
	 """
	return arg1 + arg2;

print func2(5,8);
# 查看函数的文档
print func2.__doc__;

# 2.3 关键字参数
def func3(arg1,arg2):
	print arg1 + "--1在前2在后--" + arg2;

func3(arg1="1",arg2="2");

# 2.4 收集参数 用* 接受所有的参数
def func4(*nums):
	b = 0;
	for i in nums:
		b = b + i;
	return b;
print func4(1,2,3);	

list1 = [2,2,4];
#  讲一个列表传入到里面需要进行解包，否则会报错
print func4(*list1);
# 3 关于函数和过程
# 有返回值的叫做函数，没有返回值的叫做过程，在python 中，所有都有返回值
# 没有的话，会返回none
def hello():
	print "hello me";
# 会打印一个hello me，并且返回一个None
print hello();

#4 在函数内部无法修改全局变量
def discount(price,rate):
		final_price = price * rate;
		# 在这里修改用户输入的价格
		old_price = 100;
		print ("局部变量中的old_price的值是%s" %old_price);
		return final_price;

old_price = input("请输入原价:");
rate = input("请输入折扣率:");
new_price = discount(old_price,rate);

print ("打折后的价格是%s" %new_price);
# 发现还是24 在函数内部修改就是生成一个跟全局变量相同的名字
print ("全局变量old_price现在的值是%s" %old_price);		













