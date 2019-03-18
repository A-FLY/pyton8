list1 = [1, 2, 3, 4, 5, 6, 11, 12]
list2 = [9, 8, 7, 6, 5]

# list3 = list1 + list2    #  拼接
# print(list3)
# list1.append(33)         # 在列表中追加一个参数
# print(list1)
# list1.extend([11, 22, 33])  # 在列表中末尾添加一个列表  *可以是列表名，可以是具体的一个列表
# print(list1)
# list1.extend(list2)
# print(list1)
# list1.append(3)
# x = list1.count(3)     #  在列表中查找传入参数的个数，并返回个数
# print(list1)
# print(x)
# list1.insert(2,"i love")  #在指定下标位置，插入传入参数
# print(list1)
# x=list1.pop(10)  # 弹出指定的参数（传入的），如果列表中没有该参数，则报错
# print(list1)
# print(list1)
# list1.clear()   #清除整个列表
# print(list1)
# print(list1)
# list1.reverse()  #列表翻转
# print(list1)
# print(list1)
# list1.remove(4)  # 传入一个需要移除的对象，进行移除
# print(list1)


# list1.sort()   回去查
# print(x)

# x=list1.count(1)
# print(x)
"""
字典遍历

dict1 = {43: "cndjndj", "mode": 123}
for key, value in dict1.items():
    print(key, end=":")
    print(value)
for key in dict1:
    print(dict1[key])
    """

"""
列表遍历
"""

# for _ in list1:
#    print(_)

list3 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

# for i in range(0,len(list3)):
#     for j in range(i,len):
#         print(list3[i][j],end="  ")
#     print()


for i in range(0, list3.__len__()):
    for j in range(0, list3[1].__len__()):
        print(list3[i][j], end=" ")
    print()
