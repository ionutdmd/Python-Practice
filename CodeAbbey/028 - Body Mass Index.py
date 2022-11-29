#https://www.codeabbey.com/index/task_view/body-mass-index

n = int(input())
rezultate = []
for i in range(n):
    input_values = list(map(float,input().split(" ")))
    bmi = input_values[0] / (input_values[1] ** 2)
    if bmi<18.5:
        rezultate.append("under")
    elif bmi<25:
        rezultate.append("normal")
    elif bmi<30:
        rezultate.append("over")
    else:
        rezultate.append("obese")


[print(rezultate[i], end=" ") for i in range(len(rezultate))]