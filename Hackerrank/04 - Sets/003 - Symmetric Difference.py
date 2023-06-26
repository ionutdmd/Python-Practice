# https://www.hackerrank.com/challenges/symmetric-difference/problem
# Score: 10

size_of_M = int(input())
values_of_M = set(map(int, input().split()))
size_of_N = int(input())
values_of_N = set(map(int, input().split()))

symmetric_difference = values_of_M.symmetric_difference(values_of_N)
symmetric_difference = sorted(symmetric_difference)

[print(number) for number in symetric_difference]
