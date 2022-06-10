"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/9
Description: 岩洞施工
思路：找底部坐标最大值，找顶部坐标最小值，作差，如果大于零，就是输出的最大高度，
否则用底部最大坐标减去顶部最小坐标+1
"""
N = int(input())
top_list = list(map(int, input().split()))
bottom_list = list(map(int, input().split()))
top_min = min(top_list)
bottom_max = max(bottom_list)
distance = top_min - bottom_max
if distance > 0:
    print('{} {}'.format('Yes', distance))
else:
    distance = bottom_max - top_min + 1
    print('{} {}'.format('No', distance))