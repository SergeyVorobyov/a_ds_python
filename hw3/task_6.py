# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
# Сами минимальный и максимальный элементы в сумму не включать.

import random

#######################################################
def my_minmax_elem_index(arr):
    """
    Индекс максимального и минимального элементов перебором
    """
    
    min_el_index = 0
    max_el_index = 0

    for i in range(len(arr)):
        if arr[i] < arr[min_el_index]:
            min_el_index = i
        if arr[i] > arr[max_el_index]:
            max_el_index = i
            
    return min_el_index, max_el_index
##########################################################

ARRAY_SIZE = 10
VALUES_LOWER_BOUND = 1
VALUES_UPPER_BOUND = 10

input_array = [random.randint(VALUES_LOWER_BOUND, VALUES_UPPER_BOUND) for _ in range (ARRAY_SIZE)]
print('Входной массив:')
print(input_array)

min_ind, max_ind = my_minmax_elem_index(input_array)

print(f'Первый минимальный элемент {input_array[min_ind]} с индексом {min_ind}')
print(f'Первый максимальный элемент {input_array[max_ind]} с индексом {max_ind}')

if min_ind > max_ind:
    min_ind, max_ind = max_ind, min_ind

sum_of_values = 0
    
for i in range(min_ind, max_ind+1):
    sum_of_values+=input_array[i]

if(len(input_array)) == 1: 
    print(f'Сумма элементов между ними равна 0')
else:
    print(f'Сумма элементов между ними равна: {sum_of_values-input_array[min_ind]-input_array[max_ind]}')