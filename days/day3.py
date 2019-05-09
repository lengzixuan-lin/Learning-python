#练习1：英制单位与公制单位互换
value = float(input('请输入长度：'))
unit = input("请输入单位：")
if unit == 'in' or unit == '英寸':
    print('%.2f英寸 = %.2f厘米' %(value,value * 2.54))
elif unit == 'cm' or unit == "厘米":
    print('%.2f厘米 = %.2f英寸' %(value,value / 2.54))
else:
    print('请输入正确的单位！')



#练习2：掷骰子决定做什么
from random import randint
face = randint(1,6)
if face == 1:
    result = '吃饭'
elif face == 2:
    result = '喝水'
elif face == 3:
    result = '唱歌'
elif face == 4:
    result = '写诗'
elif face == 5:
    result = '看书'
else:
    result = '写代码'
print(result)



#练习3：百分制成绩转等级制
grade = float(input('请输入成绩：'))
if grade >= 90:
    result = 'A'
elif grade >= 80:
    result = 'B'
elif grade >=70:
    result = 'C'
elif grade >= 60:
    result = 'D'
else:
    result = 'E'
print('%s is get %s'%(grade,result))#使用%进行格式化字符串时%.2f %s   %(参数)



#练习4：输入三条边长如果能构成三角形就计算周长和面积
import math
print('请输入三条边长')
a = float(input('a ='))
b = float(input('b ='))
c = float(input('c ='))
if a + b > c and a + c > b and b + c > a:
    print('周长为：%f' % (a + b + c) )
    q = a + b + c
    area = math.sqrt(q * (q - a) * (q - b) * (q - c))
    print('面积为：%f' % (area) )
else:
    print('无法构成三角形！')



#练习5：个人所得税计算器。
salary = float(input('请输入你的月薪：'))
insurance = float(input('每月五险一金：'))
diff = salary - insurance - 3500
if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 1500:
    rate = 0.03
    deduction = 0
elif diff < 4500:
    rate = 0.1
    deduction = 105
elif diff < 9000:
    rate = 0.2
    deduction = 555
elif diff < 35000:
    rate = 0.25
    deduction = 1005
elif diff < 55000:
    rate = 0.3
    deduction = 2755
elif diff < 80000:
    rate = 0.35
    deduction = 5505
else:
    rate = 0.45
    dedution = 13505
tax = abs(diff * rate - deduction)
print('个人所得税为：',tax)
print('税后收入为：',diff + 3500 - tax)
