"""
定义类
"""


class RenWu:
    def __init__(self):
        self.name = None
        self.age = None
        self.sex = None

    def eat(self, times):
        if times == 12:
            print("吃饭")

    def sleep(self):
        print("开心")

    def wanyouxi(self):
        print("wan")


ren1 = RenWu()
ren1.age = 18
ren1.name = "瑞雯"
ren1.sex = "女"
ren1.eat(12)
ren1.sleep()
