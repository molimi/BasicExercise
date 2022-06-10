"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/10
Description: 老鼠爱大米
"""
N, M = map(int, input().split())
out_list = []
for i in range(N):
    temp = list(map(int, input().split()))
    out_list.append(max(temp))
print(' '.join(map(str, out_list)))
print(max(out_list))