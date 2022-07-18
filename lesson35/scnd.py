def logger(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        elements = ', '.join(list(map(str, args)))
        named_elements = ', '.join(list(map(str, kwargs)))
        with open("log.txt", "a", encoding="utf-8") as file:
            file.write(f'Вызов функции {func.__name__}\n')
            file.write(f'Входные неименованные данные: {elements}\n')
            file.write(f'Входные именованные данные: {named_elements}\n')
            file.write(f'Результат выполнения функции: {res}\n')
            file.write(f'\n')
        return res
    return wrapper


@logger
def some_func(a, b):
    c = a+b
    return c


print(some_func(2, 3))

