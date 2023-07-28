# https://www.hackerrank.com/challenges/itertools-combinations/problem
# Score: 10
from itertools import combinations

S, k = input().split()
S = list(S)
k = int(k)
S.sort()
for i in range(1, k+1):
    [print("".join(result)) for result in list(combinations(S, i))]
