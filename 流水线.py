# 要求：两端去空格，小写转大写，按照空格切割字符串，输出字符串，同行输出，间隔使用：
# "  hello itcast python  " -> HELLO:ITCAST:PYTHON:
# n = "  hello itcast python  "
# x = n.strip()
# print(x)
# x = x.upper()
# print(x)
# x=x.split()
# x="".join(x)
# print(x)
# x = " ".join(x)
# print(x)


#   流水线
# def str0(s):
#     """
#     去两端空白符
#     :param s:
#     :return:
#     """
#     a = s.strip()
#     return str1(a)
#
#
# def str1(s):
#     """
#     小写转大写
#     :param s:
#     :return:
#     """
#     s = s.upper()
#     return str2(s)
#
#
# def str2(s):
#     """
#     按照空格切割字符串
#     :param s:
#     :return:
#     """
#     s = s.split()
#     s = ":".join(s)
#     return s
#
#
# def str3(s):
#     """
#     间隔使用
#     :param s:
#     :return:
#     """
#     s = ":".join(s)
#     return s
# print(str0("  hello itcast python  "),end=":")


# 要求：两端去空格，小写转大写，按照空格切割字符串，输出字符串，同行输出，间隔使用：

# def str0(s, **kwargs):
#     s = s.strip()
#     s = s.upper()
#     s = s.split()
#     return str1(s,**kwargs)
# def str1(s,**kwargs):
#     for i in s:
#         print(i, **kwargs)
# str0("  hello itcast python  ",end = "%")


def qs(a=1, **kwargs):
    print(a)
    return qs1(**kwargs)


def qs1(b=1, **kwargs):
    print(b)
    return qs2(**kwargs)


def qs2(c=1, **kwargs):
    print(c)
    return qs3(**kwargs)


def qs3(d=1, **kwargs):
    print(d)


qs(a=1, b=2, c=3, d=5)
