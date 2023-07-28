# https://www.hackerrank.com/challenges/maximize-it/problem
# Score: 50
from itertools import product

K, M = input().split()
all_lists = []
S = 0
for _ in range(int(K)):
    row_number_list = list(map(int, input().split()))
    all_lists.append(row_number_list[1:])

maxim_value = 0
for combination in product(*all_lists):
    current_value = sum(value ** 2 for value in combination)
    if (current_value % int(M)) > maxim_value:
        maxim_value = current_value % int(M)

print(maxim_value)

