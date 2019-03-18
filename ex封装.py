"""
封装
"""


class Car():
    kemu = "猫"

    def __init__(self, name, age, user):
        self.__user = user
        self.__name = name
        self.__age = age

    def get_name(self):
        print(self.__name)

    def set_name(self, name):
        if int(input("请输入主人号：")) == self.__user:
            self.__name = name

    def get_age(self):
        print(self.__age)

    def set_age(self, age):
        if int(input("请输入主人号：")) == self.__user:
            self.__age = age

    @classmethod
    def say_hello(cls):
        print("你好")


cat_0 = Car("琵琶", 18, 5945)
cat_0.get_name()
cat_0.get_age()
cat_0.set_name("小布点")
cat_0.get_name()
cat_0.set_age(19)
cat_0.get_age()
Car.say_hello()
print(Car.kemu)
