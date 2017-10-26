#coding=utf-8;

# tkinter 是python的内置库 可以直接导入
import  tkinter as tk
from  tkinter import  *
# 1 使用流程
# 1.1 创建主窗口 初始化 TK 模块
# top = tk.Tk();
# top.title("GOGOGO");
# # 1.2 创建Label 标签
# label = tk.Label(top,text="第一个Demo",fg='blue');
# # 1.3 pack（）用来管理和显示组件的
# # 还有 place（） grid（）
# # side 参数可以设置LEFT RIGHT TOP TOPTOM
# label.pack(side=tk.LEFT);
# 1.4 mainloop() 进入主循环
# top.mainloop();



# 2 Label 组件
# 是界面上描述输出的标签
# root = tk.Tk();
# # 创建一个文本的对象
# textLabel = tk.Label(root,text="第一个label这么丑");
# # 布局
# textLabel.pack(side=tk.LEFT);
# # 添加一个背景图
# """
#     真是个大坑，上面的代码没有屏蔽，下面的图片死也加载不出来，上网查了才知道,
#     上面的代码没有屏蔽吗，但是已经开启了一个线程，所以再次开启线程不能调用PhotoImage 对象
# """
# photo = PhotoImage(file="timg.gif");
# img_label = tk.Label(root,image=photo);
# img_label.pack(side=tk.RIGHT);
#
# root.mainloop();

# 3 文字显示在图片的上面，只需要设置compound 属性即可
# root3 = tk.Tk();
# photo3 = PhotoImage(file="timg.gif");
# textLbl = Label(root3,text="keep learning \n keep going \n be a awesome man",justify=LEFT,image=photo3,compound=CENTER,fg="red");
# textLbl.pack();
#
# tk.mainloop();


# 4 Button 组件
# 相应事件的函数要定义在前面 按钮点击之后 文字发生变化
# def root4_func():
#     var4.set("you handsome");
#
#
# root4 = tk.Tk();
# var4 = StringVar();
# # BTN 使用command 绑定对应的相应函数
# # 绑定textvariable 属性可以动态设置按钮的标题
# var4.set("SHow me !!!")
# button4 = Button(command=root4_func,textvariable=var4);
#
# button4.pack(side=tk.LEFT);
#
# root4.mainloop();

# 5 checkButton 组件
# root5 = tk.Tk();
#
# # 需要设置一个变量 来标记按钮是否被选中
# var5 = IntVar();
# c5 = Checkbutton(root5,text="first check",variable=var5);
# c5.pack(side=tk.LEFT);
#
#
# # 用一个lable 来显示选中的值
# label5 = Label(root5,textvariable=var5)
# label5.pack();
#
# c5.mainloop();


#6 练习
# root6 = tk.Tk();
#
# girls = ["a","aa","aaa","aaaa"];
# var6 = [];
# for item in girls:
#       var6.append(IntVar());
#       c6 = Checkbutton(root6,text=item, variable= var6[-1]);
#       # anchor是指定组件的显示位置
#       """
#         N NE W SE S SW W NW CENTER 九个位置
#       """
#       c6.pack(anchor= S);
#
# root6.mainloop();

#7 Radiobutton 组件
# 多个item 要共享一个变量
root7 = tk.Tk();
var7 = IntVar();
radio_btn1 = Radiobutton(text="A",variable=var7,value=1,).pack(anchor=W);
radio_btn2 = Radiobutton(text='B',variable=var7,value=2).pack(anchor=W);
# indicatoron=False 取出前面的小圆点
radio_btn3 = Radiobutton(text='C',variable=var7,value=3,indicatoron=False).pack(fill = X);
root7.mainloop();




























