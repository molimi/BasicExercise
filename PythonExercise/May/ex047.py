"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/11
Description: 找出冠军队
"""
n = int(input())
team_dict = {}
for i in range(n):
    team, score = input().split()
    team_number, _in = team.split('-')
    if team_number in team_dict:
        team_dict[team_number] += int(score)
    else:
        team_dict[team_number] = int(score)

result_list = sorted(team_dict.items(), key=lambda item: item[1])
print(result_list[-1][0] + ' ' + str(result_list[-1][1]))