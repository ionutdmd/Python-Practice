# https://www.hackerrank.com/challenges/py-the-captains-room/problem
# Score: 10

from collections import Counter

size_of_group = int(input())
room_number_list = list(map(int, input().split()))
set_of_values = set(room_number_list)

c = Counter(room_number_list)
[print(key) for key, count in c.items() if count == 1]
