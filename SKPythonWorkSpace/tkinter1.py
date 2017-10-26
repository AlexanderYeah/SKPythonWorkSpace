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
root = tk.Tk();
# 创建一个文本的对象
textLabel = tk.Label(root,text="第一个label这么丑");
# 布局
textLabel.pack(side=tk.LEFT);
# 添加一个背景图
"""
    真是个大坑，上面的代码没有屏蔽，下面的图片死也加载不出来，上网查了才知道,
    上面的代码没有屏蔽吗，但是已经开启了一个线程，所以再次开启线程不能调用PhotoImage 对象
"""
photo = PhotoImage(file="timg.gif");
img_label = tk.Label(root,image=photo);
img_label.pack(side=tk.RIGHT);

root.mainloop();








