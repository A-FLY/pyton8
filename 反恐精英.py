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
    -----------------------修复版-----------------------
9.修复英雄的信息显示模式
    状态描述 0 - 1- 70 - 99- 100
    if..elif..   and组合条件
10.修复生命值为负的问题
    射击时如果生命值<伤害值，生命值 = 0，否则正常减生命
"""


class Human:

    def __init__(self, name):
        self.name = name
        self.life = 100

    def fire(self, o, x):
        if self.life - x >= 0:
            print("%s 向 %s 射击，造成伤害值 %d" % (self.name, o.name, x))
            o.life -= x
        else:
            print("%s 向 %s 射击,打死了%s" % (self.name, o.name, o.name))

    def __str__(self):
        return "%s 生命值为 %d" % (self.name, self.life)


class Police(Human):
    def __str__(self):
        if self.life == 100:
            print("%s无伤" % self.name)
        elif 70 < self.life < 100:
            print("%s轻伤" % self.name)
        elif 1 <= self.life <= 70:
            print("%s重伤" % self.name)
        elif self.life < 1:
            print("%s挂了" % self.name)


class Bandit(Human):
    pass


def main_i():
    p = Police("成龙")
    ban = Bandit("001匪")
    while True:
        if p.life > 0:
            p.fire(ban, 40)
        if ban.life > 0:
            ban.fire(p, 10)
        ban.__str__()
        p.__str__()
        print("------------")
        if ban.life <= 0:
            print("%s 被 %s 打死了" % (ban.name, p.name))
            break
        if p.life <= 0:
            print("%s 被 %s 打死了" % (p.name, ban.name))
            break


main_i()
