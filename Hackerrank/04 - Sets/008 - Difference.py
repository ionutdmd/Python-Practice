# https://www.hackerrank.com/challenges/py-set-difference-operation/problem
# Score: 10

english_subscribers_number = int(input())
english_subscribers = set(map(int, input().split()))
french_subscribers_number = int(input())
french_subscribers = set(map(int, input().split()))
print(len(english_subscribers.difference(french_subscribers)))
