#练习1：寻找“水仙花数”。
for num0 in range(100,1000):
    num = str(num0)
    x = int(num[0])
    y = int(num[1])
    z = int(num[2])
    if int(num) == x**3 + y**3 + z**3:
        print('%s是一个水仙花数'%(num))
    else:
        None



#练习2：寻找完美数(1000以内)
sum = 0
for i in range(2,1000):
    for j in range(i-1,0,-1):
        if i % j == 0:
            sum = sum + j
    if i == sum:
        print('%d是完美数'%i)
    sum = 0
#错误点！！！
#在判断每一个数是否为完美数后，要将sun归零，否则后面数的约数的和会叠加前面的数的约数



#练习3：百鸡百钱
for x in range(20):
    for y in range(33):
        if 5 * x + 3 * y + (100 - x - y ) / 3 == 100:
            print('公鸡%d,母鸡%d,小鸡%d'%(x,y,(100-x-y)))



#练习4：生成“斐波拉切数列”。
a = 1
b = 1
print(a,end = ' ')
while a < 100:
    a , b = b , a + b
    print(a,end = ' ')



#练习5：Craps赌博游戏
from random import randint
print('Now,wo are playing a craps game! please clic "Enter" to start!')
q = input('>')
a = randint(1,6)
b = randint(1,6)
print('you got %d and %d'%(a,b))
if a + b == 7 or a + b == 11:
    print('Good,you are a winer!')
elif a + b == 2 or a + b == 3 or a + b == 12:
    print('Sorry,you are a loser!')
else:
    c = a + b
    while 1:
        print('please clic "Enter" again!')
        w = input('>')
        a = randint(1,6)
        b = randint(1,6)
        print('you got %d and %d'%(a,b))
        if c == a + b:
            print('You are win!')
            break
        if 7 == a + b:
            print('You are faile!')
            break
