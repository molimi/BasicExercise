"""
Version: 0.1
Author: CarpeDiem
Date: 2022/6/10
Description: 销量冠军
"""
N = int(input())
money_list = []
sales_list = []
for i in range(N):
    id, price, times = input().split()
    money_list.append((id, int(price) * int(times)))
    sales_list.append((id, int(times)))

money_list.sort(key=lambda item: item[1])
sales_list.sort(key=lambda item: item[1])

print(sales_list[-1][0], sales_list[-1][1])
print(money_list[-1][0], money_list[-1][1])