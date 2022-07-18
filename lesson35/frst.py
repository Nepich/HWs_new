cache = []


def cacher(func):
    def wrapper(*args):
        if func(*args) not in cache and len(cache) <= 5:
            cache.insert(0, func(*args))
            if len(cache) > 5:
                cache.pop(-1)
        return func(*args)
    return wrapper


@cacher
def some_func(a, b):
    c = a+b
    return c


print(some_func(1, 2))
print(some_func(3, 4))
print(some_func(2, 4))
print(some_func(1, 4))
print(some_func(7, 4))
print(some_func(6, 4))
print(cache)
