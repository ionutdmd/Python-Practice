#https://www.codeabbey.com/index/task_view/linear-function

n = int(input())
results = []
for i in range(n):
    values = list(map(int,input().split(" ")))
    x1,y1,x2,y2 =  values[0], values[1], values[2], values[3]
    a = (y1 - y2)//(x1 - x2)
    b = y1 - a * x1
    results.append(a)
    results.append(b)

[print("("+str(results[i])+" "+str(results[i+1])+")", end=" ") for i in range(0,len(results),2)]