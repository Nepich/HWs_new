import time


def timer(func):
    def wrapper(*args, **kwargs):
        time_start = time.perf_counter()
        res = func(*args, **kwargs)
        print(time.perf_counter()-time_start)
        return res
    return wrapper


@timer
def some_func(a, b):
    return a**b


print(some_func(2, 123))
