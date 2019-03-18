"""
给你两个数a、b (1<=a,b<=1000),
判断这两个数组成的区间内共有多少个质数
------------------------------
一个大于1的自然数，除了1和它自身外,
不能被其他自然数整除的数叫做质数
"""
a = int(input())
b = int(input())
x = 0
if a > b:
    for i in range(b, a + 1):
        for j in range(2, i):
            if i // j == 0:
                break
            else:
                x += 1
else:
    for i in range(a, b + 1):
        for j in range(1, i):
            if i % j == 0:
                break
            else:
                x += 1
print(x)
