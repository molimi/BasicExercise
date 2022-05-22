"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/21
Description: 找到色差大的点
条件：独一无二，色差大
这个题目似乎用数组要简单些
用数组进行比较，字典存放唯一的像素
"""
import sys
import numpy as np


# 计算3*3矩阵距离的最小值
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


def main():
    M, N, TOL = list(map(int, input().split()))
    input_list = []
    input_dict = {}
    result_list = []
    for _ in range(N):
        temp_lst = list(map(int, sys.stdin.readline().split()))
        input_list.append(temp_lst)
        for k in range(M):
            if temp_lst[k] in input_dict:
                input_dict[temp_lst[k]] += 1
            else:
                input_dict[temp_lst[k]] = 1

    input_array = np.array(input_list)
    input_array = np.pad(input_array, (1, 1), 'constant')

    for iter in input_dict:
        if input_dict[iter] == 1:
            index_i, index_j = np.where(input_array == iter)
            index_i, index_j = index_i[0], index_j[0]
            if min_matrix(input_array[index_i - 1:index_i + 2,
                                      index_j - 1:index_j + 2]) > TOL:
                result_list.append('({}, {}): {}'.format(
                    index_j, index_i, input_array[index_i][index_j]))

    length = len(result_list)
    # print(result_list)
    if length == 1:
        print(result_list[0])
    elif length == 0:
        print('Not Exist')
    else:
        print('Not Unique')


main()