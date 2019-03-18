# m, n = input().split()
# x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
#      'seven': 7, 'eight': 8, 'nine': 9}
# ans = x[m] + x[n]
# print(ans)


"""
递归求n个平方和，即 1^2 + 2^2+.....+n^2 (x^2表示x的平方）
x = 0
def add0(a):
    global x
    x += a ** 2
    if a == 1:
        return x
    return add0(a - 1)


print(add0(int(input())))

"""

"""
汽水瓶
"""
# x = 0
# def huan(a):
#     # global x
#     # x += 1
#     if a < 2:
#         return 0
#     # elif a == 2:
#     #     return x + 1
#     return huan(a - 2)+1
# print(huan(int(input())))


