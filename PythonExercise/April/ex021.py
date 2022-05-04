"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/28
Description: 统计出现的数字
"""


def number_fraction(number):
    number_list = []
    while number:
        number_list.append(number % 10)
        number = number // 10
    return number_list


def main():
    N = int(input())
    number_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    number_list = number_fraction(N)
    for iter in number_list:
        number_dict[iter] += 1
    for index, value in number_dict.items():
        if value != 0:
            print('{}:{}'.format(index, value))


main()