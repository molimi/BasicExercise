"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/16
Description: 统计房间空置率
bug：map()方法里面如果第一个参数是评估函数eval会导致超时
"""
import sys
N, e, D = map(float, sys.stdin.readline().split())
num_list = []
data_list = []
empty_count = 0
maybe_count = 0
for i in range(int(N)):
    num, *power = map(float, sys.stdin.readline().split())
    num_list.append(int(num))
    data_list.append(power)

for j in range(int(N)):
    compare = num_list[j]
    count = 0
    for k in range(compare):
        if data_list[j][k] < e:
            count += 1
    if count * 2 > compare:
        if compare > int(D):
            empty_count += 1
        else:
            maybe_count += 1

print('{:.1f}% {:.1f}%'.format(maybe_count * 100 / N, empty_count * 100 / N))