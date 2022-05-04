"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/26
Description: 月饼收益最大
第一行：分别给出月饼种类和市场需求
第二行给出每种月饼库存量
第三行给出每种月饼总售价
思路：就是先卖单价最高的月饼
"""
N, needs = list(map(int, input().split()))
inventory_list = list(map(float, input().split()))
price_list = list(map(float, input().split()))

total_list = list(zip(inventory_list, price_list))
total_list.sort(reverse=True, key=lambda item: item[1] / item[0])
sales = 0
i = 0
profit = 0
while needs:
    if i == N:
        break
    elif needs > total_list[i][0]:
        needs = needs - total_list[i][0]
        profit = profit + total_list[i][1]
    else:
        profit = profit + needs * total_list[i][1] / total_list[i][0]
        needs = 0
    i += 1
print('{:.2f}'.format(profit))