'''
正则表达式
验证输入的用户名（由字母、数字、下划线组成）和qq（非0开头的5-12数字）是否有效
'''
import re
def main():
    username = input('Please input your name:')
    qq = input('Please input your qq:')
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$',username)
    m2 = re.match(r'^[1-9]\d{4,11}$',qq)
    if not m1:
        print('invalid username')
    if not m2:
        print('invalid qq')
    if m1 and m2:
        print('Good')
if __name__ == '__main__':
    main()
'''
正则表达式的具体使用访问收藏页面
'''
