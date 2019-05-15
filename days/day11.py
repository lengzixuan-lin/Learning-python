# '''
# 文件与异常
# '''
# def main():
#     f = None
#     try:#标记可能出现异常的位置
#         f = open('test.txt','r')#r为只读文件，文件不存在时，无法open
#         print(f.read())
#     except:#对异常的处理
#         print('test fail')
#     finally:#无论是否发生异常都执行
#         if f:
#             f.close()#保存并关闭文件，释放外部资源
# if __name__ == "__main__":
#     main()
#
# import time
# def main():# 执行with操作并将操作的返回值赋给f，再关闭文件
#     with open('test.txt','r') as f:#必须加上文件的后缀
#         print(f.read())#f只能执行一次操作
#     with open('test.txt','r') as f:
#         for line in f:
#             print(line,end = '')
#             time.sleep(0.5)
#     print()
#     with open('test.txt','r') as f:
#         lines = f.readlines()#将文件的每行信息以字符串的方式组成一个list赋给lines
#         print(lines)
# if __name__ == '__main__':
#     main()

# '''
# 写文件：open('test.txt'.'w'),文件不存在时会自动创建一个文件
# '''
# from math import sqrt
# def is_prim(n):
#     assert n > 0
#     for factor in range(2,int(sqrt(n) + 1 )):
#         if n % factor == 0:
#             return False
#     return True if n !=1 else False
# def main():
#     filenames = ['a.txt','b.txt','c.txt']
#     fs_list = []
#     try:
#         for filename in filenames:
#             fs_list.append(open(filename,'w'))
#         for num in range(1,10000):
#             if is_prim(num):
#                 if num < 100:
#                     fs_list[0].write(str(num) + '\n')
#                 elif num < 1000:
#                     fs_list[1].write(str(num) + '\n')
#                 else:
#                     fs_list[2].write(str(num) + '\n')
#     except IOError as ex:
#         print(ex)
#         print('writting fail!')
#     finally:
#         for fs in fs_list:
#             fs.close()
#     print('Writting succes! Let me see the file')
#     p1 = open('a.txt')
#     p2 = open('b.txt')
#     p3 = open('c.txt')
#     print(p1.readlines())
#     print('-----------------------------------------------------')
#     print(p2.readlines())
#     print('-----------------------------------------------------')
#     print(p3.readlines())
# if __name__ == '__main__':
#     main()
# '''
# 读写二进制文件
# '''
# def main():
#     try:
#         with open('诗.png','rb') as fs1:#读写二进制图片文件时，open方式为'rb'、'wb'
#             date = fs1.read()
#             print(type(date))
#         with open('喜欢2.png','wb') as fs2:
#             fs2.write(date)
#     except:
#         print('读写出错！')
# if __name__ == '__main__':
#     main()
'''
JSON是纯文本,可以将数据结构转化为Json格式保存
数据结构的序列化（数据转化为存储的字节）：
dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
反序列化（字节转化为数据）
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象
'''
import json
def main():
    mydict = {
        'name':'lilin',
        'age':'23',
        'gender':'male',
        'message':[
            {'first_school':'panzhihua','years':'4'},
            {'second_school':'jiangsu','years':'3'}
        ]
    }
    try:
        with open('json.txt','w') as fs:
            json.dump(mydict,fs)
    except:
        print('Error')
if __name__ == '__main__':
    main()
