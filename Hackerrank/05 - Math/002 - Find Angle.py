# https://www.hackerrank.com/challenges/find-angle/problem
# Score: 10
from math import atan, degrees

length_AB = int(input())
length_BC = int(input())

angle = atan(length_AB/length_BC)
degree_sign = u'\N{DEGREE SIGN}'
print(f"{round(degrees(angle))}{degree_sign}")


