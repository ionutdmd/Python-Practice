#https://www.codeabbey.com/index/task_view/fahrenheit-celsius

import math

values_far = list(map(int,input().split(" ")))
n = values_far[0]
values_celsius = []
for i in range(1,n+1):
    if float((values_far[i] - 32) / 1.8 ) % 1 == 0.5:
        values_celsius.append(math.ceil((values_far[i] - 32) / 1.8 ))
    else:
        values_celsius.append(round((values_far[i] - 32) / 1.8))

for i in range(n):
    print(values_celsius[i],end=" ")