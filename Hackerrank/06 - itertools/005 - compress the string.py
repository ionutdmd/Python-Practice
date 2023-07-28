# https://www.hackerrank.com/challenges/compress-the-string/problem
# Score: 20
from itertools import groupby

S = input()

[print(f"({len(list(group))}, {key})", end=" ") for key, group in groupby(S)]
