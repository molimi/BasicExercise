"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/25
Description: 石头剪刀布
"""

import sys


def game(a, b):
    if a == b:
        return 0
    elif a == 'C' and b == 'J':
        return 1
    elif a == 'J' and b == 'B':
        return 1
    elif a == 'B' and b == 'C':
        return 1
    else:
        return -1


one_dict = {'B': 0, 'C': 0, 'J': 0}
two_dict = {'B': 0, 'C': 0, 'J': 0}
count = [0] * 3
N = int(input())
for i in range(N):
    one, two = sys.stdin.readline().split()
    score = game(one, two)
    if score == 1:
        count[0] += 1
        one_dict[one] += 1
    elif score == 0:
        count[1] += 1
    else:
        count[2] += 1
        two_dict[two] += 1

sys.stdout.write('%d %d %d' % (count[0], count[1], count[2]))
sys.stdout.write('%d %d %d' % (count[2], count[1], count[0]))
key1_max = max(one_dict, key=one_dict.get)
key2_max = max(two_dict, key=two_dict.get)
sys.stdout.write('%s %s' % (key1_max, key2_max))