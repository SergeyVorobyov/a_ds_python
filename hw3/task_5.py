#5. В массиве найти максимальный отрицательный элемент. 
# Вывести на экран его значение и позицию в массиве.
import random

ARRAY_SIZE = 10
VALUES_LOWER_BOUND = -10
VALUES_UPPER_BOUND = 10

input_array = [random.randint(VALUES_LOWER_BOUND, VALUES_UPPER_BOUND) for _ in range (ARRAY_SIZE)]
print('Входной массив:')
print(input_array)

min_subzero_index = 0
found_flag = 0

for i in range(len(input_array)):
    if input_array[i] < 0:
        found_flag = 1
        min_subzero_index = i

if (found_flag == 0):
    print('В массиве нет отрицатльных чисел')
else:
    for j in range(min_subzero_index, len(input_array)):
        if input_array[j] < 0 and input_array[j] > input_array[min_subzero_index]:
            min_subzero_index = j
    print(f'Максимальный отрицательный элемент в позиции {min_subzero_index} со значением {input_array[min_subzero_index]}')
