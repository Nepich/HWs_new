def calc(first_number, second_number, operation):
    if operation in '+ - * /':
        if operation == '-':
            return first_number - second_number
        elif operation == '+':
            return first_number + second_number
        elif operation == '*':
            return first_number * second_number
        else:
            return first_number / second_number
    else:
        return 'Вы ввели неверную операцию'


frst, scnd, oper = int(input('Введите первое число: ')), \
                   int(input('Введите второе число: ')), \
                   input('Введите вид операции(+ - / *): ')

print(calc(frst, scnd, oper))