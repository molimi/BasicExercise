"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/19
Description: 将输入按规定输出
"""

input_list = list(map(int, input().split()))
input_list = input_list[1:]
result = ''
a1, a2, a3, a4, a5 = [], [], [], [], []
for i, iter in enumerate(input_list):
    if iter % 5 == 0 and iter % 2 == 0:
        a1.append(iter)
    elif iter % 5 == 1:
        a2.append(iter)
    elif iter % 5 == 2:
        a3.append(iter)
    elif iter % 5 == 3:
        a4.append(iter)
    elif iter % 5 == 4:
        a5.append(iter)
    else:
        continue
result = ''

if len(a1) == 0:
    result += 'N' + ' '
else:
    result += str(sum(a1)) + ' '
if len(a2) == 0:
    result += 'N' + ' '
else:
    ans = 0
    for i in range(len(a2)):
        ans += (-1)**i * a2[i]
    result += str(ans) + ' '
if len(a3) == 0:
    result += 'N' + ' '
else:
    result += str(len(a3)) + ' '
if len(a4) == 0:
    result += 'N' + ' '
else:
    result += str(round(sum(a4) / len(a4), 1)) + ' '
if len(a5) == 0:
    result += 'N' + ' '
else:
    result += str(max(a5)) + ' '
print(result.strip())