"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/14
Description: 卡拉兹(Callatz)猜想
"""
n = int(input())
step = 0
while True:
    if n != 1:
        step += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n + 1) / 2
    else:
        break

print(step)
