#https://projecteuler.net/problem=2

class Fibonacci:

    def __init__(self, i1=0, i2=1):
        self.memo = {0: i1, 1: i2}

    def __call__(self, n):
        if n not in self.memo:
            self.memo[n] = self.memo[n - 1] + self.memo[n - 2]
        return self.memo[n]


fib = Fibonacci()
sum = 0
i = 0
while fib(i) <= 4000000:
    if fib(i) % 2 == 0:
        sum += fib(i)
    i += 1
print(sum)
