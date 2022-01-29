#A file THAT can tell what your LUCKY Number is.
#Written BY Evan
#2022/1/29
###############################################


print("这是一个可以显示你幸运数字的脚本")
NAME=input("请输入你的中文名的拼音（不带空格，大小写均可）: ")
name=NAME.lower()         #大写转小写
Translate=' '.maketrans('abcdefghijklmnopqrstuvwxyz','12345678912345678912345678')       #转换字母到数字
name_trans=name.translate(Translate)  
namenum=int(name_trans)

#幸运数字运算
luckynum=(namenum - 1) % 9 + 1

#输出结果
print('你的幸运数字是: '+str(luckynum))