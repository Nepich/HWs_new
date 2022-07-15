db_dict = {}


def db(name, price, count):
    if name not in db_dict:
        db_dict[name] = {"price": price,
                         "count": count}
    else:
        db_dict[name] = {"price": price,
                         "count": count}


def menu():
    print("1) ввести данные\n2) вывести все введенные ранее данные\n3) выход")
    choice = int(input())
    while choice != 3:
        if choice == 1:
            name = input("введите наименование товара: ")
            price = input("введите цену товара: ")
            count = input("введите количество товара: ")
            db(name, price, count)
            print("1) ввести данные\n2) вывести все введенные ранее данные\n3) выход")
            choice = int(input())
        elif choice == 2:
            print(db_dict)
            print("1) ввести данные\n2) вывести все введенные ранее данные\n3) выход")
            choice = int(input())
        elif choice == 3:
            break
        else:
            print('Попробуйте ввести еще раз')
            print("1) ввести данные\n2) вывести все введенные ранее данные\n3) выход")
            choice = int(input())


menu()



