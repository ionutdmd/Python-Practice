# https://www.codeabbey.com/index/task_view/modulo-and-time-difference

n = int(input())
results = []
for i in range(n):
    values = list(map(int, input().split(" ")))
    day1, hour1, min1, sec1 = values[0], values[1], values[2], values[3]
    day2, hour2, min2, sec2 = values[4], values[5], values[6], values[7]
    sum_sec1 = sec1 + min1 * 60 + hour1 * 60 * 60 + day1 * 24 * 60 * 60
    sum_sec2 = sec2 + min2 * 60 + hour2 * 60 * 60 + day2 * 24 * 60 * 60
    difference = sum_sec2 - sum_sec1
    results.append(difference // (24 * 60 * 60))
    difference = difference % (24 * 60 * 60)
    results.append(difference // (60 * 60))
    difference = difference % (60 * 60)
    results.append(difference // 60)
    results.append(difference % 60)

[print("(" + str(results[i]) + " " + str(results[i + 1]) + " " + str(results[i + 2]) + " " + str(results[i + 3]) + ")",
       end=" ") for i in range(0, len(results), 4)]
