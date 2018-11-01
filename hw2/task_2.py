#2. Посчитать четные и нечетные цифры введенного натурального числа. 
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def digit_summ(v, n, e, ne):
    if v == 0:
        return e, ne
    
    r = v % 10**n
    d = r / 10**(n-1)
    v -= r
    n += 1
    if (d%2) == 0:
        e += 1
    else:
        ne += 1
    return digit_summ(v,n,e,ne)

s = input('Введите натуральное число: ')
if s.isdigit() == False:
    print('Ошибка ввода числа')
else:
    s_int = int(s)
    if s_int == 0:
        print('Ошибка ввода числа')
    else:
        a,b = digit_summ(s_int, 1, 0, 0)
        print(f'Четных цифр: {a}, нечетных цифр: {b}')
