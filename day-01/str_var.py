""" 
a='11'
b='22'
c='33'
print('aaaa'+a+'bbbb'+b+'cccc'+c)
以上是传统加号拼接

%s 占位符 s->string
在%(变量1,变量2)
print('aaaa%s,bbbb%s,cccc%s' %(a,b,c))

"""

a='111'
b='222'
c='333'
print('aaaa'+a+',bbbb'+b+',cccc'+c)
print('aaaa%s,bbbb%s,cccc%s' %(a,b,c))

''' 
str() 内置的函数，将其他类型强制转换为字符串

'''

age=18
print('年龄：'+str(age))
print('年龄：%s' % age) #%s ->str简写;底层str()


''' 
%d -> digit 数字;底层int() -> 取整

'''
age=18.5
print('年龄是：%d' % age) #打印出来的是整型 18

''' 
%f -> 浮点型
%.1f ->保留小数点后几位；数字四舍五入
%.2f ->保留小数点后几位；数字四舍五入
'''
salary=8889.568
print('我的薪水是：%.2f' % salary)
