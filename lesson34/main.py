from copy import deepcopy
from math import *


def map0(func, some_iterable):
    new_iterable = deepcopy(some_iterable)
    for elem in range(len(some_iterable)):
        new_iterable[elem] = (func(some_iterable[elem]))
    return new_iterable


def reduce0(func, some_iterable, start=0):
    for elem in some_iterable:
        start = func([start, elem])
    return start


print(map0(sqrt, [1, 2, 3, 4]))
print(reduce0(sum, [1, 2, 3, 4], start=10))
