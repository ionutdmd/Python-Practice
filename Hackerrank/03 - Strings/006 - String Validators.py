# https://www.hackerrank.com/challenges/find-a-string/problem
# Score: 10

if __name__ == '__main__':
    s = input()
    result = [False, False, False, False, False]
    for letter in s:
        if letter.isalnum() or result[0]:
            result[0] = True
        if letter.isalpha() or result[1]:
            result[1] = True
        if letter.isdigit() or result[2]:
            result[2] = True
        if letter.islower() or result[3]:
            result[3] = True
        if letter.isupper() or result[4]:
            result[4] = True
    [print(r) for r in result]
