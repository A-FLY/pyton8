"""
案例：办公室的打印机
一台打印机可以服务于一个办公室中所有的人，完成他们的打印任务。
分析：
1.打印机：将要打印的任务添加到打印的任务队列中，真正的打印操作
2.经理：将要打印的操作加入打印机中
3.员工：将要打印的操作加入打印机中
"""


# class Pm():
#     def use_printer(self, info, p):
#         p.print_info(info)
#
#
# class Staff:
#     def use_printer(self, info, p):
#         p.print_info(info)
#
#
# class Printer:
#     __instance = None
#     __print_list = False
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = object.__new__(Printer)
#         return cls.__instance
#
#     def __init__(self):
#         if Printer.__print_list == False:
#             self.print_list = []
#             Printer.__print_list = True
#
#     def print_info(self, info):
#         """
#         添加打印队列
#         :param info:
#         :return:
#         """
#         self.print_list.append(info)
#
#     def prt(self):
#         print(self.print_list)
#
#
# p = Pm()
# pt = Printer()
# p.use_printer("欢迎莅临指导", pt)
#
# p = Printer()
# sta0 = Staff()
# sta0.use_printer("陪同人员：。。。", pt)
#
# p = Printer()
# p.prt()


class Human:
    def print_info(self, info, p):
        p.printer_work(info)


class Pm(Human):
    pass


class Staff(Human):
    pass


class Printer():
    # __is_init = False
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(Printer)
            cls.print_list = []
            return cls.__instance

    # def __init__(self):
    #     if Printer.__is_init == False:
    #         self.print_list = []
    #         Printer.__is_init = True

    def printer_work(self, info):
        self.print_list.append(info)

    def now_print(self):
        print(self.print_list)


pm = Pm()
p = Printer()
pm.print_info("jingli", p)
p.now_print()
