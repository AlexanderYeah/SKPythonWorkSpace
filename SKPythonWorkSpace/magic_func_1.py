#coding=utf-8;
# 所谓的魔力方法总是被双下划线包围
# 1 __init__ 方法，返回值一定是None，不能是其他
# 2 __new__ 这个才是对象实例化的时候第一个调用的方法，他的第一个参数不是self 而是cls，
# 而其他的参数会传递给__init__ 的,方法返回一个实例对象

class CapStr(str):
	def __new__(cls,string):
		string = string.upper();
		return str.__new__(cls,string);

a = CapStr("alexanderyeah");
print (a);		
# 3 __del__(self),上面的两个方法都市对象的构造器 ，而此方法是对象的析构器，当对象将要被销毁的时候，就会调用
# class A:
# 	def __init__(self):
# 		print("call __init__");
# 	def __del__(self):
# 		print("call __del__");

# aa = A();

# 4 工厂函数 python2.2 之后，将这个bif 转为 工厂函数list() int() float() tuple() str()
# 这些函数的type 都是 为 type 类型，也就是类对象
print (type(list));
print (type(int));

# 5 算数运算符
# __add__(self,other) 加法 
# __sub__(self,other) 减法
# 定义新的类 继承int 
class New_int(int):
	# 重写了内部的加减方法
	def __add__(self,other):
		return int.__sub__(self,other);
	def __sub__(self,other):
		return int.__add__(self,other);

a = New_int(3);
b = New_int(7);
# 结果为-4 
print (a+b);
# 结果为10
print (a-b);

# 如果我们自己写代码，不调用默认的加和减方法 也是可行的
# class Two_int(int):
# 	# 这样写看似没有错误，但是使用+的时候,因为self 和 other 都是本类的,就会触发本身的这个__add__ 方法，就会造成循环调用
# 	def __add__(self,other):
# 		return self + other;
# 	def __sub__(self,other):
# 		return self - other;

class Two_int(int):
	# 使用int，将self 和 other 转化为 int 的类对象，则就不会出触发Two_int 这个类的方法，避免了循环调用
	def __add__(self,other):
		return int(self) + int(other);
	def __sub__(self,other):
		return int(self) - int(other);

tt = Two_int(3);
kk = Two_int(25);
# 如下 结果为28 正确 ，避免了 无限调用的问题
print(tt+kk);

# 6 一元操作符 
x = -7;
y = 5;
# 取正
print (x.__neg__());
# 取负
print (y.__pos__());
# 取绝对值
print (x.__abs__());
# 按位取反 __invert__();


