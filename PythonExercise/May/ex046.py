"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/11
Description: 划拳
"""
n = int(input())
count_a, count_b = 0, 0
input_list = [[] for i in range(n)]
for i in range(n):
    input_list[i] = list(map(int, input().split()))
for i in range(n):
    if input_list[i][1] == input_list[i][0] + input_list[i][2] and input_list[
            i][3] != input_list[i][0] + input_list[i][2]:
        count_b += 1
    elif input_list[i][1] != input_list[i][0] + input_list[i][
            2] and input_list[i][3] == input_list[i][0] + input_list[i][2]:
        count_a += 1
print(str(count_a) + ' ' + str(count_b))