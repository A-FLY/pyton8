"""
分析：
1. 整体文件复制采用 rb wb模式进行
2. 复制文件需要更改名称，变化是有规则的
3. 1.txt -> 1 - 副本.txt

"""

f_pash = r"F:\python笔记\1.txt"
idx = f_pash.rfind(".")
f_new = f_pash[:idx] + " - 副本" + f_pash[idx:]
with open(f_pash, "w") as file_root:
    file_root.write("pythomn008\npyton hello\nafei love python\nkhhggjh\njjggfghh")

with open(f_pash) as file_root:
    # info =""
    while True:
        info = file_root.readline().rstrip()
        print(info)
        if len(file_root.readline()) == 0:
            break


# with open(f_new,'w+') as file_new:
#     for i in info:
#         file_new.write(i)


# file_path = r"C:\Users\阿飞\Desktop\10.txt"
# with open(file_path) as file_table:
#     info = file_table.readline()
#     info1 = file_table.readline()
#     info2 = file_table.readline()
#     print(info)
#     print(info1)
#     print(info2)
#
#
# str_file = ""
# for i in info:
#     str_file += i.rstrip()
# print(str_file)
# print(len(str_file))
