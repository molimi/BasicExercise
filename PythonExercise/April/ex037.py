"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/6
Description: 找零钱
"""


def return_money(need_money, give_money):
    galleon0, sickle0, knut0 = list(map(int, need_money.split('.')))
    money1 = galleon0 * 17 * 29 + sickle0 * 29 + knut0
    galleon1, sickle1, knut1 = list(map(int, give_money.split('.')))
    money2 = galleon1 * 17 * 29 + sickle1 * 29 + knut1
    ret_money = money2 - money1
    result_list = [0, 0, 0]
    money = abs(ret_money)
    result_list[2] = str(money % 29)
    result_list[1] = str((money // 29) % 17)
    result_list[0] = str(money // (17 * 29))
    if ret_money < 0:
        return '-' + '.'.join(result_list)
    else:
        return '.'.join(result_list)


def main():
    p, a = input().split()
    print(return_money(p, a))


main()