#https://www.codeabbey.com/index/task_view/average-of-array

import math

def int_round(numar):
    if numar % 1 == 0.5:
        return math.ceil(numar)
    else:
        return round(numar)

n = int(input())
rezultate = []
for i in range(n):
    values = list(map(int,input().split(" ")))
    rezultate.append(int_round(sum(values)/(len(values)-1)))

[print(rezultate[i], end=" ") for i in range(len(rezultate))]