# https://www.codeabbey.com/index/task_view/collatz-sequence

n = int(input())
values = list(map(int, input().split(" ")))
results = []
for i in range(n):
    number = values[i]
    counter = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number +1
        counter +=1
    results.append(counter)

[print(results[i], end=" ") for i in range(len(results))]
