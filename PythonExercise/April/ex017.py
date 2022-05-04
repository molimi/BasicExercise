"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/25
Description: 输出除数和余数
"""
p, q = list(map(int, input().split()))
print('%d %d' % (p // q, p % q))
