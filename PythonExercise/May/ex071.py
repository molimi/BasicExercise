"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/22
Description: 赌博
"""
T, K = list(map(int, input().split()))
res = T
input_list = []
for i in range(K):
    input_list.append(list(map(int, input().split())))

for index in range(K):
    if res == 0:
        print('Game Over.')
        break
    if input_list[index][2] > res:
        print('Not enough tokens.  Total = {}.'.format(res))
    else:
        if input_list[index][
                1] == 0 and input_list[index][0] > input_list[index][3]:
            res += input_list[index][2]
            print('Win {}!  Total = {}.'.format(input_list[index][2], res))
        if input_list[index][
                1] == 0 and input_list[index][0] < input_list[index][3]:
            res -= input_list[index][2]
            print('Lose {}.  Total = {}.'.format(input_list[index][2], res))
            if res == 0:
                print('Game Over.')
                break
        if input_list[index][
                1] == 1 and input_list[index][0] < input_list[index][3]:
            res += input_list[index][2]
            print('Win {}!  Total = {}.'.format(input_list[index][2], res))
        if input_list[index][
                1] == 1 and input_list[index][0] > input_list[index][3]:
            res -= input_list[index][2]
            print('Lose {}.  Total = {}.'.format(input_list[index][2], res))
            if res == 0:
                print('Game Over.')
                break