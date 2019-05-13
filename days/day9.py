'''
属性私有化，是为了避免外部代码对属性的随意访问修改
利用@property访问器和@name.setter修改器对class的私有属性进行访问和设置，是为了简化设置
属性的方法，并重复利用代码时让属性的设置有一定的值域限制

将类方法变为类属性
疑问：绕了一圈，还不如将类公有化，直接访问和修改？
你也许会问，原先那种直接通过bart.score = 59也可以修改啊，为什么要定义一个方法大费周折？
因为在方法中，可以对参数做检查，避免传入无效的参数
'''
class Person(object):
    __slots__ = ('_name','_age','_gender')#__slots__魔法限定class对写一个子对象的属性绑定量
    def __init__(self,name,age):
        self._name = name#属性 = 变量
        self._age = age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):#在设置中还可增加设置条件
        self._age = age
    def paly(self):
        if self._age  >= 18:
            print('%s can watch miove'% self._name)
        else:
            print('%s can not watch miove'% self._name)

def main():
    person = Person('Bob',16)
    print(person.name)#添加@property后，访问从类方法变为类属性，不用写成person.name()
    print(person.age)
    person.paly()
    person.age = 23#不用写成person.age(23)
    person.paly()
    person._gender = 'male'
    person._is_gay = 'True'#不能设置这个属性
    # print(person._gender)
    # person._gender = 'No'
    # print(person._gender)
if __name__ == '__main__':
    main()

'''
静态方法：通过给类发消息，来判断所传递的参数是否能构成类的一个实例化对象
类静态方法的写法：@staticmethod + 函数的定义
调用方式：类.函数
比如：传递三个参数，判断他们能否构成一个三角形，再计算周长和面积
'''
from  math  import sqrt
class Triangle(object):
    def __init__(self,a,b,c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a,b,c):
        return a+b>c and a+c>b and b+c>a
    def perimeter(self):
        return self._a + self._b + self._c
    def area(self):
        half = self.perimeter()/2
        return sqrt(half * (half - self._a) * \
                (half - self._b) * (half - self._c))
def main():
    a,b,c = 3,4,5
    if Triangle.is_valid(a,b,c):#静态方法给类发消息
        t = Triangle(a,b,c)
        print(t.perimeter())#动态方法给对象发消息
        print(t.area())
if __name__ == '__main__':
    main()


'''
类方法：通过@classmethod给类发消息，来获取类的对象的信息，创建对象
'''
from time import sleep,localtime,time
class Clock(object):
    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    @classmethod
    def now(cls):#类方法格式
        ctime = localtime(time())#将当地时间赋给ctime
        return cls(ctime.tm_hour,ctime.tm_min,ctime.tm_sec)
    def run(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minite = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0
    def show_time(self):
        return '%02d:%02d:%02d'%(self.hour,self.minute,self.second)
def main():
    clock = Clock.now()#调用用类方法给予对象信息
    while 1:
        print(clock.show_time())
        sleep(1)
        clock.run()
if __name__ == '__main__':
    main()


'''
类之间的关系：
1.is-a关系也叫继承或泛化，比如学生和人的关系、手机和电子产品的关系都属于继承关系。
2.has-a关系通常称之为关联，比如部门和员工的关系，汽车和引擎的关系都属于关联关系；关联关系如果是整体和部分的关联，那么我们称之为聚合关系；如果整体进一步负责了部分的生命周期（整体和部分是不可分割的，同时同在也同时消亡），那么这种就是最强的关联关系，我们称之为合成关系。
3.use-a关系通常称之为依赖，比如司机有一个驾驶的行为（方法），其中（的参数）使用到了汽车，那么司机和汽车的关系就是依赖关系。
'''


'''
继承：子类可以从父类继承属性、方法和装饰器属性
'''
class Person(object):
    def __init__(self,name,age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        self._age = age
    def paly(self):
        if self._age >= 18:
            print('%s can get out'% self._name)
        else:
            print('%s can not get out'% self._name)
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)#属性的继承格式  super.__init__(继承参数)
        self._grade = grade
    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self,grade):
        if not isinstance(grade,int):
            raise ErrorValue('The grade is not int!')#
        elif grade < 0 or grade > 100:
            raise ErrorValue('The grade is out of range!')
        else:
            self._grade = grade
    def study(self,course):
        print('%s is studying %s'%(self._name,course))
def main():
    stu = Student('lilin',16,70)
    print(stu.name)#继承父类的装饰器
    print(stu.age )
    print(stu.grade )
    stu.paly()#继承父类的方法
    stu.age = 23
    stu.grade = 90 #子类自己的装饰器，并且有数据限制
    stu.paly()
    stu.study('python')
if __name__ == '__main__':#
    main()

'''
多态：子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本
'''
from abc import ABCMeta,abstractmethod
class Pet(object,metaclass=ABCMeta):
    def __init__(self,nick_name):
        self._name = nick_name
    @abstractmethod#定义一个抽象类只能被继承，不能实例化
    def make_vioce(self):
        print('%s is make vioce!'% self._name)
# class Dog(Pet):#无法继承父类的抽象方法
#     pass
class Ant(Pet):
    def make_vioce(self):#覆盖父类的方法
        print('%s is yayayay'% self._name)
class Cat(Pet):
    def make_vioce(self):
        print('%s is miaomiaomiao'% self._name)
def main():
    pets = [Ant('hei'),Cat('miao')]
    for pet in pets:
        pet.make_vioce()
if __name__ == '__main__':
    main()
'''
案例1：奥特曼打小怪兽

'''
