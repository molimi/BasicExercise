"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/1
Description: 找重复的差值
"""
N = int(input())
init_list = [i for i in range(1, N + 1)]
input_list = list(map(int, input().split()))
result_dict = {}
for i in range(N):
    temp = abs(input_list[i] - init_list[i])
    if temp in result_dict:
        result_dict[temp] += 1
    else:
        result_dict[temp] = 1
result_list = sorted(result_dict.items(),
                     key=lambda item: item[0],
                     reverse=True)
for j in range(len(result_list)):
    if result_list[j][1] > 1:
        print(result_list[j][0], result_list[j][1])