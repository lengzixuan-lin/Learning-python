def main():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    list3 = sorted(list1, reverse=True)
    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, key=len)
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    # 给列表对象发出排序消息直接在列表对象上进行排序
    list1.sort(reverse=True)
    print(list1)


if __name__ == '__main__':
    main()

import sys
def main():
    f = [x for x in range(1,10)]
    print(f)
    f = [x + y for x in 'ABCDEF' for y in '123']
    print(f)
    f = [x**2 for x in range(1,1000)]
    print(sys.getsizeof(f))
    print(f)
    f = (x**2 for x in range(1,1000))
    print(sys.getsizeof(f))
    print(f)
    for val in f:
        print(val)

if __name__ == '__main__':
    main()

def fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b, a + b
        yield a
def main():
    for val in fib(20):
        print(val)

if __name__ == '__main__':
    main()

#练习1：在屏幕上显示跑马灯文字
import os
import time
def main():
    content = '北京欢迎你......'
    while True:
        os.system('cls') #清空屏幕
        print(content)
        time.sleep(2)   #休眠2秒
        content = content[1:] + content[0]#循环字符串
if __name__ =="__main__":
    main()

import os
import time
def main():
    content = '翻过这座山，你就会知道挖掘机附系点什么！'
    while 1:
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]
if __name__ == "__main__":
    main()


#练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
import random as r
def generetor_code(code_len = 4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    all_len = len(all_chars) - 1#计算出最大索引号
    code = ''
    for _ in range(code_len):#生成数
        index = r.randint(0,all_len)#随机生成一个索引
        code += all_chars[index]#将索引值添加到code中
    return code
if __name__ == '__main__':
    print(generetor_code(7))



#练习3：设计一个函数返回给定文件名的后缀名。
def fileix(filename,has_dot = False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''
if __name__ == '__main__':
    print(fileix())


#练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
def max2(list):
    list.sort(reverse = True)#自我排序为sort，传给其他变量a =sorted(list)
    m1,m2 = list[0],list[1]
    return m1,m2
if __name__ == '__main__':
    print(max2([2,3,1,4,9,6,7]))



#练习5：计算指定的年月日是这一年的第几天
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 ==0

def which_days(year,month,date):
    days_of_month =[
        [31,28,31,30,31,30,31,31,30,31,30,31],
        [31,29,31,30,31,30,31,31,30,31,30,31]
    ][is_leap_year(year)] #选择变量所指向的列表，True为后一个列表
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date
def main():
    print(which_days(2019,3,17))
    print(which_days(1996,3,17))
if __name__ == '__main__':
    main()



#练习6：打印杨辉三角。(待改正，非三角)
def main():
    num = int(input('please input your row:'))
    yh = [[]] * num#二维列表，num行[]
    for row in range(len(yh)):#循环n行次
        yh[row] = [None] * (row + 1)#在n行设置n个空值元素
        for col in range(len(yh[row])):#在第n行进行n次循环
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row-1][col-1]
            print(yh[row][col],end = '\t')
        print()
if __name__ == '__main__':
    main()



#综合练习1：双色球选号
from random import randrange,randint,sample
def dispaly(balls):
    for index,ball in enumerate(balls):#enumerate函数生成的序列中，每个元素为(索引号，元素)
        if index == len(balls) - 1:
            print('|',end = ' ')
        print('%02d'%ball,end = ' ')#不是遍历两次，而是最后一次先打印if，再打印数字，这不是if else语句！！！
    print()

def random_select():
    red_balls = [x for x in range(1,34)]
    selected_num = []
    selected_num = sample(red_balls,6)#在red_balls中随机选择6个元素，以list返回
    selected_num.sort()
    selected_num.append(randint(1,16))#生成随机整数randint(1,16)，不加range
    return selected_num

def main():
    n = int(input('生成注数：'))
    for _ in range(n):
        dispaly(random_select())

if __name__ == '__main__':
    main()



#综合案例2：约瑟夫环问题
def main():
    persons = [True] * 30#定义30个True列表
    count , num , index = 0,0,0#count为记录死人数，num记录报道号，index记录原始位置
    while count < 15:
        if persons[index]:#索引的元素为True时，num向前走一步
            num += 1#活人报道，死人不报道
            if num == 9:#当报道为9时，扔下海，死人+1，报道重置
                persons[index] = False#找出列表中的非基督教位置
                count += 1
                num = 0
        index += 1#无论上一次索引的元素是否为True，index都向前走一步
        index %= 30#索引在30以内循环
    for person in persons:
        print('基' if person else '非', end = ' ')
if __name__  ==  '__main__':
     main()
#简单写法
def main():
    persons = [x for x in range(1, 31)]
    dropped = 0
    while (dropped < 15):
        persons = persons[9:] + persons[0:8]#记住切片与rang()的前闭后开
        dropped += 1
    print ('基督徒的原始位置为：')
    print (sorted(persons))
if __name__ == '__main__':
    main()



#综合案例3：井字棋游戏
import os
def print_board(board):#打印实时棋盘
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-+-+-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-+-+-')
    print(board[7]+'|'+board[8]+'|'+board[9])

def main():
    init_board = {
    1:' ',2:' ',3:' ',
    4:' ',5:' ',6:' ',
    7:' ',8:' ',9:' '
    }#初始化棋盘，避免重启程序
    begain = True
    while begain:
        begain = False
        curr_board = init_board.copy()
        os.system('cls')#清屏，避免一个屏幕出现多个棋盘
        count = 0
        trun = 'x'
        print_board(curr_board)#显示初始棋盘
        while count < 9:
            move = int(input('轮到%s走，请输入位置：'% trun))#输入下一步走棋位置
            if curr_board[move] == ' ':#判断该位置是否为空，并计数，走棋
                count += 1
                curr_board[move] = trun
                if trun == 'x':#下一步换另一方走棋
                    trun = 'o'
                else:
                    trun = 'x'
            os.system('cls')#清空上一步走棋屏幕
            print_board(curr_board)#打印这一步的走棋
        select = input('Try again?')
        begain = True if select == 'yes' else False

if __name__ == '__main__':
    main()
