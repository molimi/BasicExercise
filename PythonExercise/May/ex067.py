"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/21
Description: 尝试密码
思路：题目本身不难，主要是理解逻辑问题，每错误三次则自动锁账号
"""
password, times = input().split()
times = int(times)
count = 0
flag = True
while flag:
    input_str = input()
    if input_str == '#':
        flag = False
    elif input_str == password and count < times:
        print('Welcome in')
        flag = False
    elif input_str != password and count < times:
        print('Wrong password: {}'.format(input_str))
    if count >= times:
        print('Account locked')
        flag = False
    count += 1