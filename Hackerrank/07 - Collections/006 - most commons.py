# https://www.hackerrank.com/challenges/py-collections-deque/problem
# Score: 20
import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = list(input())
    s.sort()
    letter_counter = Counter(s)
    [print(key, value) for key, value in letter_counter.most_common(3)]
