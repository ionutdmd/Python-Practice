# https://projecteuler.net/problem=5

def gcd(x, y):  # Calculate the greater common divisor of 2 numbers
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x


number_limit = 20  # Change value for other examples
result = 1
for i in range(1, number_limit + 1):
    # Multiple of 2 numbers can be calculated using formula [a,b] = (a * b) / gcd(a,b)
    result = (result * i) // gcd(result, i)

print(result)
