#coding=utf-8;

from tkinter import  *
import  tkinter as tk
# 1 LabelFrame 组件

# root1 = tk.Tk();
#
# group = LabelFrame(root1,text="世界上最帅的男人?",padx= 16,pady=16);
# group.pack();
# choices = [("Alex",1),("YSK",2),("yege",3),("Alexander",4)];
# v = IntVar()
# v.set(1);
# for item ,idx in choices:
#     r = Radiobutton(group,text=item,variable=v,value=idx);
#     r.pack();
#
# root1.mainloop();

# 2 Entry 组件
# # 就是平时说的输入框
# root2 = tk.Tk();
# e = Entry(root2);
# e.pack(padx= 25,pady=25);
# # 删除从0 到 结束的文字
# e.delete(0,END);
# e.insert(0,"default text");
#
#
# # 如果要获取用户的信息 使用get() 即可获取
# def getinfo():
#     value2 = e.get();
#     # 清楚文字
#     e.delete(0,END);
#     print (value2);
#
# button2 = Button(root2,text="Get Info",command=getinfo);
# button2.pack(side=tk.LEFT);
#
# root2.mainloop();

# 3 Entry 密码输入框
# root3 = tk.Tk();
# # grid 是允许你用表格的方式来管理组件 row 代表行 column 代表列
# lbl3_1 = Label(root3,text="Username:").grid(row=0);
# lbl3_2 = Label(root3,text="Password:").grid(row=1);
# v3_1 = StringVar();
# v3_2 = StringVar();
# e3_1 = Entry(root3,textvariable=v3_1);
# # 开启密文模式
# e3_2 =Entry(root3,textvariable=v3_2,show="*");
# e3_1.grid(row = 0,column=1,padx=15,pady=10);
# e3_2.grid(row=1,column=1,padx=15,pady=5);
#
# def getInfo3():
#     value1 = e3_1.get();
#     value2 = e3_2.get();
#     e3_1.delete(0,END);
#     e3_2.delete(0,END);
#
#     print ("username:-%s\npassword:%s" % (value1,value2));
#
#
# # 按钮
# button3_1 = Button(root3,text="getInfo3",command=getInfo3).grid(row=2,column=0,padx=15,pady=15);
# # 退出的话 直接调用quit 方法 即可
# button3_2 = Button(root3,text="exit3",command=root3.quit).grid(row=2,column=2,padx=15,pady=15);
#
# root3.mainloop();

# 4 Entry 组件还支持验证输入的合法性
# 需要设置 validate  设么时候验证  有 focus focusin focusout key all none 选项
# validatecommand  绑定验证的函数
# invalidcommand 指定的函数 ，只有当validate绑定的函数返回的值为False 的时候会调用

root4 = tk.Tk();
# 当组件获得失去焦点的时候进行验证
def test4():
    value4 = e4.get();
    if value4.isdigit():
        print ("is number");
    else:
        print ("not number");


var4 = StringVar();
e4 = Entry(root4,textvariable=var4,validate="focusout",validatecommand=test4);
e4.pack(padx=15,pady=25);

e4_1 = Entry(root4);
e4_1.pack(padx=17,pady=26);

root4.mainloop();











