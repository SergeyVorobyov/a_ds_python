# 7. В одномерном массиве целых чисел определить два наименьших элемента. 
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.


import random

ARRAY_SIZE = 10
VALUES_LOWER_BOUND = 1
VALUES_UPPER_BOUND = 10

input_array = [random.randint(VALUES_LOWER_BOUND, VALUES_UPPER_BOUND) for _ in range (ARRAY_SIZE)]
print('Входной массив:')
print(input_array)

min_index_1 = 0
min_index_2 = 0

for i in range(len(input_array)):
    if input_array[i] < input_array[min_index_1]:
        min_index_1 = i
        
for i in range(len(input_array)):
    if input_array[i] < input_array[min_index_2] and i != min_index_1:
        min_index_2 = i

print(f'Минимальные элементы {input_array[min_index_1],input_array[min_index_2]}') 