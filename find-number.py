"""
二分查找
"""


# 给定列表为升序时
def find_key_up(listx, key):
    left = 0
    right = len(listx) - 1
    while left <= right:
        mid = (left + right) // 2
        if listx[mid] < key:
            left = mid + 1
        elif listx[mid] > key:
            right = mid - 1
        else:
            return mid
    return None


# 列表为降序时
def find_key_down(listx, key):
    left = 0
    right = len(listx) - 1
    while left <= right:
        mid = (left + right) // 2
        if listx[mid] < key:
            right = mid - 1
        elif listx[mid] > key:
            left = mid + 1
        else:
            return mid
    return None


# ans_1 = find_key_down(list_1, 6)
# print(ans_1)

if __name__ == '__main__':
    n = [int(i) for i in input("请输入查询有序列表：").split(" ")]
    key = int(input("请输入要查询的数字："))
    if n[0] > n[1]:
        print(find_key_down(n, key))
    elif n[0] < n[1]:
        print(find_key_up(n, key))
