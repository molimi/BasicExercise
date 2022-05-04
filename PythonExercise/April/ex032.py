"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/4
Description: 分数测试
"""

import sys


def main():
    n = int(input())
    new_dict = {}
    for i in range(n):
        group, score = map(int, sys.stdin.readline().split())
        if group in new_dict.keys():
            new_dict[group] += score
        else:
            new_dict[group] = score

    result_list = sorted(new_dict.items(), key=lambda item: item[1])
    print('{} {}'.format(result_list[-1][0], result_list[-1][1]))


if __name__ == '__main__':
    main()