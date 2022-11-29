#https://www.codeabbey.com/index/task_view/array-counters

input_values1 = list(map(int,input().split(" ")))
m, n = input_values1[0], input_values1[1]
input_data = list(map(int,input().split(" ")))
results = []
for i in range(1, n+1):
    results.append(input_data.count(i))

[print(results[i], end=" ") for i in range(len(results))]