# https://www.codeabbey.com/index/task_view/bubble-sort

n = int(input())
values = list(map(int, input().split(" ")))
pass_values = 0
swaps = 0
more_swaps = True
while more_swaps:
    more_swaps = False
    for i in range(0, n-1):
        if values[i] > values[i+1]:
            t = values[i]
            values[i] = values[i+1]
            values[i+1] = t
            swaps += 1
            more_swaps = True
    pass_values += 1

print(pass_values, swaps)
