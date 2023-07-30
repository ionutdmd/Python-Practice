# https://www.hackerrank.com/challenges/word-order/problem
# Score: 50
from collections import OrderedDict

n = int(input())
word_list = OrderedDict()
for _ in range(n):
    next_word = input()
    try:
        word_list[next_word] += 1
    except KeyError:
        word_list[next_word] = 1

print(len(word_list))
[print(value, end=" ") for key, value in word_list.items()]


