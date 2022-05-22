"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/21
Description: 计算朋友数
"""


def sum_number(number):
    sum = 0
    while number:
        sum += number % 10
        number = number // 10
    return sum


def main():
    N = int(input())
    input_list = list(map(int, input().split()))
    result_list = []
    for i in range(N):
        sum = sum_number(input_list[i])
        if sum not in result_list:
            result_list.append(sum)
    result_list.sort()
    print(len(result_list))
    print(' '.join(list(map(str, result_list))))


main()