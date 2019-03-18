# class Human:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = object().__new__(Human)
#         return cls.__instance


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#
# class Dog:
#     def __init__(self, name):
#         self.name = name
#
#
# p = Cat('ao')
# # print(id(p))
# # print(p.name)
# p = Cat('liu')
# print(id(p))
# print(p.name)

