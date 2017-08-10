#coding=utf-8;
# 1 使用这个模块,先要导入
import easygui as g
import sys
# g.msgbox("hello everyone!!!");

# 2 gui 的小使用

g.msgbox("hello,nice to meet u!");
msg = "What do u think of me???";
title = "Questions";
choices = ["handsome","smart","gentle man","very good"];
cb = g.choicebox(msg,title,choices);

g.msgbox("your choice is :" + str(cb));

msg = "Do u want choose again？";
title = "please choose";
if g.ccbox(msg,title):
	pass
else:
	sys.exit(0);	


