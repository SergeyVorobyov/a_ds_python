# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
# заданный случайными числами на промежутке [0; 50). 
# Выведите на экран исходный и отсортированный массивы.

import random

# Решение через рекурсию

def my_merge(left_array, right_array):
    """Соединяет два отсортированных массива в один отсортированный"""   
    left_arr_end = len(left_array)
    right_arr_end = len(right_array)
    left_arr_ind, right_arr_ind = 0, 0
    res = list() # требуется доп. память для хранения результата
    res_len = left_arr_end + right_arr_end

    # проходим два отсортированных массива
    for i in range(res_len):
        # если один из массиов уже закончился, то добавляем все оставшиеся элементы из второго
        if left_arr_ind >= left_arr_end:
            res.extend(right_array[right_arr_ind:])
            break
            
        if right_arr_ind >= right_arr_end:
            res.extend(left_array[left_arr_ind:])
            break           
        
        if left_array[left_arr_ind] < right_array[right_arr_ind]:
            res.append(left_array[left_arr_ind])
            left_arr_ind+=1
        else:
            res.append(right_array[right_arr_ind])
            right_arr_ind+=1                  
    return res


def my_merge_sort(array):
    """Рекурсивная функция сортировки слиянием"""
    assert len(array) >= 1, 'Для сортировки ожидается не пустой массив'
    
    if len(array) == 1: # массивы из одного элемента сортировать не нужно, окончание рекурсии
        return array
    
    middle = len(array)//2 # разделяй и властвуй
    return my_merge(my_merge_sort(array[:middle]), my_merge_sort(array[middle:])) # слияние двух отсортированных массивов
                    
ARRAY_SIZE = 10
ARRAY_LOWER_BOUND = 0
ARRAY_UPPER_BOUND = 50 # не включается, но зависит от округления float

if ARRAY_LOWER_BOUND > ARRAY_UPPER_BOUND: 
    ARRAY_LOWER_BOUND, ARRAY_UPPER_BOUND = ARRAY_UPPER_BOUND, ARRAY_LOWER_BOUND

my_array = [ARRAY_LOWER_BOUND + (ARRAY_UPPER_BOUND - ARRAY_LOWER_BOUND)*random.random() for _ in range(ARRAY_SIZE)]

print(f'Исходный массив: {my_array}\n')

print(f'Отсортированный массив: {my_merge_sort(my_array)}')