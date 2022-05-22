"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/22
Description: 穿绳子
思路：由于每次串在一起就会折半，而长绳子折半的次数越多，
减少的就越多，所以从最短的开始串
bug：测试点二：输入1，1， 输出为0
"""
N = int(input())
input_list = list(map(int, input().split()))
input_list.sort()
sum = input_list[0]  # 测试点2  输入1 1，如果这个地方是sum=0 则输出0 因为1/2=0.5 舍掉了。
for i in range(1, N):
    sum = sum / 2 + input_list[i] / 2
print(int(sum))