# https://www.hackerrank.com/challenges/python-string-formatting/problem
# Score: 10

def print_formatted(number):
    # your code goes here
    padding = len(bin(number)[2:])
    for i in range(1, number + 1):
        print(str(i).rjust(padding), oct(i)[2:].rjust(padding), hex(i)[2:].upper().rjust(padding), bin(i)[2:].rjust(padding))



if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
