# https://www.codeabbey.com/index/task_view/rounding

import math

n = int(input())
rezultate = []
for i in range(n):
    valori = list(map(float, input().split(" ")))
    rezultat = valori[0] / valori[1]
    if float(rezultat) % 1 == 0.5:
        rezultate.append(str(math.ceil(rezultat)))
    else:
        rezultate.append(str(round(rezultat)))

for numar in rezultate:
    print(numar, end=" ")
