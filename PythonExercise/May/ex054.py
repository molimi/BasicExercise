"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/16
Description: 计算符合要求的数字，并求平均值
建议使用正则表达式判断
否则会有 .12和12.这样的通过，还有1000.00之类的，注意这个正则表大四的写法
"""
import re


def check(num):
    pattern = re.compile(
        r'^[-]?(\d{0,3}|1000)$|^[-]?\d{0,3}\.[0-9]{0,2}$|^[-]?1000\.0{0,2}$')
    result = pattern.match(num)
    return True if result else False


def main():
    N = int(input())
    input_list = input().split()
    count, sum = 0, 0
    for i in range(N):
        if check(input_list[i]):
            sum += float(input_list[i])
            count += 1
        else:
            print('ERROR: {} is not a legal number'.format(input_list[i]))

    if count == 0:
        print('The average of 0 numbers is Undefined')
    elif count == 1:
        print('The average of {:d} number is {:.2f}'.format(
            count, sum / count))
    else:
        print('The average of {:d} numbers is {:.2f}'.format(
            count, sum / count))


main()