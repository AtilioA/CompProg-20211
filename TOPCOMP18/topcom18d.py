import math


def f(x):
    return int((1/2)*(1 + math.sqrt(8*x + 1)))


def run():
    cases = int(input())

    for i in range(cases):
        n = int(input())
        print(f(n))


run()
