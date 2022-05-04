"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/28
Description: D进制的A+B
注意小心都为零的情况
"""


def base_conversion(number, base):
    result_list = []
    if number == 0:
        result_list.append('0')
    else:
        while number:
            result_list.append(str(number % base))
            number = number // base
    result_list.reverse()
    return result_list


def main():
    a, b, d = list(map(int, input().split()))
    c = a + b
    print(''.join(base_conversion(c, d)))


main()