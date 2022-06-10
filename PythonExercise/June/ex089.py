"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/5
Description: 狼人杀
思路：可以先假设两只狼，然后看所有人的逻辑是否都行得通，
因为多解时是输出最小的解，所以可以直接遍历假设狼的号码，
遇到正确解就直接中断并输出
"""
n = int(input())
s = [int(input()) for i in range(n)]  # 将他们说的话放在一个列表里

for i in range(1, n):  # 假设第一只狼
    for j in range(i + 1, n + 1):  # 假设第二只狼
        good_peo = 0  # 定义说谎的好人变量
        wolves = 0  # 定义说谎的狼人变量
        for k in range(1, n + 1):
            # 如果有人说i或者j是好人，或者说i和j之外的人是狼人，那么这个人说谎了
            if (s[k - 1] > 0 and
                (s[k - 1] == i or s[k - 1] == j)) or (s[k - 1] < 0
                                                      and abs(s[k - 1]) != i
                                                      and abs(s[k - 1]) != j):
                if k == i or k == j:  # 对照看这个说谎的人是不是狼人，是的话说谎的狼人+1
                    wolves += 1

                else:  # 看这个说谎的人是不是好人，是的话说谎的好人+1
                    good_peo += 1
        if wolves == 1 and good_peo == 1:  # 如果说谎的人包括一个好人和一个狼人
            print(i, j)  # 答案正确，直接输出
            exit()
print('No Solution')  # 遍历结束没有正确答案，输出‘No Solution’
