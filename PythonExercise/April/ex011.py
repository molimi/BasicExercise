"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/19
Description: 判断数字是否大于第三个数
"""
n = int(input())
input_list = []
for i in range(n):
    input_list.append(list(map(int, input().split())))
comp = lambda a, b, c: a + b > c
for j in range(n):
    ans = comp(input_list[j][0], input_list[j][1], input_list[j][2])
    print('Case #{}: {}'.format(j + 1, str(ans).lower()))
# print(cmp(4, 2, 4))