#coding=utf-8;

# 1 对象 = 属性 + 方法
# python 中类名必须大写
class Dog:
	# 下面是属性，代码层面来看的话就是变量
	color ='red';
	legs = 4;
	name = 'Tom';
	# 方法就是函数
	def eat(self):
		print ("i want to eat something...");
	def run(self):
		print ("run and run");
	def sleep(self):
		print ("have some sleep");

# 1.1 对象的使用 就需要来实例化一个对象 Instance Objects
dd = Dog();
dd.eat();
print (dd.name);


# 1.2 构造方法 __init__() 只要创建对象的时候，就会调用此方法
class Cat:
	# 这里规定了 要传入一个参数
	def __init__(self,name):
		self.name = name;

	def bark(self):
		print ("i am a Cat and my name is %s" % self.name);
# 必须要传入一个参数
cc = Cat("jerry");
cc.bark();		

# 2 公有和私有  面向对象编程的语言都有公有和私有类型之分
class Person:
	# python 中的私有 就是使用名字改编技术，在函数名前加上__,就变成私有的了
	__name = "Alexander";

pp = Person();
# 但是，在外部同样是可以访问的 _类名__变量名就可以访问了
print(pp._Person__name); 

# 3 继承
# 被继承的类城称之为父类 基类 超类 ，一个子类可以继承父类的任何属性和方法

class Parent():
	def hello(self):
		print ("this is hello form Parrent class");
# 定义子类的时候，要将父类传递进去 如果子类中定义的方法和属性和父类相同，则会覆盖父类的方法
class Child(Parent):
	pass;		

p = Parent();
p.hello();
c = Child();
c.hello();

# 4 调用未绑定的父类方法
import random as r
class Fish():
	def __init__(self):
		self.x = r.randint(0,10);
		self.y = r.randint(0,10);
	def move(self):
		self.x -= 1;
		print ("my current location:",self.x,self.y);

# 定义一个Shark 的子类
class Shark(Fish):
	"""docstring for Shark"""
	def __init__(self):
		# 解决方案一 ：调用父类
		# Fish.__init__(self);
		# 解决方案二 ： 调用super 函数
		super().__init__();
		self.hungry = True;
	def eat(self):
			if self.hungry:
				print("i am so hungry,eat ...");
			else:
				print("i feel so good,not hungry");		



fish = Fish();
fish.move();
shark = Shark();
# 虽然继承了但是还是会报错 所以要先去初始化的时候，要先去调用父类的init方法
# Fish.__init__(self); 必须要先调用此方法，否则的话，父类中初始化的x，y 子类访问不到
shark.move();	

# 使用super函数 也可以解决以上的问题	

# 5 多重继承 简而言之，就是一个子类可以同时继承多个父类的方法和属性
class Base1:
	def hello1(self):
		print("hello from base_1");
class Base2:
	def hello2(self):
		print("hello from base_2");

class Children(Base1,Base2):
	pass;
# 如下 同时继承两个父类的方法，多重继承容易造成代码混乱
child1 = Children();
child1.hello1();
child1.hello2();			





	
