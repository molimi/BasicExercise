"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/10
Description: 2019数列
bug: 这么简单个程序，不知为啥测试点二不通过
"""
n = int(input())
out_list = [2, 0, 1, 9]
for i in range(4, n):
    out_list.append(
        (out_list[i - 1] + out_list[i - 2] + out_list[i - 3] + out_list[i - 4])
        % 10)

print(''.join(map(str, out_list)))