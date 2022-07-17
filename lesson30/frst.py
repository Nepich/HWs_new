def division():
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
    except ValueError:
        return "Сказал же число введи, все сломал, дурачок!!!"
    try:
        c = a/b
    except ZeroDivisionError:
        return "Делишь на ноль! Совсем ополаумел, хочешь создать черную дыру?"
    return c


print(division())
