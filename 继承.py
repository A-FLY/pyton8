"""
继承
"""


class Zoology:
    life = "huode"
    shengao = 178

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def sleep(self):
        print("睡觉")


class people(Zoology):

    def __init__(self, name, sex, cloth):
        super.__init__(name, sex)
        self.cloth = cloth
