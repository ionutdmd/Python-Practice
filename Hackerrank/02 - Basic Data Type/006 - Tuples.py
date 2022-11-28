# https://www.hackerrank.com/challenges/python-tuples/problem
# Score: 10

N = int(input())
l = map(int, input().split())
print(hash(tuple(l)))
