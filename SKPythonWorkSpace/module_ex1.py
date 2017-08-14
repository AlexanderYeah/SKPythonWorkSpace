#coding= utf-8;
def sayHi():
	print("hello from other py file");
def sayBye():
	print ("bye bye from other py file");	

def test_main():
	print ("这是一个test函数，当作为引入模块的时候，这句话不能打印");



if __name__ == '__main__':
	# 调用此函数
	test_main();	