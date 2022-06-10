"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/6
Description: 危险品装箱
思路一：顺循环实现会超时
思路二：使用字典实现，dict.get(key) + b
"""
'''
import sys
N, M = map(int, sys.stdin.readline().split())
item1, item2 = [], []
for i in range(N):
    temp = sys.stdin.readline().split()
    item1.append(temp[0])
    item2.append(temp[1])

for j in range(M):
    K, *item3 = sys.stdin.readline().split()
    for k in range(int(K)):
        if item3[k] in item1:
            index = item1.index(item3[k])
            if item2[index] in set(item3):
                print('No')
                break
        if item3[k] in item2:
            index = item2.index(item3[k])
            if item1[index] in set(item3):
                print('No')
                break
    else:
        print('Yes')
'''

import sys
M, N = map(int, sys.stdin.readline().split())
temp_dict = {}
for i in range(M):
    temp1 = sys.stdin.readline().split()
    temp_dict[temp1[0]] = temp_dict.get(temp1[0], []) + temp1[1:]
for j in range(N):
    temp2 = input().split()
    flag = 'Yes'
    for item1 in set(temp2[1:]):
        if item1 in temp_dict:
            for item2 in temp_dict[item1]:
                if item2 in set(temp2[1:]):
                    flag = 'No'
                    break
        if flag == 'No':
            break
    print(flag)