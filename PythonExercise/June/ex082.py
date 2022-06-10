"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/1
Description: 射击比赛
"""

N = int(input())
stu_list = []
for i in range(N):
    id, x, y = input().split()
    temp = int(x)**2 + int(y)**2
    stu_list.append((id, temp))

stu_list.sort(key=lambda item: item[1])
print(stu_list[0][0], stu_list[-1][0])