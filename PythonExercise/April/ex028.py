"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/3
Description: 人口普查
"""

# 这种情况一个测试点过不去，应该是要考虑闰年和平年，相差一天还是有区别的
import sys


def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def main():
    n = int(input())
    j = 0
    month_day = [[31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334],
                 [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]]
    min = 200
    max = 0
    for i in range(n):
        name, date = sys.stdin.readline().split()
        year, month, day = list(map(int, date.split('/')))
        if year > 2014 or (year == 2014
                           and month > 9) or (year == 2014 and month == 9
                                              and day > 6):
            continue
        elif year < 1814 or (year == 1814
                             and month < 9) or (year == 1814 and month == 9
                                                and day < 6):
            continue
        else:
            j = j + 1
            if is_leap(year):
                age = 2014 - year + (month_day[1][month - 1] + day) / 365
            else:
                age = 2014 - year + (month_day[0][month - 1] + day) / 365
            if min > age:
                min = age
                min_name = name
            if max < age:
                max = age
                max_name = name
    if j == 0:
        print('{}'.format(j))
    else:
        print('{} {} {}'.format(j, max_name, min_name))


if __name__ == '__main__':
    main()
'''
# 字符串确实可以直接比较大小
import sys


def main():
    n = int(input())
    max_birthday = '2014/09/06'
    min_birthday = '1814/09/06'
    count = 0
    for i in range(n):
        name, birthday = sys.stdin.readline().split()
        if birthday > '2014/09/06' or birthday < '1814/09/06':
            continue
        else:
            count += 1
            if birthday > min_birthday:
                min_birthday = birthday
                min_name = name
            if birthday < max_birthday:
                max_birthday = birthday
                max_name = name

    if count == 0:
        print(count)
    else:
        print('{} {} {}'.format(count, max_name, min_name))


if __name__ == '__main__':
    main()
'''