"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/11
Description: 统计主元个数
思路：笨办法，一一比较，果然超时
思路二：先排序，比较位置是否发生改变，且比当前位置要大的没变的就是主元(要排除相同值的元素)
"""
'''
import sys
n = int(input())
input_list = list(map(int, sys.stdin.readline().split()))
sorted_list = sorted(input_list)
out_list = []
count = 0
for i in range(n):
    left_list = input_list[:i]
    right_list = input_list[i + 1:]
    if i == 0:
        if input_list[i] <= min(right_list):
            count += 1
            out_list.append(input_list[i])
    elif i == n - 1:
        if input_list[i] >= max(left_list):
            count += 1
            out_list.append(input_list[i])
    elif input_list[i] <= min(right_list) and input_list[i] >= max(left_list):
        count += 1
        out_list.append(input_list[i])

print(count)
print(' '.join(map(str, out_list)))
'''
import sys
n = int(input())
input_list = list(map(int, sys.stdin.readline().split()))
sorted_list = sorted(input_list)
out_list = []
max = 0
for i in range(n):
    if input_list[i] > max:
        max = input_list[i]
        if input_list[i] == sorted_list[i]:
            out_list.append(input_list[i])

print(len(out_list))
print(' '.join(map(str, out_list)))