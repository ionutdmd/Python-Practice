#https://www.codeabbey.com/index/task_view/arithmetic-progression

n = int(input())
rezultate = []
for i in range(n):
    input_values = list(map(int,input().split(" ")))
    result = 0
    for j in range(input_values[2]):
        result = result + input_values[0] + input_values[1] * j
    rezultate.append(result)

[print(rezultate[i], end=" ") for i in range(len(rezultate))]