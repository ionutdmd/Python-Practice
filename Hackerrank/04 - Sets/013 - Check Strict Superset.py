# https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# Score: 10

elements_of_set_A = set(map(int, input().split()))
number_of_test_cases = int(input())

result = True
for _ in range(number_of_test_cases):
    elements_of_set_B = set(map(int, input().split()))
    if not elements_of_set_A.issuperset(elements_of_set_B):
        result = False
        break
print(result)
