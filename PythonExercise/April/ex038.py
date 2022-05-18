"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/6
Description: 成绩统计
"""
# 思路一：时间复杂度比较高
'''
import sys

n = int(sys.stdin.readline())
score_list = list(map(int, sys.stdin.readline().split()))
find_list = list(map(int, sys.stdin.readline().split()))
for i in range(1, find_list[0] + 1):
    if i == find_list[0]:
        print(score_list.count(find_list[i]))
    else:
        print(score_list.count(find_list[i]), end=' ')
'''
# 思路二：利用空间换取时间
import sys

n = int(sys.stdin.readline())
score_list = list(map(int, sys.stdin.readline().split()))
find_list = list(map(int, sys.stdin.readline().split()))
count_list = [0 for i in range(101)]
result_list = []
for score in score_list:
    count_list[score] += 1
for i in range(1, find_list[0] + 1):
    result_list.append(str(count_list[find_list[i]]))
print(' '.join(result_list))