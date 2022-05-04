"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/26
Description: 计算程序运行时间
"""
CLK_TCK = 100
c1, c2 = map(int, input().split())
running_time = int(round((c2 - c1) / 100, 0))
result = [0, 0, 0]
for i in range(3):
    result[i] = running_time % 60
    running_time //= 60

print('{:0>2}:{:0>2}:{:0>2}'.format(result[2], result[1], result[0]))