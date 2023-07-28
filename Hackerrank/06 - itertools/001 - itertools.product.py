# https://www.hackerrank.com/challenges/itertools-product/problem
# Score: 10
from itertools import product

list_A = list(map(int, input().split(" ")))
list_B = list(map(int, input().split(" ")))

[print(result, end=" ") for result in list(product(list_A, list_B))]