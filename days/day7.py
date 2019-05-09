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

练习1：在屏幕上显示跑马灯文字
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
    fileix()
