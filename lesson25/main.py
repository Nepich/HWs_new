def move(x1, y1, x2, y2):
    if ((x1 + 1) == x2 and (y1 + 2) == y2) or ((x1 + 2) == x2 and (y1 + 1) == y2) or ((x1 - 1) == x2 and (y1 + 2) == y2) \
            or ((x1 + 1) == x2 and (y1 - 2) == y2) or ((x1 + 2) == x2 and (y1 - 2) == y2) \
            or ((x1 - 1) == x2 and (y1 - 2) == y2) or ((x1 - 2) == x2 and (y1 - 1) == y2) \
            or ((x1 - 2) == x2 and (y1 + 1) == y2):
        return True
    else:
        return False


def menu():
    print("1) ввести данные \n2) выход")
    a = int(input())
    while a != 2:
        if a == 1:
            x1 = int(input("Введите начальную координату х1 коня: "))
            y1 = int(input("Введите начальную координату y1 коня: "))
            x2 = int(input("Введите начальную координату х2 коня: "))
            y2 = int(input("Введите начальную координату y2 коня: "))
            print(move(x1, y1, x2, y2))
            print("1) ввести данные \n2) выход")
            a = int(input())
        elif a == 2:
            break
        else:
            print("Неправильный ввод")
            print("1) ввести данные \n2) выход")
            a = int(input())


menu()
