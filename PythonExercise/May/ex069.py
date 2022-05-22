"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/22
Description: 微博转发抽奖
"""

M, N, S = list(map(int, input().split()))  # 分别是总人数，间隔，开始的序号
input_list = [0]  # 占位符
for i in range(M):
    input_list.append(input())

result_list = []
index = S
while True:
    if index <= M:
        if input_list[index] in result_list:
            index += 1
        else:
            result_list.append(input_list[index])
            index += N
    else:
        break

length = len(result_list)
if length == 0:
    print('Keep going...')
else:
    for k in range(length):
        print(result_list[k])