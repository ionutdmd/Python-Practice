# https://www.hackerrank.com/challenges/collections-counter/problem
# Score: 10
from collections import Counter

x = int(input())
shoe_sizes = list(map(int, input().split()))
n = int(input())

sizes_dict = Counter(shoe_sizes)
sales_income = 0
for _ in range(n):
    size, value = map(int, input().split())
    if sizes_dict[size] > 0:
        sales_income += value
        sizes_dict[size] -= 1

print(sales_income)


