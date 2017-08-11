#coding= utf-8;
# 1 需求，一个水池，有5条鱼 7个乌龟。‘
# 这时候就要使用到组合了，组合就是将需要的类放进去实例化就可以了,这就是组合
class Turtle:
	def __init__(self,x):
		self.num = x;
class Fish:
	def __init__(self,x):
		self.num = x;	
# 水池这个类
class Pool:
	def __init__(self,x,y):
		self.turtle = Turtle(5);
		self.fish = Fish(7);
	def print_num(self):
		print("Fish:%d----turtlr:%d" %(self.turtle.num,self.fish.num));

p = Pool(5,7);
p.print_num();		

# 2 一些相关的BIF
# 2.1 issubclass(class,classinfo),如果第一个参数是第二个参数的子类，则返回True，classinfo 可以是类对象组成的元组
# 2.2 isinstance（object，classinfo）如果第一个参数是第二个参数的实例对象，则返回True				
# 2.3 hasattr(object,name) 测试一个对象里面是否有指定的属性
class C:
	def __init__(self,num = 6):
		self.num = num;
c1 = C();
print (hasattr(c1,'num'));

#2.4 getattr(object,name[,default])
# 返回对象指定的属性值，如果属性值不存在，返回default 默认值，如没有设置默认值，跑出attrError
print (getattr(c1,'num'));
# 2.5 setarrt(object,name,value) 相应的这是设置对象中的指定的属性值
setattr(c1,'num',88);
print (getattr(c1,'num'));
# 2.6 delattr(object,name)删除某一个对象的属性值，如果属性不存在，抛出AttrbuteError 异常
# 2.7 property() 通过属性来设置属性

class A:
	def __init__(self,size = 26):
		self.size = size;

	def getsize(self):
		return self.size

	def setsize(self,value):
		self.size = value

	def delsize(self):
		del self.size
# a = A();
# x = property(getsize,setsize,delsize);
# a.x;		



