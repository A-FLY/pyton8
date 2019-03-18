"""
案例斗地主
分析：
1.扑克牌作为对象呈现
2.创建未发牌的牌堆的列表
3.创建三个玩家牌堆的列表
4.创建底牌的元组
5.最原始的牌堆初始化，将54张牌加入到牌堆
6.创建洗牌操作
7.创建发牌操作

"""

# import random
#
#
# class Poke:
#     """
#     扑克牌
#     """
#
#     def __init__(self, flower, num):
#         self.flower = flower
#         self.num = num
#
#     def __str__(self):
#         # 生成牌的地方
#         return "%s%s" % (self.flower, self.num)
#
#
# class PokeManager:
#     """
#     荷官
#     """
#     pokes = []
#     player1 = []
#     player2 = []
#     player3 = []
#     base = None
#
#     # 初始化牌堆
#     def init_pokes(self):
#         flowers = ["♠", "♣", "♥", "♦"]
#         nums = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
#         kings = {'big': '大王', 'small': '小王'}
#         for flower in range(len(flowers)):
#             for num in range(len(nums)):
#                 # 下面两行代码生成一张牌，给牌堆添加，P 中一直是一张牌
#                 p = Poke(flowers[flower], nums[num])
#                 PokeManager.pokes.append(p)
#         # 这一步没有生成一张牌，下行代码等于直接  给牌堆中追加了一个字符串“大王”
#         PokeManager.pokes.append(kings['big'])
#         PokeManager.pokes.append(kings['small'])
#
#     # 发牌
#     def send_poke(self):
#         for i in range(17):
#             self.player1.append(self.pokes.pop(0))
#             self.player2.append(self.pokes.pop(0))
#             self.player3.append(self.pokes.pop(0))
#         self.base = tuple(self.pokes)
#
#     # 洗牌
#     def wash_poke(self):
#         for i in range(54):
#             x = random.randint(0, 53)
#             self.pokes[i], self.pokes[x] = self.pokes[x], self.pokes[i]
#
#     # 展示玩家手牌
#     def show_palyer(self):
#         print("玩家一：")
#         for i in self.player1:
#             print(i, end=' ')
#         print()
#         print("玩家二：")
#         for i in self.player2:
#             print(i, end=' ')
#         print()
#         print("玩家三：")
#         for i in self.player3:
#             print(i, end=' ')
#         print()
#         print("底牌：")
#         for i in self.base:
#             print(i, end=' ')
#         print()
#
#     # 展示牌堆
#     def show(self):
#         for i in self.pokes:
#             print(i, end='  ')
#         print()
#
#
# PM = PokeManager()
# PM.init_pokes()
# PM.show()
# PM.wash_poke()
# PM.show()
# PM.send_poke()
# PM.show_palyer()


import random


class Poke:
    def __init__(self, flower, num):
        self.flower = flower
        self.num = num

    def __str__(self):
        return "%s%s" % (self.flower, self.num)


class PokeManage:
    pokes = []
    player1 = []
    player2 = []
    player3 = []
    last = None

    # 初始化牌堆
    def init_poke(self):
        print("生成扑克")
        flowers = ["♠", "♥", "♣", "♦"]
        nums = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        kings = {'big': '大王', 'small': '小王'}
        for flower in flowers:
            for num in nums:
                p = Poke(flower, num)
                self.pokes.append(p)
        p = Poke(kings['big'], "")
        self.pokes.append(p)
        p = Poke(kings['small'], '')
        self.pokes.append(p)

    # 洗牌
    def wash_poke(self):
        print("----------------洗牌中--------------------")
        for i in range(len(self.pokes)):
            x = random.randint(0, 53)
            self.pokes[i], self.pokes[x] = self.pokes[x], self.pokes[i]

    # 发牌
    def send_poke(self):
        print("发牌")
        for i in range(17):
            self.player1.append(self.pokes.pop(0))
            self.player2.append(self.pokes.pop(0))
            self.player3.append(self.pokes.pop(0))
        self.last = tuple(self.pokes)

    # 展示玩家手牌
    def show_player(self):
        print("玩家一：")
        for i in self.player1:
            print(i, end='  ')
        print()
        print("玩家二：")
        for i in self.player2:
            print(i, end='  ')
        print()
        print("玩家三：")
        for i in self.player3:
            print(i, end='  ')
        print()
        print("底牌：")
        for i in self.last:
            print(i, end='  ')
        print()

    # 展示牌堆
    def show(self):
        print("展示牌堆")
        for i in self.pokes:
            print(i, end='  ')
        print()


PM = PokeManage()
PM.init_poke()
PM.show()
PM.wash_poke()
PM.show()
PM.send_poke()
PM.show_player()
