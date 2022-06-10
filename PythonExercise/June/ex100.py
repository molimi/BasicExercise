"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/9
Description: 校庆
"""
import sys
N = int(input())
alumna_list = []
guest_list = []
for i in range(N):
    alumna_list.append(input())
M = int(input())
for j in range(M):
    guest_list.append(input())

alumna_set = set(alumna_list)
guest_set = set(guest_list)
result_list = []
for iter in guest_set:
    if iter in alumna_set:
        result_list.append(iter)
length = len(result_list)
print(length)
if length:
    result_list.sort(key=lambda iter: iter[6:14])
    print(result_list[0])
else:
    guest_list.sort(key=lambda iter: iter[6:14])
    print(guest_list[0])