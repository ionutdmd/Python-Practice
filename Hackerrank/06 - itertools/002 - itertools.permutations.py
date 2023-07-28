# https://www.hackerrank.com/challenges/itertools-permutations/problem
# Score: 10
from itertools import permutations

S, k = input().split()
S = list(S)
k = int(k)
S.sort()

[print("".join(result)) for result in list(permutations(S, k))]
