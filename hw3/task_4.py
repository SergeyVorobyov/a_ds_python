# 4. Определить, какое число в массиве встречается чаще всего.

# без словаря очень долго

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

array_no_repeat = list() # массив элементов без повторов
array_for_count = list() # массив для учета числа вхождений

# оставляем уникальные элементы
for i in range(len(input_array)):
    if input_array[i] in array_no_repeat: 
        continue
    else:
        array_no_repeat.append(input_array[i]) 

# считаем число вхождений уникальных элементов
for j in range(len(array_no_repeat)):
    count = 0
    for k in range(len(input_array)):
        if input_array[k] == array_no_repeat[j]:
            count+=1
    array_for_count.append(count)

# чаще всего (индекс)
_ , max_el_ind = my_minmax_elem_index(array_for_count)

print(f'Чаще всего ({array_for_count[max_el_ind]} раз(-а)) встречается число {array_no_repeat[max_el_ind]}')