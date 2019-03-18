"""
案例找出真凶
分析：
1.姓 name                startswith
2.名 name nick_name      find
3.性别 gender            ==
4.血型 blood             ==
5.籍贯 native            find
6.出生日期 idcard        切片，比较运算
"""
# db_infos = [{"name": "张三丰", "gender": 1, "nick_name": "三爷", "idcard": "110101153808081017", "blood": "b",
#              "native": "湖北省丹江口市武当山玉虚宫"}
#     , {"name": "张大彪", "gender": 1, "nick_name": "斌仔", "idcard": "130323197711111011", "blood": "b",
#        "native": "河北省秦皇岛市武山海关区鞋拔子路胶水胡同103"}]
# 1. 循环列表，取出个人信息
# for idx in db_infos:
#     name = idx["name"]
#     gender = idx["gender"]
#     nick_name = idx["nick_name"]
#     idcard = idx["idcard"]
#     blood = idx["blood"]
#     native = idx["native"]
#     if not name.startswith("张"):
#         continue
#     if nick_name.find("斌") == -1:
#         continue
#     if gender != 1:
#         continue
#     if int(idcard[6:10]) < 1975 or int(idcard[6:10]) > 1978:
#         continue
#     if blood.lower() != 'b':
#         continue
#     if '河北省' not in native:
#         continue
#     sex = {1: '男', 0: '女'}
#     print("姓名：" + name + "  性别:" + sex[gender] + "  外号:" + nick_name +
#           "  身份证号:" + str(idcard) + "  血型:" + blood + "  出生地址：" + native)

# for idx in db_infos:
#
#     name = idx["name"]
#     gender = idx["gender"]
#     nick_name = idx["nick_name"]
#     idcard = idx["idcard"]
#     blood = idx["blood"]
#     native = idx["native"]
#
#     if not name.startswith("张"):
#         continue
#     if gender != 1:
#         continue
#     if nick_name.find("斌") == -1:
#         continue
#     if int(idcard[6:10]) < 1975 or int(idcard[6:10]) > 1978:
#         continue
#     if blood.lower() != "b":
#         continue
#     if "河北省" not in native:
#         continue
#     sex = {0: '女', 1: '男'}
#     print('姓名：' + name + '  性别：' + sex[gender] + '  外号：' + nick_name +
#           '  身份证号：' + str(idcard) + '  血型：' + blood + '  户籍地址：' + native)
