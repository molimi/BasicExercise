"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/26
Description: 组成最小的数
"""
number_list = list(map(int, input().split()))
result_str = ''
if number_list[0] == 0:
    for i in range(10):
        result_str += str(i) * number_list[i]
else:
    for index in range(1, 10):
        if number_list[index] != 0:
            break
    result_str = str(
        index) + '0' * number_list[0] + str(index) * (number_list[index] - 1)
    for j in range(index + 1, 10):
        result_str += str(j) * number_list[j]

print(result_str)