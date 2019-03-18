"""
演示反恐精英案例
对一个匪徒
分析：
1.定义人类，描述公共属性 life:100  name:姓名要传参
2.定义出英雄与恐怖分子类
3.定义主函数描述枪战过程 main，创建两个对象
4.定义开枪方法，分成两个方法，Hero Is都有
    定义的方法要传入被射击的对象
    被射击对象的生命值要进行减少
5.主程序中调用开枪操作
6.开枪操作后，要在主程序中显示每个人的状态信息
7.定义Person类的__str__方法，用于显示每个人的状态
8.设置开枪操作为反复操作
    再设置停止条件：一方生命值<=0
    停止循环使用break
"""


class Human:

    def __init__(self, name):
        self.name = name
        self.life = 100

    def fire(self, o, x):
        print("%s 向 %s 射击,伤害值 %d" % (self.name, o.name, x))
        o.life -= x

    def __str__(self):
        return "%s当前生命值 %d" % (self.name, self.life)


class Police(Human):
    pass


class Bandit(Human):
    pass


def main_i():
    p = Police("007")
    # x = ("ban", "ban_0", "ban_1")
    # y = ["不要命", "不怕死", "铁头娃"]
    ban = Bandit()
    ban_0 = Bandit()
    ban_1 = Bandit()
    # for j in y:
    #     Bandit(j)
    while True:
        if p.life > 0:
            if ban.life > 0:
                p.fire(ban, 50)
            elif ban_0.life > 0:
                p.fire(ban_0, 60)
            elif ban_1.life > 0:
                p.fire(ban_1, 100)
        if ban.life > 0:
            ban.fire(p, 10)
        if ban_0.life > 0:
            ban_0.fire(p, 20)
        if ban_1.life > 0:
            ban_1.fire(p, 5)
        print(p)
        print(ban, ban_0, ban_1)
        print("--------------")
        if ban.life <= 0 and ban_0.life <= 0 and ban_1.life <= 0:
            print("%s  %s  %s被打死" % (ban.name, ban_0.name, ban_1.name))
            break
        if p.life <= 0:
            print("%s被打死" % p.name)
            break


main_i()
