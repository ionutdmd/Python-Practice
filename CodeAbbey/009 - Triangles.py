#https://www.codeabbey.com/index/task_view/triangles

n = int(input())
rezultate = []
for i in range(n):
    input_values = list(map(int,input().split(" ")))
    a, b, c = input_values[0], input_values[1], input_values[2]
    if a+b<c or a+c<b or b+c<a:
        rezultate.append(0)
    else:
        rezultate.append(1)

[print(rezultate[i], end=" ") for i in range(len(rezultate))]