"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/18
Description: 求一元多项式导数
测试例一：
input: 3 4 -5 2 6 1 -2 0
output: 12 3 -10 1 6 0
测试例二：
input: 3 4 -5 2 6 1 -2 0 3 -1
output: 12 3 -10 1 6 0 -3 -2
测试例三：
input: 0  5 3 4 -5 2 6 1 -2 0 3 -1
output: 12 3 -10 1 6 0 -3 -2
测试例四：
input: 2 0
output: 0 0
"""
input_list = list(map(int, input().split()))
coefficient_list = input_list[::2]
index_list = input_list[1::2]
out_coefficient = []
out_index = []
length = len(index_list)
result = ''
for i in range(length):
    if index_list[i] == 0:
        if length == 1:
            result += '0 0'
        else:
            continue
    else:
        out_coefficient.append(coefficient_list[i] * (index_list[i]))
        out_index.append(index_list[i] - 1)
for j in range(len(out_index)):
    result += str(out_coefficient[j]) + ' ' + str(out_index[j]) + ' '
print(result.strip(), end='')