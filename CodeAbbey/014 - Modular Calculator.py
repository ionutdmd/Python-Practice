# https://www.codeabbey.com/index/task_view/modular-calculator

result = int(input())
values = list(map(str, input().split(" ")))
while values[0] != "%":
    if values[0] == "+":
        result = result + int(values[1])
    else:
        result = result * int(values[1])
    values = list(map(str, input().split(" ")))

result = result % int(values[1])
print(result)
