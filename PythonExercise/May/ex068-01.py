"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/21
Description: 找到色差大的点
条件：独一无二，色差大
这个题目似乎用数组要简单些
用数组进行比较
"""
import sys

# 计算3*3矩阵距离的最小值
'''
def min_matrix(matrix):
    mid = matrix[1][1]
    distance = 16777215
    for i in range(0, 3):
        for j in range(0, 3):
            if i != 1 and j != 1:
                temp = abs(matrix[i][j] - mid)
                if temp < distance:
                    distance = temp
    return distance
'''
import sys

M, N, TOL = list(map(int, input().split()))
fill_lst = [0 for _ in range(M + 2)]
input_list = []
input_dict = {}
result_list = []
for k in range(N):
    temp_lst = list(map(int, sys.stdin.readline().split()))
    for k in range(M):
        if temp_lst[k] in input_dict:
            input_dict[temp_lst[k]] += 1
        else:
            input_dict[temp_lst[k]] = 1
    temp_lst.append(0)  # 在两端填充零
    temp_lst.insert(0, 0)
    input_list.append(temp_lst)
input_list.insert(0, fill_lst)  # 在上下填充零
input_list.append(fill_lst)
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if input_dict[input_list[i][j]] == 1:
            low, high = i + 1, i - 1
            right, left = j + 1, j - 1
            length1 = abs(input_list[i][j] - input_list[low][left])
            length2 = abs(input_list[i][j] - input_list[low][j])
            length3 = abs(input_list[i][j] - input_list[low][right])
            length4 = abs(input_list[i][j] - input_list[i][left])
            length5 = abs(input_list[i][j] - input_list[i][right])
            length6 = abs(input_list[i][j] - input_list[high][left])
            length7 = abs(input_list[i][j] - input_list[high][j])
            length8 = abs(input_list[i][j] - input_list[high][right])
            if length1 > TOL and length2 > TOL and length3 > TOL and length4 > TOL and length5 > TOL and length6 > TOL and length7 > TOL and length8 > TOL:
                result_list.append('({}, {}): {}'.format(
                    j, i, input_list[i][j]))

length = len(result_list)
if length == 1:
    print(result_list[0])
elif length == 0:
    print('Not Exist')
else:
    print('Not Unique')