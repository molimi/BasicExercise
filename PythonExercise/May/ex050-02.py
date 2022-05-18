"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/12
Description: 螺旋矩阵
思路：
计算m*n的矩阵，然后排列顺序并填充，
思路一：按一层一层来写，先上右下左
思路二：逐个元素填充
"""


def factorization(N):  # 因式分解
    iter = int(N**0.5)
    for i in range(iter, 0, -1):
        if N % i == 0:
            return N // i, i


def main():
    N = int(input())
    input_list = list(map(int, input().split()))
    input_list.sort(reverse=True)  # 对输入列表从大到小排序
    m, n = factorization(N)
    result_list = [[0 for j in range(n)]
                   for i in range(m)]  # 构造二维数组，用来记录螺旋访问的结果
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 记录四个移动方向，依次为右、下、左、上
    direction_index = 0  # 记录当前方向
    corr_x, corr_y = 0, -1  # 当前坐标
    vertical = False  # 是否在竖直方向上前进，否就是在水平方向上前进
    vertical_count = m - 1  # 记录本次竖直方向上应访问的元素个数
    horizontal_count = n  # 记录本次水平方向上应访问的元素个数
    count_line = 0  # 记录当前方向上访问过的元素个数
    count = 0  # 记录已经访问过的元素总个数
    while count < N:
        direction = directions[direction_index]
        corr_x += direction[0]  # 前进一步
        corr_y += direction[1]
        result_list[corr_x][corr_y] = input_list[count]  # 螺旋赋值
        count += 1
        count_line += 1  # 记录数都加一
        if vertical and count_line == vertical_count:  # 判断在竖直方向是否达到尽头
            vertical = False  # 接下来是水平方向
            direction_index = (direction_index + 1) % 4  # 下一个方向
            vertical_count -= 1  # 下次的竖直方向上元素个数要减一
            count_line = 0  # 下个方向上的元素个数置零
        if not vertical and count_line == horizontal_count:  # 如果是在水平方向上走到头了
            vertical = True  # 接下来走竖直方向
            direction_index = (direction_index + 1) % 4  # 下一个方向
            horizontal_count -= 1  # 下次的水平方向上的元素个数要减一
            count_line = 0  # 下个方向的元素个数置零
    for t in range(m):
        print(' '.join(list(map(str, result_list[t]))))


main()