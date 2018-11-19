#1. Проанализировать скорость и сложность одного - трёх любых алгоритмов, 
# разработанных в рамках домашнего задания первых трех уроков


# 4. Определить, какое число в массиве встречается чаще всего.

# без словаря

import random
#import cProfile 

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

def main(n):
    """n - размер массива"""
    ARRAY_SIZE = n
    VALUES_LOWER_BOUND = 1
    VALUES_UPPER_BOUND = 10

    input_array = [random.randint(VALUES_LOWER_BOUND, VALUES_UPPER_BOUND) for _ in range (ARRAY_SIZE)]
    #print('Входной массив:')
    #print(input_array)

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

    #print(f'Чаще всего ({array_for_count[max_el_ind]} раз(-а)) встречается число {array_no_repeat[max_el_ind]}')
    return(array_no_repeat[max_el_ind])

#cProfile.run('main(10000000)')


#######################################################################################
# cProfile
# n = 10
# 85 function calls in 0.000 seconds
# n = 100
# 603 function calls in 0.000 seconds
# n = 1000
# 5640 function calls in 0.003 seconds
# n = 10000
# 56097 function calls in 0.037 seconds
# n = 100000
# 559637 function calls in 0.379 seconds
# n = 1000000
# 5599632 function calls in 3.637 seconds
# n = 10000000
# 56003134 function calls in 35.352 seconds

# Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <ipython-input-9-59a47917badb>:13(my_minmax_elem_index)
#        1   11.960   11.960   35.330   35.330 <ipython-input-9-59a47917badb>:30(main)
#        1    2.889    2.889   23.370   23.370 <ipython-input-9-59a47917badb>:36(<listcomp>)
#        1    0.021    0.021   35.352   35.352 <string>:1(<module>)
# 10000000    7.892    0.000   17.205    0.000 random.py:172(randrange)
# 10000000    3.277    0.000   20.482    0.000 random.py:216(randint)
# 10000000    6.546    0.000    9.313    0.000 random.py:222(_randbelow)
#        1    0.000    0.000   35.352   35.352 {built-in method builtins.exec}
#       13    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       20    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# 10000000    0.684    0.000    0.684    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 16003095    2.083    0.000    2.083    0.000 {method 'getrandbits' of '_random.Random' objects}

#######################################################################################
# timeit
# n = 10
# 100 loops, best of 3: 27 usec per loop
# n = 100
# 100 loops, best of 3: 238 usec per loop
# n = 1000
# 100 loops, best of 3: 2.46 msec per loop
# n = 10000    
# 100 loops, best of 3: 25.6 msec per loop
# n = 100000
# 100 loops, best of 3: 266 msec per loop