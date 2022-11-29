#https://www.codeabbey.com/index/task_view/median-of-three

n = int(input())
rezultate = []
for i in range(n):
    input_values = list(map(int,input().split(" ")))
    input_values.sort()
    rezultate.append(input_values[1])

[print(rezultate[i], end=" ") for i in range(len(rezultate))]