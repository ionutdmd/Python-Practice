# https://www.hackerrank.com/challenges/py-collections-deque/problem
# Score: 20
from collections import deque

d = deque()
n = int(input())

for _ in range(n):
    function_details = list(input().split())

    try:
        exec(f"d.{function_details[0]}({function_details[1]})")
    except:
        exec(f"d.{function_details[0]}()")

[print(value, end=" ") for value in d]




