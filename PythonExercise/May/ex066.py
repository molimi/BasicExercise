"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/21
Description: 图像过滤
"""
M, N, A, B, C = list(map(int, input().split()))
for i in range(M):
    pixel_list = list(map(int, input().split()))
    for j in range(N):
        if pixel_list[j] > A and pixel_list[j] < B:
            pixel_list[j] = C
    str_format = lambda str1: '{:0>3d}'.format(str1)
    result_list = list(map(str_format, pixel_list))
    print(' '.join(result_list))