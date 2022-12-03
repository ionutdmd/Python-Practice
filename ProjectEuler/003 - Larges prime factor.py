# https://projecteuler.net/problem=3

def is_prime(n):
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return False
    return True


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

# Check for prime divisor
maxim = 1
for num in set(divisor_list):
    if is_prime(num) and maxim < num:
        maxim = num

print(maxim)
