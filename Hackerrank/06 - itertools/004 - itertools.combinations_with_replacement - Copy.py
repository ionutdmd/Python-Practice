# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
# Score: 10
from itertools import combinations_with_replacement

S, k = input().split()
S = list(S)
k = int(k)
S.sort()
[print("".join(result)) for result in list(combinations_with_replacement(S, k))]
