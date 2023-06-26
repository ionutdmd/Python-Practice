# https://www.hackerrank.com/challenges/py-check-subset/problem
# Score: 10

number_of_test_cases = int(input())

for _ in range(number_of_test_cases):
    size_of_set_A = int(input())
    elements_of_set_A = set(map(int, input().split()))
    size_of_set_B = int(input())
    elements_of_set_B = set(map(int, input().split()))

    print(elements_of_set_A.issubset(elements_of_set_B))
