#https://www.codeabbey.com/index/task_view/array-checksum

n = int(input())
rezultate = []
values = list(map(int,input().split(" ")))
result = 0
for value in values:
    result = ((result + value) * 113) % 10000007

print(result)