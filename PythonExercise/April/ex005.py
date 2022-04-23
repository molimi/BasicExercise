"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/15
Description: 选择关键数
"""


def callatz(number):
    """返回以查找的记录的列表"""
    cover_list = []
    while True:
        if number != 1:
            if number % 2 == 0:
                number = int(number / 2)
                cover_list.append(number)
            else:
                number = int((3 * number + 1) / 2)
                cover_list.append(number)
        else:
            break
    cover_list.pop()
    return cover_list


n = int(input())
input_number = [int(x) for x in input().split(' ')]  # 将输入转换为整数列表

# number_list = callatz(max(input_number))
number_list = []  # 存放前面没出出现的记录
for i in range(n):
    if input_number[i] in number_list:
        continue
    else:
        number_list += callatz(input_number[i])

# print(sorted(list(set(number_list))))
result_list = []
for i in range(n):
    if input_number[i] in number_list:
        continue
    else:
        result_list.append(input_number[i])

result_list.sort(reverse=True)  # 把输出结果排序
result_str = ''
for i in range(len(result_list)):
    result_str += str(result_list[i]) + ' '
print(result_str.strip())