"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/9
Description: 座位号
"""
import sys

n = int(input())
seat_dict = {}

for i in range(n):
    admission_number, seat_number, exam_number = sys.stdin.readline().split()
    seat_dict[seat_number] = (admission_number, exam_number)

m = int(input())
number_list = input().split()
for j in range(m):
    print(' '.join(seat_dict[number_list[j]]))