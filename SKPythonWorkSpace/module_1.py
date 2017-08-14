#coding= utf-8;

# 1 导入模块的使用 将另外一个py文件的名字直接写上
import module_ex1 as HelloFunc
# 直接进行调用
HelloFunc.sayHi();

# 2 from 模块名 import 函数名
from module_ex1 import sayBye
# 这样的话，直接调用函数名字
sayBye();

# 3  if __name__ == '__main__'
# 模块作为单独程序运行的时候，就是__main__,
# 引入此模块之后，test_main() 就不会去调用了，只要单独运行的时候才去调用

# 4 搜索路径
import sys 
# ['/Users/alexander/Desktop/2222/SKPythonWorkSpace/SKPythonWorkSpace', '/Library/Frameworks/Python.framework/Versions/3.4/lib/python34.zip', '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4', '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/plat-darwin', '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages']
# 以上是打印出来的搜索路径
# 写好的模块，一般放到site-package 下面 然后拼接上具体的路径，在导入的时候就能正确找到
print (sys.path);
# 直接 导入 site-package 放的模块 直接就可以使用 
import ex1 

# 假如说，你想添加一个自定义的路径到系统的搜索路径中也是可以的
# 如下 拼接桌面上的一个路径，这样就可以搜索到该路径下面的模块了
sys.path.append("/Users/alexander/Desktop/testaaaa")

import ex2

