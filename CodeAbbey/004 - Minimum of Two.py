# https://www.codeabbey.com/index/task_view/min-of-two

n = int(input())
rezultate = []
for i in range(n):
    valori = list(map(int, input().split(" ")))
    rezultate = rezultate + [min(valori)]

for numar in rezultate:
    print(numar, end=" ")
