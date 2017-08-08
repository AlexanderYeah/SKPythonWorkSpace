#coding= utf-8;

#1 字典的创建方式有多种
a = dict(one = 1 ,two = 2,three = 3);
b = {'one':1,'two':2,'three':3};
c = dict(zip(['one','two','three'],[1,2,3]));
d = dict([('one',1),('two',2),('three',3)]);
e = dict({'one':1,'two':2,'three':3});
print a == b == c == d == e;

# 2 fromkeys(),用于创建并且返回一个新的字典，第一个参数是字典的键
# 第二个参数是可选的 传入键对应的值
dict1 = {};
dict1.fromkeys((1,2,3),"111");
print dict1;

#3 keys values items items() 输出所有的item
#3.1 keys() 输出所有的键值, values() 输出所有的value 值 
dict2 = {'apple':'111','tom':'222','jerry':'333'};
print dict2.keys();
print dict2.values();
print dict2.items();

# 4 get 方式提供了更为宽松的方式 访问字典项,根据键值去访问，
print dict2.get('apple');
# 4.1 当访问不到的时候，可以在第二个参数设置默认的返回值
print dict2.get('listen','找不到');
# 4.2 判断一个键是否在字典中，可以用in 或者 not in 来进行判断
print 'apple' in dict2;
print 'listen' not in dict2;

# 5 清空一个字典 用clear 方法
dict2.clear();
print dict2;

# 6 复制字典 copy 方法
dict3 = {'1':'cat','2':'dog','three':'fish'};
dict4 = dict3.copy();
print dict4;

# 7 pop 和 popitem 方法
# 7.1 pop 根据给定的键，弹出对应的值
dict4.pop('2');
print dict4;

# 7.2 popitem 弹出一个项
dict4.popitem();
print dict4;

# 8 setdefault 方法 ，和get 方法类似，但是找不到对应的值的时候，会自动创建,设置为none
print dict3.setdefault('three');
print dict3.setdefault('6');
print dict3;

# 9 update 方法 利用它来更细字典
dict3.update(three='duck');
print dict3;

# 10 用** 接受参数 打包成字典形式
def func1(** params):
	print params;

func1(** dict3);
