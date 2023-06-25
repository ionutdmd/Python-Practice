# https://www.hackerrank.com/challenges/designer-door-mat/problem
# Score: 10

N, M = map(int, input().split())
for i in range(1, (N + 1) // 2):
    print((".|." * (i * 2 - 1)).center(M, '-'))

print("WELCOME".center(M, '-'))

for i in range((N - 1) // 2, 0, -1):
    print((".|." * (i * 2 - 1)).center(M, '-'))
