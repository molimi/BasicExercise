"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/1
Description: 倒序输入结果
"""
a, b = input().split()
c = int(a) * int(b)
out_list = list(str(c))
out_list.reverse()
out_str = ''.join(out_list)
print(out_str.strip('0'))
# print(out_str)