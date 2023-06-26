# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
# Score: 10

english_subscribers_number = int(input())
english_subscribers = set(map(int, input().split()))
french_subscribers_number = int(input())
french_subscribers = set(map(int, input().split()))
print(len(english_subscribers.symmetric_difference(french_subscribers)))
