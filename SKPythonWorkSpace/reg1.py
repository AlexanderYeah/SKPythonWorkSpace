#coding=utf-8;
import  re

# 1 通配符 .
print( re.search(r'.','www.alexander'))
# 2 反斜杠 就是消除一个字符的特殊功能
# 例如 取出原点的通配符功能 . 这样就代表照着原的位置 （3，4）
print(re.search(r'\.','www.axaxaxax'));
# \ 可以剥夺元字符的特殊能力，当然也可以使得普通字符有特殊能力
# 如果想匹配数字 就是反斜杠 \d
print(re.search(r'\d','www.666666.com'));


# 2 字符类
# 用括号包起来就是一个字符类 这是区分大小写的 匹配打（9，10），只要匹配到任意一个就行
print (re.search(r'[a-z]',"12588888.alex.com"));
# 用来匹配数字范围 匹配数字为三位的 每一位都满足条件 就能match 到，匹配到（6，9）
print(re.search(r'[0-2][0-7][5-9]','akelx.167.com'));

# 3 重复匹配
# 用一个大括号 限制起来次数就可以了
print(re.search(r'a{3}]','kkssaaajjj'));





