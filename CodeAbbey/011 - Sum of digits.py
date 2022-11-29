#https://www.codeabbey.com/index/task_view/sum-of-digits

n = int(input())
rezultate = []
for i in range(n):
    input_values = list(map(int,input().split(" ")))
    result = input_values[0] * input_values[1] + input_values[2]
    digit_sum = 0
    while result > 0:
        digit_sum += result % 10
        result = result // 10
    rezultate.append(digit_sum)

[print(rezultate[i], end=" ") for i in range(len(rezultate))]