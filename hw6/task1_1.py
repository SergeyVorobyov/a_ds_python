# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных 
# программах в рамках первых трех уроков. Проанализировать результат и определить 
# программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
# P.S. Напишите в комментариях версию Python и разрядность ОС.

import sys

mem_usage_dict = dict()

def show_size(mem_usage_dict, x):
    """
    Переделанная функция из лекции
    Для каждого переданного объекта x его id и размер записывается в словарь
    Затем по id обновляется максимальный объем памяти
    """
    mem_volume = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                mem_volume += sys.getsizeof(key)
                mem_volume += sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                mem_volume += sys.getsizeof(item)
    mem_in_dict = mem_usage_dict.get(id(x), None)
    
    if mem_in_dict == None:
        mem_usage_dict[id(x)] = mem_volume
    elif mem_in_dict < mem_volume:
        mem_usage_dict[id(x)] = mem_volume                   

############################################################################################################
# 3. По введенным пользователем координатам двух точек вывести уравнение прямой, проходящей через эти точки

x1 = float(input('Введите x1: '))
show_size(mem_usage_dict, x1)
y1 = float(input('Введите y1: '))
show_size(mem_usage_dict, y1)
x2 = float(input('Введите x2: '))
show_size(mem_usage_dict, x2)
y2 = float(input('Введите y2: '))
show_size(mem_usage_dict, y2)

if (x1 == x2) and (y1 == y2):
    print(f'Это точка ({x1}, {y1})')
else:
    if x1 == x2:
        print(f'Уравнение x = {x1}')
    else:
        if y1 == y2:
            print(f'Уравнение y = {y1}')
        else:
            k = (y2 - y1)/(x2-x1)
            show_size(mem_usage_dict, k)
            b = y2 - k*x2
            show_size(mem_usage_dict, b)
            print(f'Уравнение y = {k}*x + {b}')        
##################################################################        


itog = 0
for v in mem_usage_dict.values():
    itog += v
print(f'Оценка использования памяти под переменные: {itog} байт(-а)')

# Python 3.6.2 ОС 64 bit
# Оценка использования памяти под переменные: 144 байт(-а)
