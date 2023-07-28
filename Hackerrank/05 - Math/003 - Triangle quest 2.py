# https://www.hackerrank.com/challenges/triangle-quest-2
# Score: 20
# for i in range(1, int(input()) + 1):  # More than 2 lines will result in 0 score. Do not leave a blank line also
#     print("".join(list(map(str, range(1, i+1))))+"".join(reversed(list(map(str, range(1, i))))))

# for i in range(1, int(input()) + 1):  # More than 2 lines will result in 0 score. Do not leave a blank line also
#     print(int(i*"1")**2)

for i in range(1, int(input()) + 1):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**i // 9) ** 2)