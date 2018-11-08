# 2. Во втором массиве сохранить индексы четных элементов первого массива. 
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить
# значениями 0, 3, 4, 5 , т.к. именно в этих позициях первого массива стоят четные числа.

import random

ARRAY_SIZE = 10
VALUES_LOWER_BOUND = 1
VALUES_UPPER_BOUND = 10

input_array = [random.randint(VALUES_LOWER_BOUND, VALUES_UPPER_BOUND) for _ in range (ARRAY_SIZE)]
print('Входной массив:')
print(input_array)

output_array = [j for j in range(len(input_array)) if input_array[j]%2 == 0]

print('Массив индексов четных элементов:')
print(output_array)