"""
手机案例
    手机电量默认是100
    打游戏每次消耗电量10
    听歌每次消耗电量5
    打电话每次消耗电量4
    接电话每次消耗电量3
    充电可以为手机补充电量

"""


class Phone:
    def __init__(self):
        self.power = 100

    def game(self):
        self.power -= 10
        print("游戏中，剩余电量：%d" % self.power)

    def song(self):
        self.power -= 5
        print("听歌中，剩余电量：%d" % self.power)

    def call(self):
        self.power -= 4
        print("打电话中，剩余电量：%d" % self.power)

    def answer(self):
        self.power -= 3
        print("接电话，剩余电量：%d" % self.power)

    def charg(self, electric):
        self.power += electric
        print("充电完毕，剩余电量：%d" % self.power)

    def __str__(self):
        return "这是一部手机使用情况"


p = Phone()
print(p)
p.game()
p.game()
p.game()
p.charg(20)
p.call()
p.answer()
p.song()
