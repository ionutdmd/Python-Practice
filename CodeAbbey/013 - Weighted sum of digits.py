#https://www.codeabbey.com/index/task_view/weighted-sum-of-digits

n = int(input())
rezultate = []
values = list(map(int,input().split(" ")))
for i in range(0,n):
    counter = len(str(values[i]))
    wsd = 0
    numar = values[i]
    while numar>0:
        wsd += (numar % 10) * counter
        counter -= 1
        numar = numar // 10
    rezultate.append(wsd)


[print(rezultate[i], end=" ") for i in range(len(rezultate))]