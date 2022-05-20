"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/20
Description: 判断题
"""

N, M = list(map(int, input().split()))
score_list = list(map(int, input().split()))
right_list = list(map(int, input().split()))

for i in range(N):
    score = 0
    student_list = list(map(int, input().split()))
    for j in range(M):
        if student_list[j] == right_list[j]:
            score += score_list[j]
    print(score)