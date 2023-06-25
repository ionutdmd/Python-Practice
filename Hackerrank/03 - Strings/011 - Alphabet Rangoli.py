# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
# Score: 20

def print_rangoli(size):
    # your code goes here

    alphabet_list = list(map(chr, range(97, 123)))
    alphabet = "".join(alphabet_list)
    result = []
    for i in range(size):
        s = "-".join(alphabet[i:size])
        result.append((s[::-1]+s[1:]).center(4*size-3, "-"))

    print("\n".join(result[:0:-1]+result))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
