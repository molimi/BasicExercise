"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/17
Description: 求和计算
"""
input_list = list(map(int, input().split()))
iter = input_list[0] * (input_list[0] - 1)
sum = 0
length = len(input_list)
for i in range(1, length):
    for j in range(1, length):
        if j == i:
            continue
        else:
            sum += input_list[i] * 10 + input_list[j]
print(sum)