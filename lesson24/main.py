def calc(a, b, c):
    if a != 0 and b != 0 and c != 0:
        d = b ** 2 - 4 * a * c
        if d > 0:
            x1 = (-b + d ** 0.5) / 2 * a
            x2 = (-b - d ** 0.5) / 2 * a
            return x1, x2
        elif d == 0:
            x = (-b) / 2 * a
            return x
        else:
            return 'Корней нет'
    elif a!= 0 and b == 0 and c == 0:
        return 0
    elif a!= 0 and b != 0 and c == 0:
        x = -b / a
        return 0, x
    elif a!= 0 and b == 0 and c != 0:
        x = -c / a
        if x >= 0:
            x1 = -(x ** 0.5)
            x2 = x ** 0.5
            return x1, x2
        else:
            return 'Корней нет'
    elif a == 0 and b != 0:
        x = -c / b
        return x
    elif a == 0 and b == 0:
        return 'Корней нет'


a, b, c = int(input("Введите а: ")), int(input("Введите b: ")), int(input("Введите c: "))
print(calc(a, b, c))
