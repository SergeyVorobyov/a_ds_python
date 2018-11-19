# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. 
# Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: 
# в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.

import random

# для проверки
def bubble_sort_from_lection(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        n += 1

def median_search(array, median_index):
    """Поиск медианы в массиве без сортировки"""
    
    if len(array) == 1:
        return array[0]
    # выбираем элемент по середине и разбиваем массив на 3
    mid= len(array)//2
    lower = list()
    middle = list()
    upper = list()
    for el in array:
        if el < array[mid]:
            lower.append(el)
        elif el > array[mid]:
            upper.append(el)
        else:
            middle.append(el)

    if len(lower)//(median_index)>0:
        return median_search(lower, median_index)
    elif (len(lower)+len(middle))//median_index>0:
        return median_search(middle[:1], median_index-len(lower))
    elif (len(lower)+len(middle)+len(upper))//median_index:
        return median_search(upper, median_index-len(lower)-len(middle))  
         
        
SIZE_M = 5
ARRAY_LOWER_BOUND = 1
ARRAY_UPPER_BOUND = 100
my_array = [random.randint(ARRAY_LOWER_BOUND, ARRAY_UPPER_BOUND) for _ in range(2*SIZE_M+1)]
#my_array = [61, 61, 61, 83, 57, 5, 57, 57, 70, 100, 97]
print(f'Массив: {my_array}')
print(f'Медиана: {median_search(my_array, len(my_array)//2+1)}')
#проверка сортировкой
bubble_sort_from_lection(my_array)
print(f'Отсортированный массив для проверки: {my_array}')
print(f'Медиана для проверки: {my_array[len(my_array)//2]}')