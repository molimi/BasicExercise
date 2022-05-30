"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/30
Description: MOOC期终成绩
"""
P, M, N = list(map(int, input().split()))
student_dict = {}
for i in range(P):
    number, score = input().split()
    if int(score) >= 200:
        student_dict[number] = [int(score), -1, -1]

for j in range(M):
    number, score = input().split()
    if number in student_dict:
        student_dict[number][1] = int(score)

for k in range(N):
    number, score = input().split()
    if number in student_dict:
        student_dict[number][2] = int(score)

result_dict = {}
for item in student_dict:
    GM = student_dict[item][1]
    GF = student_dict[item][2]
    if GM > GF:
        G = round(GM * 0.4 + GF * 0.6)
    else:
        G = GF
    if G >= 60:
        result_dict[item] = [student_dict[item][0], GM, GF, G]

result_list = sorted(result_dict.items(), key=lambda item: item[0])
result_list.sort(key=lambda item: item[1][-1], reverse=True)
for k in range(len(result_list)):
    print('{} {} {} {} {}'.format(result_list[k][0], result_list[k][1][0],
                                  result_list[k][1][1], result_list[k][1][2],
                                  result_list[k][1][3]))