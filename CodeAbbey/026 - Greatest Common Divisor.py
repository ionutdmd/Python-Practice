# https://www.codeabbey.com/index/task_view/greatest-common-divisor

def gcd(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x


n = int(input())
results = []
for i in range(n):
    values = list(map(int, input().split(" ")))
    results.append(gcd(values[0], values[1]))
    results.append((values[0] * values[1]) // gcd(values[0], values[1]))

[print("(" + str(results[i]) + " " + str(results[i + 1]) + ")", end=" ") for i in range(0, len(results), 2)]
