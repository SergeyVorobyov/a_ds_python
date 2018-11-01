#3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
# Например, если введено число 3486, то надо вывести число 6843

def digit_mirror(v, n):
    if v == 0:
        return v, 0
    
    r = v % 10**n
    d = r / 10**(n-1) 
    v -= r
    n += 1
    a, b = digit_mirror(v,n)
    return a+d*10**b, b+1

s = input('Введите целое положительное число (нули в записи слева не учитываются): ')
if s.isdigit() == False:
    print('Ошибка ввода числа')
else:
    s_int = int(s)
    if s_int == 0:
        print('Результат: 0')
    else:
        res, _ = digit_mirror(s_int, 1)
        print(f'Результат: {int(res)}')
