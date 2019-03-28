"""
飞机大战
"""
import sys  # 导入系统模块
import random  # 导入多个敌机是位置为随机数

import pygame  # TODO 5.导入pygame模块
import pygame.locals  # TODO 13.导入pygame本地策略

APP_ICON = "res/app.ico"  # 1.提取游戏LOGO图标地址为常量
IMG_BACKGROUND = "res/img_bg_level_2.jpg"  # 2.提取背景图片路径地址为常量
IMG_ENEMY = "res/img-plane_1.png"  # 初始化敌机图片


# 创建一个窗口元素模型类
class Model:
    win = None  # 主窗体对象，用于模型访问使用

    def __init__(self, img_path, x, y):  # TODO 16.制作背景构造方法，传入图片路径img_path，x,y
        self.img = pygame.image.load(img_path)  # 背景图片
        self.x = x  # 窗体中放置的x坐标
        self.y = y  # 窗体中放置的y坐标

    def display(self):
        self.win.blit(self.img, (self.x, self.y))  # 填充图片到窗体中


# 背景类
class Background(Model):
    # def __init__(self, img_path, x, y):  # TODO 16.制作背景构造方法，传入图片路径img_path，x,y
    #     self.img = pygame.image.load(img_path)
    #     self.x = x
    #     self.y = y
    def background_move(self):  # 更新高度的引用
        if self.y <= Game.WIN_HEIGHT:  # 如果没有超出屏幕就正常移动
            self.y += 1  # 纵坐标自增1
        else:  # 如果超出屏幕，恢复图片位置为原始位置
            self.y = 0  # 纵坐标回0

    def display(self):  # 覆盖父类display方法，做辅助背景贴图
        # self.win.blit(self.img, (self.x, self.y))
        super().display()  # 原始背景贴图
        self.win.blit(self.img, (self.x, self.y - Game.WIN_HEIGHT))  # 更新高度的引用  .辅助背景即将原始背景图片展示第二遍，坐标位置与第一遍展示上下拼接吻合


# 玩家类
class PlayerPlane(Model):
    pass


# 敌机类
class EnemyPlane(Model):

    def enemy_move(self):
        if self.y <= Game.WIN_HEIGHT:
            self.y += 3
        else:
            self.y = -100


# 子弹类
class Bullet(Model):
    pass


# 游戏类
class Game:
    # TODO 1.主程序，运行游戏入口
    WIN_WIDTH = 512  # 定义窗体宽度常量
    WIN_HEIGHT = 768  # 定义窗体高度常量

    def run(self):
        self.frame_init()  # TODO 4.执行窗体初始化

        self.model_init()  # 窗体元素执行调取方法

        while True:  # TODO 7.构造反复执行的机制，刷新窗体，使窗体保持在屏幕上

            self.background.background_move()  # 调取背景移动方法

            self.background.display()  # 调取背景第二张图片移动展示

            for enemy in self.enemy_plane:
                enemy.enemy_move()
                enemy.display()
            # self.enemy_plane.enemy_move()
            #
            # self.enemy_plane.display()

            pygame.display.update()  # TODO 8.刷新窗体

            self.event_init()  # TODO 11.反复监控是否存在监控事件

    # TODO 3.初始化窗体函数
    def frame_init(self):
        self.win = pygame.display.set_mode((self.WIN_WIDTH, self.WIN_HEIGHT))  # TODO 6.初始化窗体
        Model.win = self.win  # 初始化窗体传入Model类
        icon = pygame.image.load(APP_ICON)  # 5.提取游戏LOGO图标地址为常量  # TODO 7.设置游戏LOGO路径，加载图标文件为图片对象
        pygame.display.set_icon(icon)  # TODO 8.加载LOGO
        pygame.display.set_caption("plane War")  # TODO 9.设置游戏标题

    # TODO 10. 初始化事件
    def event_init(self):
        event_list = pygame.event.get()  # TODO 12.获取pygame界面的所有事件列表
        # print(event_list)
        for event in event_list:
            if event.type == pygame.locals.QUIT:  # TODO 14.捕获退出按钮事件
                sys.exit()  # TODO 15.执行退出按钮

    # TODO 17.初始化窗体中的元素
    def model_init(self):
        self.background = Background(IMG_BACKGROUND, 0, 0)  # 3.初始化背景对象，使用图片路径常量，放置在0,0位
        self.background.display()  # 4.填充图片到窗体中
        self.enemy_plane = []
        for i in range(5):
            self.enemy_plane.append(EnemyPlane(IMG_ENEMY, random.randint(0, self.WIN_WIDTH - 100) - 50, 0))


# TODO 2.设置测试类入口操作
if __name__ == '__main__':
    developer = Game()
    developer.run()
