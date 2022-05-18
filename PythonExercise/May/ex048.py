"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/11
Description: 加密规则
思路：奇数位相加对13求余，JQK，偶数位用B-A，需要考虑两个字符的长度，
若B短则补零，而A短直接把B的剩余部分加上
"""
number_a, number_b = input().split()
a_list = list(number_a)
a_list = list(map(int, a_list))
b_list = list(number_b)
b_list = list(map(int, b_list))
a_list.reverse()
b_list.reverse()
result_list = []
length1 = len(a_list)
length2 = len(b_list)
length = length1 if length1 > length2 else length2
if length1 > length2:
    b_list.extend([0] * (length1 - length2))
else:
    a_list.extend([0] * (length2 - length1))

for i in range(length):
    if i % 2 == 0:
        he = a_list[i] + b_list[i]
        if he % 13 == 12:
            result_list.append('K')
        elif he % 13 == 11:
            result_list.append('Q')
        elif he % 13 == 10:
            result_list.append('J')
        else:
            result_list.append(str(he % 13))
    else:
        cha = b_list[i] - a_list[i]
        result_list.append(str(cha + 10)) if cha < 0 else result_list.append(
            str(cha))

result_list.reverse()

print(''.join(result_list))