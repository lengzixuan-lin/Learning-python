def foo():
    pass


def bar():
    pass


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()

#练习1：实现计算求最大公约数和最小公倍数的函数。
def fun(x,y):
    if x > y:
        x,y = y,x
    for _ in range(x,0,-1):
        if x % _ == 0 and y % _ == 0:
            print("%d和%d的最大公约数为%d"%(x,y,_))
            print("%d和%d的最小公倍数为%d"%(x,y,x * y / _))
            break

if __name__ == '__main__':#被引用时这个部分不会执行，因为此时__name__ == 'day6'
    fun(15,35)            #但是在解释器中执行时，__name__ == '__main__' ,此时会执行



#练习2：实现判断一个数是不是回文数的函数。
def fun(x):
    y = 0
    temp = x
    while temp > 0:
        y *= 10
        y += (temp % 10)
        temp //= 10
    if x == y:
        print('%d是回文'%x)
    else:
        print('%d不是回文'%x)
fun(int(input('>')))




#练习3：实现判断一个数是不是素数的函数。
def fun(x):
    for i in range(2,x):
        if x % i == 0 or x == 1:
            return print('%d不是素数'%x)
    return print('%d是素数'%x)
fun(int(input('>')))
#总结：利用return语句来终止函数继续运行，函数只返回第一个return



#练习4：写一个程序判断输入的正整数是不是回文素数。
def fun(x):
    temp = x
    y = 0
    while temp > 0:
        y *= 10
        y += (temp % 10)
        temp //= 10
    if x != y:
        return print('%d不是回文数'%x)
    else:
        for i in range(2,x):
            if x % i ==0 or x == 1:
                return print('%d不是素数'%x)
    return print('%d是回文素数'%x)
fun(int(input('请输入一个正整数：')))
#函数变量的作用域
#Python查找一个变量时会按照“局部作用域”、“嵌套作用域”、“全局作用域”和“内置作用域”的顺序进行搜索
#函数内部可以调用外部的变量，但这个变量的改变只作用于函数的内部，函数外，变量的值不变
#可是利用关键字global 和nonlocal来从内部函数修改外部变量的值

#python 模板(这样写，既能直接作为脚本在解释器中运行，又能作为模块，因为别的脚本中)
def main():
    pass

if __name__ == '__main__':
    main()
