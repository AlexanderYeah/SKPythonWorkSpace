#coding=utf-8

# 这是为了从外部到导入参数，外部运行的时候 需要传入参数 user_name
# 使用 argv 和 raw_input 来向用户提问一下问题，raw_input 是接收用户的输入
from sys import argv


script, user_name = argv;
prompt = 'yes/no>>';

print "Hello,%s,i am script %s" %(user_name,script);
print "i would like to ask you few questions？";
print "Do you like me %s" % user_name;
likes = raw_input(prompt);
# 可以拿到用户的输入，进行判断
if likes == "yes":
	print "ok ,thank you budy";


print "Where do you lives??";
lives = raw_input("location>>");

print "What kind of work do you like?";
works = raw_input("work_type>>");
