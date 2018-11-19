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
# 7. В одномерном массиве целых чисел определить два наименьших элемента. 
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

ARRAY_SIZE = 10
show_size(mem_usage_dict,ARRAY_SIZE)
VALUES_LOWER_BOUND = 1
show_size(mem_usage_dict, VALUES_LOWER_BOUND)
VALUES_UPPER_BOUND = 10
show_size(mem_usage_dict, VALUES_UPPER_BOUND)

input_array = [random.randint(VALUES_LOWER_BOUND, VALUES_UPPER_BOUND) for _ in range (ARRAY_SIZE)]
show_size(mem_usage_dict, input_array)
print('Входной массив:')
print(input_array)

min_index_1 = 0
show_size(mem_usage_dict, min_index_1)
min_index_2 = 0
show_size(mem_usage_dict, min_index_2)

for i in range(len(input_array)):
    if input_array[i] < input_array[min_index_1]:
        min_index_1 = i
        show_size(mem_usage_dict, min_index_1)
        
for i in range(len(input_array)):
    if input_array[i] < input_array[min_index_2] and i != min_index_1:
        min_index_2 = i
        show_size(mem_usage_dict, min_index_2)

print(f'Минимальные элементы {input_array[min_index_1],input_array[min_index_2]}')        
##################################################################        


itog = 0
for v in mem_usage_dict.values():
    itog += v
print(f'Оценка использования памяти под переменные: {itog} байт(-а)')


# Python 3.6.2 ОС 64 bit
#Оценка использования памяти под переменные: 636 байт(-а)