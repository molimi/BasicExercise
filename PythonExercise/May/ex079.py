"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/29
Description: 延迟的回文数
思路：先分解数字，并判断是否是回文数，然后执行操作，10次后还不是结束循环
"""


def is_palindromes(number):
    temp_list = list(str(number))
    length = len(temp_list)
    iter = int(length / 2)
    for i in range(iter):
        if temp_list[i] != temp_list[length - i - 1]:
            return False
    return True


def main():
    number = int(input())
    old_number = number
    for i in range(10):
        if is_palindromes(old_number):
            print('{} is a palindromic number.'.format(old_number))
            break
        else:
            temp_list = list(str(old_number))
            temp_list.reverse()
            reverse_number = int(''.join(temp_list))
            new_number = old_number + reverse_number
            print('{} + {} = {}'.format(old_number, reverse_number,
                                        new_number))
            old_number = new_number
    else:
        print('Not found in 10 iterations.')

    # print(is_palindromes(255552))
    # print(is_palindromes(2554552))
    # print(is_palindromes(0))


main()