# class A:
#
#     def __init__(self):
#         self.name = 1000
#
#     def bb(self):
#         print("sjbchdghd")
#
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.age = 18
#
#
# class C:
#     def kan(self):
#         #  a.bb()
#         # print(b.age())
#
#
# a = A()
# b = B()
# c = C()
# c.kan()

# lt = [1, 2, 3, 4, 5, 7, 7, 99, ]
# a = []
# a = [item for item in lt[:-1]]
# print(a)
# print(len(a))
# print(len(lt))
#
# # 元组  创建
# b = (1, 2, 3)
# x = list(b)# 把元组变为列表
#             # 然后修改
# print(x)

# 反向截取
# d=list(range(8,5,-1))
# print(d)

# a= ()
# print(type(a))


# a = list(range(1, 9))
# for i in range(len(a) - 1, -1, -1):
#     print(a[i])
# list

# a = [1, 2, 3]
# del a[0]
# print(a)

"""
取某个数的每一位

b = 1234
while b != 0:
    a = b % 10
    print(a)
    b //= 10
    """

"""
阶乘求和
"""
#
# n = int(input())
# x = 0
# a = 1
# for i in range(1, n + 1):
#     # a = 1      a可以放在此处，最好
#     for j in range(1, i + 1):
#         a *= j
#     x += a
#     # 每次内循环结束，要对上一个数的阶乘 a 重置为一，否则下次循环开始 a 不等于1
#     a = 1
# print(x)


# a = ["xiaoming", "xiaozhang", "xiaoli", "afei"]
# for i in a:
#     print(i)
# for i in range(len(a)):
#     print(a[i])

# guset = ["aowang", "xiaozhang", "xiaojing", "dudu"]
# # for i in guset:
# #     print("\t%s" % i)
# # x = guset.pop()
# # print(x)
# # guset.append("huahua")         #  追加
# # print(guset)
# # guset.insert(0, "wendaoliu")     # 指定位置 插入
# # print(guset)
# # guset.sort()                    # 永久排序
# # print(guset)
# guset.reverse()              #翻转序列
# print(guset)
# x = sorted(guset)                  #  传入要排序的序列，进行排序，返回值可以接收
# print(x)

# guset.clear()
# print(guset)
# guset[3] = "xiaohua"

# print(guset)
"""
一种列表 复制时的问题

a = [1, 2, 3]
# b = [8, 4, 6]
# b = a   # 这种复制，只是让 b 指向 a 的存储位置
b = a[::]    # 可以使用切片来复制，此时 b 将不会被修改
print(a,b)
a.pop()
print(a,b)    # 当修改a 时，b 中数据也被修改
"""

#
# a = "xiaoh"
# b = "xiaoAAA"
# # print(b.lower())
# # print(a == b)
# # print(b in a)
# c = ["xiaoh",123]
# print(a in c)
# d = "xiaohua"
# print( a not in d)

# alien_color = "green"
# if alien_color == "green":
#     print("Y")

# names = ["afei", 'ajing', 'ahua', 'awang', 'azhang', 'admin']
# for name in names:
#     if name == 'admin':
#         print(name + "：\t大家好,爱你们")
#     print(name + "：\t大家好")
# names.clear()
# print(f"{names}没人了")
# only_users = ["afei", 'ajing', 'ahua', 'awang', 'azhang', 'admin']
# new_users = ['Ahua', 'aWaNg', "xiaoliu", 'acheng', 'ateng']
# for new_user in new_users:
#     x = new_user.lower()
#     print('---------')
#     if x in only_users:
#         print('请换一个名字')
#     else:
#         print('创建成功')

# a = 'aWaNg'
# print(a)
# x=a.lower()
# print(x)
# print(a)

# friend = {'name':'xiaowang','age':30,'city':'xian'}
# for value in friend.values():
#     # print(key,end=':')
#     print(value)
#     print()

# friend_0 = {'name': 'xiaohua', 'sex': 'girl'}
# friend_1 = {'name': 'xiaowang', 'sex': 'boy'}
# friend_2 = {'name': 'wenge', 'sex': 'girl'}
# # list_0 =[]
# list_0.append(friend_0)
# list_0.append(friend_1)
# list_0.append(friend_2)
# print(list_0)
# dict_0 = {}
# del friend_0['name']
# friend_0.pop()
# friends = friend_0 + friend_1
# print(friends)
# # print(x)

# .get  课后查

# friend_2 = {'name': 'wenge', 'sex': 'girl'}
# x=friend_2.get('name')       # 传入键
# print(x)

