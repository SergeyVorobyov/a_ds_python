# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, 
# заданный случайными числами на промежутке [-100; 100). 
# Вывести на экран исходный и отсортированный массивы

import cProfile 
import random

########################################################################################
## Замер времени
## Измененная функция быстрее примерно на 30%
########################################################################################

#array = [12, 9, 3, 10, 15, 11, 7, 13, 14, 0, 2, 4, 1, 6, 8, 5]

def bubble_sort_original(array):
    n = 1
    #print(array)
    while n < len(array):
        for i in range(len(array) - 1):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    
        n += 1
        #print(array)
        


def bubble_sort_new(array):
    n = 1
    j = 1 # элементы в конце уже будут упорядочены
    while n < len(array):
        permutations_count = 0
        for i in range(len(array) - j):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                permutations_count += 1
    
        n += 1
        j += 1
        if permutations_count == 0: #при очередном проходе перестановок элементов не было
            break



def main_original(n):
    """n - размер массива"""
    ARRAY_SIZE = n
    VALUES_LOWER_BOUND = -100
    VALUES_UPPER_BOUND = 100

    input_array = [random.randint(VALUES_LOWER_BOUND, VALUES_UPPER_BOUND) for _ in range (ARRAY_SIZE)]
    
    bubble_sort_original(input_array)
    
# cProfile.run('main_original(100000)')
# n = 1000 7262 function calls in 0.190 seconds
# n = 10000 72794 function calls in 16.484 seconds
# n = 100000 727381 function calls in 1571.114 seconds

def main_new(n):
    """n - размер массива"""
    ARRAY_SIZE = n
    VALUES_LOWER_BOUND = -100
    VALUES_UPPER_BOUND = 100

    input_array = [random.randint(VALUES_LOWER_BOUND, VALUES_UPPER_BOUND) for _ in range (ARRAY_SIZE)]
    
    bubble_sort_new(input_array)
    
# cProfile.run('main_new(100000)')

# n = 1000 7221 function calls in 0.106 seconds
# n = 10000 72384 function calls in 11.852 seconds
# n = 100000 726244 function calls in 1066.967 seconds

#Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1 1066.723 1066.723 1066.753 1066.753 <ipython-input-21-cce1485258f0>:25(bubble_sort_new)
#        1    0.000    0.000 1066.966 1066.966 <ipython-input-21-cce1485258f0>:57(main_new)
#        1    0.026    0.026    0.213    0.213 <ipython-input-21-cce1485258f0>:63(<listcomp>)
#        1    0.001    0.001 1066.967 1066.967 <string>:1(<module>)
#   100000    0.076    0.000    0.157    0.000 random.py:172(randrange)
#   100000    0.030    0.000    0.187    0.000 random.py:216(randint)
#   100000    0.059    0.000    0.081    0.000 random.py:222(_randbelow)
#        1    0.000    0.000 1066.967 1066.967 {built-in method builtins.exec}
#   198810    0.029    0.000    0.029    0.000 {built-in method builtins.len}
#   100000    0.007    0.000    0.007    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   127428    0.016    0.000    0.016    0.000 {method 'getrandbits' of '_random.Random' objects}

###################################################################################################

def main_new_print(n):
    """n - размер массива"""
    ARRAY_SIZE = n
    VALUES_LOWER_BOUND = -100
    VALUES_UPPER_BOUND = 100

    input_array = [random.randint(VALUES_LOWER_BOUND, VALUES_UPPER_BOUND) for _ in range (ARRAY_SIZE)]
    print(f'Исходный массив: {input_array}')
    bubble_sort_new(input_array)
    print(f'Отсортированный массив: {input_array}')
    
main_new_print(15)