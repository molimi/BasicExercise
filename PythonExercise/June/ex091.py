"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/7
Description: N 自守数
"""
M = int(input())
input_list = list(map(int, input().split()))
for i in range(M):
    for j in range(1, 10):
        n = len(str(input_list[i]))
        temp = input_list[i]**2 * j
        if temp % (10**n) == input_list[i]:
            print('{} {}'.format(j, temp))
            break
    else:
        print('No')