# class stu:
#     def __init__(self, name):
#         self.name = name
#
#
# list1 = [stu('王五'), stu('李四'), stu('张三')]

# list1.pop(2)  # 根据索引位置删
# print(list1)
# stu0 = None
# for i in list1:
#     if i.name == '张三':
#         list1.remove(i)
# print(list1)
# for i in range(len(list1)):
#     if list1[i].name == '张三':
#         stu0 = list1[i]
#         break
#     else:
#         pass
#
# if stu0:
#     list1.remove(stu0)
#     print("已删除")
# else:
#     print("未找到")
# print(list1)
# print(list1[0])


# class Stu():
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age  = age
#         self. sex = sex
#
#
#     def __str__(self):
#         return self.name + str(self.age) + str(self.sex)
#
# def send_stu(name,age=18,sex=1):
#     st = Stu(name,age,sex)
#     print(st)
#
# send_stu("阿飞")

"""
换汽水瓶

def huan(n):
    if n < 2:
        return 0
    return huan(n - 2) + 1


# ans = []
# while True:
#     n = int(input())
#     if n != 0:
#         ans.append(huan(n))
#     else:
#         break
# print(ans)
while True:
    n = int(input())
    if n != 0:
        ans=huan(n)
        print(ans)
    else:
        break
"""

# def list0(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return list0(n-1)+list0(n-2)
# while True:
#     in_input = int(input())
#     if in_input > 0:
#         print(list0(in_input))
#     else:
#         break
#       1  2   3
#  20   9  4   1


# def eat_peach(n):
#     if n ==1:
#         return  1
#     return n*2+1
#
# in_input = int(input())
# print(eat_peach(in_input))

# def eat_peach(a):
#     if a == 1:
#         return 1
#     return 2 * (eat_peach(a - 1) + 1)
#
# while True:
#     n = int(input())
#     if n ==0:
#         break
#     else:
#         print(eat_peach(n))


# def print_str(num,b):
#     for i in range(num):
#         print(b)
# c = input()
# n = int(input())
# m = int(input())
# str0=c*m
# print_str(n,str0)
"""
公交换号
"""
# car = {'801': 601, '802': 99, '808': 608, '810': 609, '814': 614, '823': 626, '826': 626,
#        '836': 617, '846': 619, '849': 620, '852': 621}
# while True:
#     n = input()
#     if n == "0":
#         break
#     else:
#         if n in car:
#             print(car[n])
#         else:
#             print(n)

"""
逆序
"""
# nums = [int(i) for i in input().split()]
# nums.sort(reverse=True)
# for i in range(len(nums)):
#     if i == 0:
#         print(nums[i],end="")
#     else:
#         print(" "+str(nums[i]),end="")

#

"""
数字模式的识别
"""
#
# nums = [i for i in input().split()]
# new_nums = "".join(nums)
# a = []
# for i in nums:
#     x = str(new_nums.count(i)) + i
#     a.append(x)
# a.sort(reverse=True)
# print(a[0][1])

"""
字符出现最多
"""

# n = input()
# a = []
# for i in n:
#     x = str(n.count(i)) + i
#     a.append(x)
# a.sort(reverse=True)
# print(a[0][-1])


"""
判断素数
"""

# a = int(input())
# b = int(input())
# stamp = []
# if a > b:
#     a, b = b, a
# for i in range(a, b + 1):
#     count = []
#     for j in range(2, i):
#         if i % j == 0:
#             count.append(j)
#     if len(count) == 0:
#         stamp.append(i)
# print(len(stamp))

"""
字符统计
"""
# n = input()
# lower = 0
# upper = 0
# nums = 0
# others = 0
# for i in n:
#     if i.isalnum():
#         if i.isnumeric():
#             nums += 1
#         elif i.isupper():
#             upper += 1
#         elif i.islower():
#             lower += 1
#     else:
#         others += 1
# print(lower,upper,nums,others)
#
# b=[]
# for x in range(2,200):
#     a = []
#     for y in range(2,x):
#         if x//y==0:
#             a.append(y)
#     if len(a)==(x-2):
#         b.append(x)
#
# print(b,end=" ")

"""
完数

n = int(input())
ans = []
for i in range(1, n + 1):
    a = []
    add0 = 0
    for j in range(1, i):
        if i % j == 0:
            a.append(j)
    for x in a:
        add0 += x
    if i == add0:
        ans.append(i)
        print("%d its fastors are " % i, end="")
        print(" ".join(str(y) for y in a))
if len(ans) == 0:
    print("no")
"""