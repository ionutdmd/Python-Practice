# https://www.hackerrank.com/challenges/py-set-add/problem
# Score: 10

number_of_stamps = int(input())
stamps_set = set()
for _ in range(number_of_stamps):
    stamps_set.add(input())

print(len(stamps_set))
