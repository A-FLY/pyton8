"""
求Sn=a+aa+aaa+…+aa…aaa（有n个a）之值，其中a是一个数字。
例如：2+22+222+2222+22222（n=5），
输入两个数．第一个为a ，第二个为n（表示有多少个数相加）
，其中a和n都是大于１且小于１０的整数，输出其和
"""
a = input()
n = int(input())
i = 1
x = 0
while i < n + 1:
    x += int(a * i)
    i += 1
print(x)
