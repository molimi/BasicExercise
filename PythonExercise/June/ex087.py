"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/5
Description: 有多少不同的值
"""
N = int(input())
result_list = []
for i in range(1, N + 1):
    result_list.append(int(i / 2) + int(i / 3) +
                       int(i / 5))  # i // 2 + i // 3 + i // 5
print(len(set(result_list)))