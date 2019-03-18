"""
面向对象的名称总结
"""

"""
1. 变量称呼

    全局变量
    局部变量
    公有变量
    独有变量
    私有变量
    类变量
    
    对象变量（属性）
"""


class User:
    country = "类属性"
    __title = "类属性,私有属性"

    def __init__(self):
        self.name = "实例属性，对象属性，对象变量，公有属性"
        self.__age = "私有属性，对象属性"
        info = "局部变量"

    def test(self):
        self.address = "对象方法，实例方法"
        email = "局部变量"


u = User()
u.gender = "独有属性"

city = "全局变量"
info = "全局变量"


def test():
    info = "局部变量"
    global city
    city = "全局变量"


"""
2. 方法和函数的称呼
    实例方法
    类方法
    静态方法
    函数
    
    初始化方法
    魔法方法
"""


class User:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        print("初始化方法")

    def instance_method(self, info):
        message = info
        print("对象方法，成员方法")

    @classmethod
    def cls_method(cls):
        print("类方法")

    @staticmethod
    def static_func():
        print("静态方法")


def hello():
    print("函数")
