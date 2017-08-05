#coding=utf-8;

# 1 创建tuple
tuple1 = (1,2,3,4,5,6);
# 1.1访问元组的形式和列表无异
print tuple1[1];
# 1.2 使用分片的方式复制一个元组
tuple2 = tuple1[:];
# 1.3 元组的更新,通过分片的方法,将元组拆分成两部分，使用连接符+拼接成一个新的元组
tuple3 = ("apple","banana","orange");
# 要注意加, 代表是元组类型
tuple3 = tuple3[:1] + ("grape",) + tuple3[1:];
print tuple3;

# 2 将元组转为 list，修改完毕转为tuple
tuple4 = (3,6,9,12);
b = list(tuple4);
b[2] = 99;
tuple5 = tuple(b);
print tuple5;

