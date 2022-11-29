#https://www.codeabbey.com/index/task_view/dice-rolling

import math

n = int(input())
rezultate = []
for i in range(n):
    value = float(input())
    rezultate.append(math.floor(value*6) + 1)

[print(rezultate[i], end=" ") for i in range(len(rezultate))]