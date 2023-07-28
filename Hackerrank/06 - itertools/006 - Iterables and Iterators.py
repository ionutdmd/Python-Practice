# https://www.hackerrank.com/challenges/iterables-and-iterators/problem
# Score: 40
from itertools import combinations

N = int(input())
char_list = list(map(str, input().split()))
K = int(input())

combinations_list = list(combinations(char_list, K))
number_of_appearances = sum("a" in item for item in combinations_list)
print(number_of_appearances/len(combinations_list))