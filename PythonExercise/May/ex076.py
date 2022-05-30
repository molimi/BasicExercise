"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/27
Description: WiFI密码
"""
N = int(input())
input_list = []
right_list = ['A-T', 'B-T', 'C-T', 'D-T']
for i in range(N):
    input_list.append(input().split())

result = ''
for i in range(N):
    for j in range(4):
        temp = input_list[i][j]
        if temp in right_list:
            result += str(ord(temp[0]) - ord('A') + 1)
print(result)