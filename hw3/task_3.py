#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# если несколько, то любой с любым

import random

ARRAY_SIZE = 10
VALUES_LOWER_BOUND = 1
VALUES_UPPER_BOUND = 10

input_array = [random.randint(VALUES_LOWER_BOUND, VALUES_UPPER_BOUND) for _ in range (ARRAY_SIZE)]
print('Входной массив:')
print(input_array)

min_el_index = 0
max_el_index = 0

for i in range(len(input_array)):
    if input_array[i] < input_array[min_el_index]:
        min_el_index = i
    if input_array[i] > input_array[max_el_index]:
        max_el_index = i

print(f'Минимальный элемент {input_array[min_el_index]} с индексом {min_el_index}')
print(f'Максимальный элемент {input_array[max_el_index]} с индексом {max_el_index}')

temp_buffer = input_array[min_el_index]
input_array[min_el_index] = input_array[max_el_index]
input_array[max_el_index] = temp_buffer


print('Измененный массив:')
print(input_array)