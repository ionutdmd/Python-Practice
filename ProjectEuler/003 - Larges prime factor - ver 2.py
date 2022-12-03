# https://projecteuler.net/problem=3
import sympy

number = int(input("Enter a number: "))  # Number to test 600851475143
# Create a list of divisors
divisor_list = []
divisor = 2
while number > 1:
    if number % divisor == 0:
        divisor_list.append(divisor)
        number = number // divisor
        divisor = 2
    else:
        divisor += 1

# Checking for prime divisors
maxim = 1
for num in set(divisor_list):
    if sympy.isprime(num) and num > maxim:
        maxim = num

# Printing result
print(maxim)
