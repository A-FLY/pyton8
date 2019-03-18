# n = [int(i) for i in input().split()]
# x1 = [int(i) for i in input().split()]
# x2 = [int(i) for i in input().split()]
# x3 = [int(i) for i in input().split()]
#
#
# # print(n)
# # print(x1)
# # print(x2)
# # print(x3)
# def gain_number(a):
#     """
#     获取一组数
#     :param a:
#     :return:
#     """
#     z = []
#     for j in range(a[0], a[1] + 1):
#         z.append(j)
#     return z
#
#
# def sum0(a, b, c):
#     """
#     计算三个集合中的树，并计算剩余树
#     :param a:
#     :param b:
#     :param c:
#     :return:
#     """
#     x = len(set(a) | set(b) | set(c))
#     x = n[0] + 1 - x
#     return x
#
#
# x1 = gain_number(x1)
# x2 = gain_number(x2)
# x3 = gain_number(x3)
# print(sum0(x1, x2, x3))


# def found_interval():
#     """
#     创建区间
#     :return:
#     """
#     for i in range(len(m)):
#         m[i] = [int(x) for x in input().split()]

n = [int(x) for x in input().split()]
m = [1, ] * (n[0] + 1)
z = [0, ] * n[1]
ans = 0
for i in range(len(z)):
    z[i] = [int(x) for x in input().split()]
for i in z:
    if i[0] > i[1]:
        i[0], i[1] = i[1], i[0]
    for j in range(i[0], i[1] + 1):
        m[j] = 0
for i in m:
    ans += i
print(ans)
