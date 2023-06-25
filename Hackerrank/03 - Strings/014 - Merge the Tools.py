# https://www.hackerrank.com/challenges/merge-the-tools/problem
# Score: 40

def merge_the_tools(string, k):
    # your code goes here
    substrings = []
    for i in range(0, len(string), k):
        substrings.append(string[i:i + k])
    for substring in substrings:
        solution = ""
        for letter in substring:
            if letter not in solution:
                solution += letter
        print(solution)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
