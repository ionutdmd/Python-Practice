# https://www.hackerrank.com/challenges/capitalize/problem
# Score: 20

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    solution = s.split(" ")
    solution = [word.capitalize() for word in solution]
    return " ".join(solution)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

