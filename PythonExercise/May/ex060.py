"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/20
Description: 爱丁顿数
思路：正确理解题意，先把列表排序，然后就可以计算哪一天的里程数刚好大于天数
"""
import sys
N = int(input())
distance_list = list(map(int, sys.stdin.readline().split()))
distance_list.sort(reverse=True)
day = 0
for i in range(N):
    if distance_list[i] > day + 1:
        day += 1
print(day)