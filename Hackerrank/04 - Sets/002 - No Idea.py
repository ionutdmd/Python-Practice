# https://www.hackerrank.com/challenges/no-idea/problem
# Score: 50

def happiness(a, s, counter):
    result = 0
    for number in a:
        if number in s:
            result += counter
    return result


n, m = map(int, input().split())
array = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

print(happiness(array, set_a, 1) + happiness(array, set_b, -1))
