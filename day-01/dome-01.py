print('hello word');
print('python 的第一天吧'); #python必须换行

#变量
name="张三"
age=12
floatNum=3.26
print(name)
print(age)
print(floatNum)

#分割符sep="-"
print(name,age,floatNum,sep="-")

#转译字符:\n ->换行
#python结尾默认追加\n换行
print('hello\nword')
#\t -> 制表符（键盘上的tab键，等于四个空格）
print('\tAAAAAAAAA')
#\r -> 回车（换行）
print('BBBBCCCCC\r')
#'''' ; "''" ; '""'
#单引号嵌套需要转义字符
print('乔治说：\'想玩恐龙\'')
#双、单引号的嵌套使用
print("乔治说：'想吃冰淇淋'")
#字符串前面加r -> 原样输出字符（即便有转译字符也不会转译）
print(r'乔治\r疯\\了')

#手动添加不换行,end手动将末尾热\n替换成空字符串
print('aaaa',end="")  #aaa\n ----> aaa  
print('bbbb',end="")  #bbb\n ----> bbb
print('cccc',end="\n")  #ccc\n ---->ccc\n

#变量-命名规则
#命名规则-见名知意

import keyword
print(keyword.kwlist)
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#以上是python关键字


