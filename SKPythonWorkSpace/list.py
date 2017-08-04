#coding=utf-8

print "this is list"

#1 创建列表,列表可以包含各种类型的数据
nums = [1,"kkk",3,[1,29]];

#1.1 想列表中添加元素 append 方法,只能添加一个元素
nums.append("addE");
print nums;

#1.2 extend 添加多个元素
nums.extend([7,9]);

#1.3 在指定位置插入元素
nums.insert(1,"alex");
print nums;

# 1.4 从列表中获取元素
print nums[2];

#1.5 从列表中删除元素 有remove del pop 方法
# remove 不能删除指定的位置的元素
print nums.remove("alex");
# del 删除指定位置的元素  del 加上列表名 直接删除列表
del nums[1];
print nums;
# 弹出最后一个元素 或者指定位置的元素
print nums.pop();
print nums.pop(3);


# 2 列表分片
friuts = ["orange","apple","banana","watermelon"];
# 2.1 截取0 到2 的元素
print friuts[0:2];
# 2.2 到最后一位
print friuts[:-1];
# 2.3 隔一个取一个元素
print friuts[0:3:2];
# 2.3 复制一个反转的列表
print friuts[::-1];

# 3 常用的操作符
# 3.1 比较 > 或者 < 
list1 = [123];
list2 = [234];
# 为真的话，返回true ，比较原理，就是list 的第一个元素进行比较，如果是字符串的话，进行ASCII 比较
print list1 > list2;
# 3.2 相加 两个列表合成一个
print list1 + list2;
# 3.3 * 将自身复制n 次
print list1 * 3;
# in 和 not in  判断成员是否在列表中
print "orange" in friuts;
print "aaa"  not in friuts;


# 4 常用方法
# 4.1 count 方法，计算某一个元素在列表中出现的次数
list3 = [1,2,3,4,2,2,2,7,3];
print list3.count(2);

# 4.2 返回其中某个参数在列表中的位置,返回的是第一个目标的位置
print list3.index(4);
# 限定查找范围
print list3.index(2,1,3);
# 4.3 reverse 反转字符串
list3.reverse();
print list3;

# 4.4 sort 用指定的方法 对列表进行排序
# 默认不需要参数，从小到大排序
list4 = [1,4,2,99,32,34,22,14,26];
list4.sort();
print  list4;

# sort 可以传递三个参数 sort (func,key,reverse)




