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
print(re.search(r'ka{3}j','kaaaj'));

# 也可以表示范围 匹配到（0 ，5）
print  (re.search(r'ab{2,4}c','abbbc'));

# 4 元字符 所有的元字符 如下
# . ^ $ * + ? {} [] \ | ()
# 4.1 ^ 脱字符 表示匹配字符串开始的位置，只要目标字符串出现在开始的位置，才会进行匹配
print (re.search(r'^LOVE','LOVE me!!!'));
# 否则的话 不进行匹配 结果为none
print  (re.search(r'^LOVE','i do not LOVE u'));

# 4.2 $ 美元字符 则表示匹配到字符串的结束位置 (9,16);
print  (re.search(r'kidding$','i am not kidding'));

# 4.3 \ 用途最为广泛  \ 后面跟的数字是1-99，则匹配对应的字符串
# 后面跟的是0开头或者八进制数，则表示这个八进制数对应的ASCII字符

# () 本身来讲是一个元字符，变成子组的话，可以当做一个整体
# \1 就表示序号为1 的子组，也就是handsome必须要连续出现两次才能成功匹配
print (re.search(r'(handsome)\1','alex is handsome'));
print  (re.search(r'(handsome)\1','alex is handsomehandsome'));
# \ 后面跟着数字0 开头 八进制60对应的ASCII 吗 就是0
print (re.search(r'LOVE\060','ALOVELOVE0'));
# 141 八进制对应的ASCII 吗 就是 a 匹配到（0，3）
print  (re.search(r'\141bc','abc'));

# 5 [] 字符类 就是一个字符的集合 被他包围的元字符都失去了特殊功能
print  (re.search(r'[.]','www.baidu.com'));
# 5.1 - 表示范围 就可以匹配到（3，4）；
print (re.search(r'[a-z]','999kjs'));
# 5.2 \ 反斜杠 用于字符串转义
# 5.3 ^ 用于取反字符串 匹配出所有的大写字符串
print (re.findall(r'[^a-z]','AbcDE'));












