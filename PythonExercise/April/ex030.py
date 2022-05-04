"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/4
Description: 完美数列
"""

# 思路一：暴力搜索法
import sys


def main():
    n, p = map(int, sys.stdin.readline().split())
    number_list = sorted(list(map(int, sys.stdin.readline().split())))
    max_len = 0
    for i in range(n):
        for j in range(max_len + i, n):
            if number_list[j] > number_list[i] * p:
                break
            max_len += 1
    print(max_len)


if __name__ == '__main__':
    main()
'''
def is_perfect(input_list, p):
    max_number = max(input_list)
    min_number = min(input_list)
    if min_number * p >= max_number:
        return True
    else:
        return False

# 思路一：每次删除最大元素和最小元素，进行判断，但复杂度比较高
def main():
    n, p = map(int, sys.stdin.readline().split())
    number_list = sorted(list(map(int, sys.stdin.readline().split())))
    max_list = number_list.copy()
    min_list = number_list.copy()

    count = n
    for i in range(n):
        if is_perfect(max_list, p) or is_perfect(min_list, p):
            print(count)
            break
        else:
            max_list.remove(max(max_list))
            min_list.remove(min(min_list))
            count = count - 1


if __name__ == '__main__':
    main()
    '''