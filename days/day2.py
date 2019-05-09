# f = float(input("请输入华氏温度："))
# c = (f-32)/1.8
# print("%.2f华氏度 = %.2f摄氏度"%(f,c))
#
#
#
# import math as m
# r = float(input("请输入圆的半径："))
# c = 2 * m.pi * r
# s = m.pi * r**2
# print("圆的周长为{:.2f},面积为{:.2f}".format(c,s))
#
#
#
# year = int(input("请输入年份："))
# is_leap = (year % 4 == 0 and year % 100 != 0
#            or year % 400 == 0)
# if is_leap == True:
#     print(f"{year} 是闰年")
# else:
#     print(f"{year} 不是闰年")
#
#
# a = 100
# b = str(a)
# c = 123.456
# d = str(c)
# e = "123"
# f = int(e)
# g = "123.456"
# h = float(g)
# i = False
# j = str(i)
# k = 'hello'
# l = bool(k)
# print(a)
# print(type(a))
# print(b)
# print(type(b))
# print(c)
# print(type(c))
# print(d)
# print(type(d))
# print(e)
# print(type(e))
# print(f)
# print(type(f))
# print(g)
# print(type(g))
# print(h)
# print(type(h))
# print(i)
# print(type(i))
# print(j)
# print(type(j))
# print(k)
# print(type(k))
# print(l)
# print(type(l))


str1 = 'hello, world!'
print('字符串的长度为：',len(str1))
print('字符串的首字母大写：',str1.title())
print("首字母大写后的str1:",str1)
print('字符串大写：',str1.upper())
print('大写后的str1:',str1)

print('字符串是否为大写',str1.isupper())
print('字符串是不是以hello开头：',str1.startswith('hello'))
print('字符串是不是以hello结尾：',str1.endswith('hello'))
str2 = '- \u9a86\u660a'
str3 = str1.title() + ' ' + str2.lower()
print(str3)
