# https://projecteuler.net/problem=4

def palindrome(number):
    pal_number = 0
    while number > 0:
        pal_number = pal_number * 10 + number % 10
        number //= 10
    return pal_number


pal_list = []
for i in range(1000, 100, -1):
    for j in range(1000, 100, -1):
        if i * j == palindrome(i * j):
            pal_list.append(i * j)

print(max(pal_list))
