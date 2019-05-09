#练习1：输入一个数判断是不是素数。
#素数无法整除从2到它平方根向下取整的数
import math

num =int(input('请输入一个整数：'))
num_sqrt = int(math.sqrt(num))
is_prim = True
for x in range(2,num_sqrt+1):
    if num % x == 0:
        is_prim = False
        break
if is_prim and num != 1:
    print('%d是素数'%(num))
else:
    print('%d不是素数'%(num))
#总结：向下圆整：int(num)和floor(num)
#     向上圆整:ceil(num)
#     四舍五入：round(num)
#     %格式化中间不加逗号



#练习2：输入两个正整数，计算最大公约数和最小公倍数。
x = int(input('x ='))
y = int(input('y ='))
if x > y:
    x,y = y,x
for i in range(x,0,-1):
    if x % i == 0 and y % i == 0:
        print('%d和%d的最大公约数为%d'%(x,y,i))
        print('%d和%d的最小公倍数为%d'%(x,y,x * y // i))
        break



#练习3：打印三角形图案。
x1 = 4
x2 = 4
for i in range(1,6):
    print('*' * i)
for i in range(1,6):
    print(' ' * x1 + '*' * i)
    x1 = x1 - 1
for i in range(1,10,2):
    print(' ' * x2 + '*' * i)
    x2 = x2 - 1
#改进
row = int(input('请输入行数：'))
for i in range(row):
    for j in range(i + 1):
        print('*',end = '')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ',end = '')
        else:
            print('*',end = '')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ',end = '')
        else:
            print('*',end = '')
    print('*' * i)
#print()会自动换行  print(,end = '')不换行
