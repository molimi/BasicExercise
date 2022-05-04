"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/26
Description: 数字黑洞，Kaprekar 常数
"""


def number_fraction(number):
    number_list = []
    for i in range(4):
        number_list.append(str(number % 10))
        number = number // 10
    return number_list


def main():
    N = int(input())
    n_list = number_fraction(N)
    result1 = int(''.join(sorted(n_list, reverse=True)))
    result2 = int(''.join(sorted(n_list)))
    ans = result1 - result2
    if N % 1111 == 0:  # 判断是否相等
        print('{:0>4d} - {:0>4d} = {:0>4d}'.format(N, N, 0))
    elif ans == 6174:  # 判断输入是否满足条件
        print('{:0>4d} - {:0>4d} = {:0>4d}'.format(result1, result2, ans))
    else:
        print('{:0>4d} - {:0>4d} = {:0>4d}'.format(result1, result2, ans))
        while ans != 6174:
            n_list = number_fraction(ans)
            result1 = int(''.join(sorted(n_list, reverse=True)))
            result2 = int(''.join(sorted(n_list)))
            ans = result1 - result2
            print('{:0>4d} - {:0>4d} = {:0>4d}'.format(result1, result2, ans))


main()