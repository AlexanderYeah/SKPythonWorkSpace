#coding=utf-8;

#1 global 关键字
count = 8;
def func1():
	# 在函数体内部 修改全局变量，需要加上global
	global count;
	count = 2;
	print (count);

func1();

# 2 内嵌函数 在函数体内部嵌入另外一个函数
def func2():
		print("func2 正在被调用");
		def func3():
				print("func3 正在被调用");
		func3();

func2();

# 3 闭包 closure
# closure 是函数式编程的一个重要的语法结构，函数式编程是一种编程范式

def funX(x):
	def funY(y):
		return x * y;
	return funY;
# 像这种在一个内部函数里（funcY）对外部作用域的变量进行引用，则这个内部函数就是一个闭包	
i = funX(8);

# lambda 表达式
# 匿名函数，语法精简，：左边放参数，：右边放返回值

a = lambda x : 2 * x + 1;
print "a=="+ str(a(5));	

# 4 BIF 函数 filter()
# 过滤器有两个参数，第一个参数可以是函数，也可以是None，如果是函数的话
# 就将第二个可迭代数据里面每一个元素作为函数的参数进行运算，为True 返回
# 如果为None，则默认返回可跌代数据里面ture的元素

temp = filter(None,[1,0,2,3,True,False]);
# 返回1,2,3 和True
print temp;

# 传入函数
def func_filter(z):
	if z % 2:
		return z;
# 将函数传递进去 直接调用
temp2 = filter(func_filter,range(10));
print temp2;

# 5 BIF 函数  map();
# map 有两个参数，第一个是函数，第二个是可迭代序列，将序列的每一个参数作为
#函数的参数传递进去，进行加工，在返回。
temp3 = map(lambda x : x * 2,range(10));
print temp3;		








		
