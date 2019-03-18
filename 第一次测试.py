"""
给定一个数字n，求1-n之间的数字为奇数的总和

n = int(input())
if 1 <= n <= 10000:
    x = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            pass
        else:
            x += i
    print(x)
  """

"""
过火车站

n = int(input())
m = int(input())
if n <= 40 and 1000 <= m <= 2000:
    print("Yes")
else:
    print("No")
"""

"""
数 1  的个数

n = int(input())
x = 0
for i in range(1, n + 1):
# i =j
    while i != 0:
        if i % 10 == 1:
            x += 1
        i = i // 10
print(x)
"""

dict1 = {"xihao": "dhsgdh", "nhjhg": 789, 123: "dcghd"}
for x, y in dict1.items():
    print(x)
    print(y)
