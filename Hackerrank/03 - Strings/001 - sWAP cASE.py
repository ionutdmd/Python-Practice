# https://www.hackerrank.com/challenges/swap-case/problem
# Score: 10

def swap_case(s):
    return_s = ''
    for letter in s:
        if letter.upper() == letter:
            return_s += letter.lower()
        else:
            return_s += letter.upper()
    return return_s
