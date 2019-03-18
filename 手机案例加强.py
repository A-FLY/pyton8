"""
手机案例
    手机电量默认是100
    打游戏每次消耗电量10
    听歌每次消耗电量5
    打电话每次消耗电量4
    接电话每次消耗电量3
    充电可以为手机补充电量
要求：
    手机耗电操作前要先判定电量是否足够完成此项任务
    手机充电操作不能充电超过最大值
"""


# class Phone:
#     """
#     创建一个电话类
#     """
#     def __init__(self):
#         self.power = 100
#
#     def game(self):
#         if self.power > 10:
#             self.power -= 10
#             print("游戏中，剩余电量：%d" % self.power)
#         else:
#             print("电量不足，无法打游戏")
#
#     def song(self):
#         if self.power > 5:
#             self.power -= 5
#             print("听歌中，剩余电量：%d" % self.power)
#         else:
#             print("电量不足，无法听歌")
#
#     def call(self):
#         if self.power > 4:
#             self.power -= 4
#             print("打电话中，剩余电量：%d" % self.power)
#         else:
#             print("电量不足，无法打电话")
#
#     def answer(self):
#         if self.power > 3:
#             self.power -= 3
#             print("接电话，剩余电量：%d" % self.power)
#         else:
#             print("电量不足，无法接听")
#
#     def charg(self, electric):
#         if self.power + electric < 100:
#             self.power += electric
#             print("充电完毕，剩余电量：%d" % self.power)
#         else:
#             print("能量已满，请及时拔掉电源")
#
#     def __str__(self):
#         return "这是一部手机使用情况"
#
#
# p = Phone()
# print(p)
# i = 1
# while i < 10:
#     p.game()
#     i += 1
# p.game()
# p.song()
# p.answer()
# p.call()
# p.game()
# p.charg(70)
# p.game()
# p.song()
# p.answer()
# p.call()

class Phone:
    def __init__(self):
        self.power = None

    def game(self):
        if self.power > 10:
            self.power -= 10
            print("游戏中，剩余电量：%d" % self.power)
        else:
            print("无法打游戏，电量不足10")

    def song(self):
        if self.power > 5:
            self.power -= 5
            print("听歌中，剩余电量：%d" % self.power)
        else:
            print("无法听歌，电量不足5")

    def call(self):
        if self.power > 4:
            self.power -= 4
            print("打电话中，剩余电量：%d" % self.power)
        else:
            print("无法打电话，电量不足4")

    def answer(self):
        if self.power > 3:
            self.power -= 3
            print("接电话，剩余电量：%d" % self.power)
        else:
            print("无法接电话，电量不足3")

    def charg(self, electric):
        if self.power + electric < 100:
            self.power += electric
            print("充电完毕，剩余电量：%d" % self.power)
        else:
            print("电量充满 100")

    def __str__(self):
        return "这是一部手机使用情况"


p = Phone()
p.power = 100
i = 1
while i < 12:
    p.game()
    i += 1
p.charg(70)
p.answer()
p.call()
p.song()
