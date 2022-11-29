# https://www.codeabbey.com/index/task_view/sums-in-loop

n = int(input())
rezultate = []
for i in range(n):
    valori = list(map(int, input().split(" ")))
    rezultate = rezultate + [sum(valori)]

for numar in rezultate:
    print(numar, end=" ")
