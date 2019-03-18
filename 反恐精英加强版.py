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
   --------------------------------------------------------
11.创建三个恐怖份子对象
    三个对象都要开枪，三个对象都要打印状态
12.修复结束条件为三个恐怖份子都死亡
    三个满足同时死亡 and
13.解决向三个恐怖份子开枪的问题
    随机数：random
    步骤1:使用random    import random  必须写在所有程序的前面
    步骤2：使用random.randint(1,3) 可以产生1到3的随机数
    产生一个随机数，判断是几就向几号敌人开枪
"""

import random


class Human:
    def __init__(self, name):
        self.name = name
        self.life = 100

    def fire(self, obj, x):
        if obj.life - x > 0:
            print("%5s向 %5s 射击，造成 %d 伤害" % (self.name, obj.name, x))
            obj.life -= x
        else:
            obj.life = 0
            print("%5s挂了，生命值为0" % obj.name)

    def __str__(self):
        return "%s当前生命值为 %d" % (self.name, self.life)


class Police(Human):
    def __str__(self):
        ob = ""
        if self.life == 100:
            ob = "无伤"
        elif 70 < self.life < 100:
            ob = "轻伤"
        elif 0 < self.life <= 70:
            ob = "重伤"
        else:
            ob = "死了"
        return "%s当前状态为%s" % (self.name, ob)


class Bandit(Human):
    pass


def main_i():
    p = Police("007")
    b_1 = Bandit("1号匪")
    b_2 = Bandit("2号匪")
    b_3 = Bandit("3号匪")
    while True:
        if p.life <= 0:
            print("%s  被击杀" % p.name)
            break
        if b_1.life <= 0 and b_2.life <= 0 and b_3.life <= 0:
            print("%s  被击杀" % b_1.name)
            break
        if p.life > 0:
            rm = random.randint(1, 3)
            if rm == 1:
                p.fire(b_1, 50)
            elif rm == 2:
                p.fire(b_2, 50)
            elif rm == 3:
                p.fire(b_3, 50)
        b_1.fire(p, 10)
        b_2.fire(p, 10)
        b_3.fire(p, 10)
        print(p)
        print(b_1)
        print(b_2)
        print(b_3)
        print("---------------")


main_i()
