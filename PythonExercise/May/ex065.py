"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/21
Description: 计算单身人士
解决超时问题：使用in会发现dict、set都比list快
"""
import sys

N = int(input())
mate_dict = {}
for i in range(N):
    man, woman = sys.stdin.readline().split()
    mate_dict[man] = woman

K = int(input())
guest_lst = sys.stdin.readline().split()
result_lst = guest_lst[:]
guest_set = set(guest_lst)
for i in range(K):
    if guest_lst[i] in mate_dict:
        if mate_dict[guest_lst[i]] in guest_set:
            result_lst.remove(guest_lst[i])
            result_lst.remove(mate_dict[guest_lst[i]])

result_lst.sort()
length = len(result_lst)
print(length)
if length:
    print(' '.join(result_lst))