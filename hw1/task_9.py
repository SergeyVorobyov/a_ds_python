# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

if a > b:
    if b > c:
        print(f'Среднее {b}')
    else:
        if a > c:
            print(f'Среднее {c}')
        else:
            print(f'Среднее {a}')
else:
    if c > b:
        print(f'Среднее {b}')
    else:
        if  a > c:
            print(f'Среднее {a}')
        else:
            print(f'Среднее {c}')
