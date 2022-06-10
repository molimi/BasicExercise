"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/5
Description: 有多少不同的值
bug: 题目没说第三个数值必须是整数，所以就不用考虑都为整数
"""


def compare(m, n):
    if m == n:
        return 'Ping'
    elif m > n:
        return 'Gai'
    else:
        return 'Cong'


me, x, y = list(map(int, input().split()))
result_list = []
for a in range(1, 10):
    for b in range(10):
        one = 10 * a + b
        two = 10 * b + a
        three = abs(one - two)
        if x * two == y * three:
            result_list.append((one, two, two / y))

if len(result_list):
    result_list.sort(key=lambda item: item[0])
    print('{} {} {} {}'.format(result_list[-1][0],
                               compare(me, result_list[-1][0]),
                               compare(me, result_list[-1][1]),
                               compare(me, result_list[-1][2])))
else:
    print('No Solution')