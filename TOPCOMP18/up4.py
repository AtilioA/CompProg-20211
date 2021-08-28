import math

n = int(input())

def isPrime(n):
    if n == 2:
        return "Primo"
    if n % 2 == 0 or n <= 1:
        return "Nao primo"

    nSqrt = int(math.sqrt(n)) + 1

    for divisor in range(3, nSqrt, 2):
        if n % divisor == 0:
            return "Nao primo"
    return "Primo"

print(isPrime(n), end='')

