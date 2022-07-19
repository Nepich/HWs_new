from math import factorial


def fact_x(t):
    while t >= 0:
        yield factorial(t)
        t += 1


for x in fact_x(0):
    print(x)
    print()
