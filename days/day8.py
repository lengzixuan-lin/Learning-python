'''
定义类
在Python中可以使用class关键字定义类，然后在类中通过之前学习过的函数来定义方法，
这样就可以将对象的动态特征描述出来，代码如下所示。
'''
class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def study(self,course_name):
        print('%s is studying %s' %(self.name,course_name))
    def watch_moive(self):
        if self.age < 18:
            print('%s can watch katun'% self.name)
        else:
            print('%s can watch miove'% self.name)
'''
创建和使用对象
当我们定义好一个类之后，可以通过下面的方式来创建对象并给对象发消息。
'''
stu1 = Student('LiLin',23)
stu1.study('python')
stu1.watch_moive()
stu2 = Student('XiaoMing',8)
stu2.study('yuwen')
stu2.watch_moive()
'''
访问可见性问题
在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，
如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头
所以大多数Python程序员会遵循一种命名惯例就是让属性名以单下划线开头来表示属性是受保护的
本类之外的代码在访问这样的属性时应该要保持慎重。
'''
class Test:
    def __init__(self,foo):#限制访问属性
        self.__foo = foo
    def __bar(self):#限制访问方法
        print(self.__foo)
        print('__bar')
def main():
    test = Test('Hello')
    print(test.__foo)#显示没有这个属性，程序将他换了一个名字进行封装
    test.__bar()
if __name__ == '__main__':
    main()
'''
封装：隐藏一切可以隐藏的实现细节，只向外界暴露（提供）简单的编程接口
我们在类中定义的方法其实就是把数据和对数据的操作封装起来了，在我们创建了对象之后，
只需要给对象发送一个消息（调用方法）就可以执行方法中的代码，也就是说我们只需要知道方法
的名字和传入的参数（方法的外部视图），而不需要知道方法内部的实现细节（方法的内部视图)
'''



#练习1：定义一个类描述数字时钟
import time as t
class Clock(object):
    def __init__(self,hours,minites,seconds):
        self._hours = hours
        self._minites = minites
        self._seconds = seconds
    def run(self):
        self._seconds += 1
        if self._seconds == 60:
            self._seconds = 0
            self._minites += 1
            if self._minites == 60:
                self._minites = 0
                self._hours += 1
                if self._hours == 24:
                    self._hours = 0
    def show_time(self):
        return '%d:%d:%d' % (self._hours,self._minites,self._seconds)
        #函数最好是return，外端调用函数时再print。两个print会导致外端多打印出None
def main():
    clock = Clock(15,54,55)
    while 1:
        print(clock.show_time())
        t.sleep(1)#程序延迟1秒再继续执行
        clock.run()
if __name__ == '__main__':
    main()



#练习2：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
from math import sqrt
class Point(object):
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def move_by(self,dx,dy):
        self.x += dx
        self.y += dy
    def distence_to(self,other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2 + dy**2)
    def __str__(self):
        return '(%s,%s)' %(str(self.x),str(self.y))
        #魔法，__str__()用于显示给用户，此时print(p1)相当于print(p1.__str__())其实也不是
def main():
    p1 = Point(3,5)
    p2 = Point()
    print(p1)#调用__str__魔法
    print(p2)
    p2.move_by(-2,3)
    print(p2)
    print(p1.distence_to(p2))
if __name__ == '__main__':#脚本借口，if中为==
    main()
