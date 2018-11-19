# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных 
# программах в рамках первых трех уроков. Проанализировать результат и определить 
# программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
# P.S. Напишите в комментариях версию Python и разрядность ОС.

import sys

mem_usage_dict = dict()

def show_size(mem_usage_dict, x):
    """
    Переделанная функция из лекции
    Для каждого переданного объекта x его id и размер записывается в словарь
    Затем по id обновляется максимальный объем памяти
    """
    mem_volume = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                mem_volume += sys.getsizeof(key)
                mem_volume += sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                mem_volume += sys.getsizeof(item)
    mem_in_dict = mem_usage_dict.get(id(x), None)
    
    if mem_in_dict == None:
        mem_usage_dict[id(x)] = mem_volume
    elif mem_in_dict < mem_volume:
        mem_usage_dict[id(x)] = mem_volume                   

############################################################################################################

# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно. 
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

code_start = 32
show_size(mem_usage_dict, code_start)
code_end = 127
show_size(mem_usage_dict, code_end)
i = code_start
show_size(mem_usage_dict, i)

while(i<=code_end):
    show_size(mem_usage_dict, i)
    j = 0
    show_size(mem_usage_dict, j)
    s=''
    show_size(mem_usage_dict, s)
    while(i+j<=code_end and j<10):
        show_size(mem_usage_dict, i)
        show_size(mem_usage_dict, j)
        s+=str(i+j)
        show_size(mem_usage_dict, s)
        s+=' - \''
        show_size(mem_usage_dict, s)
        s+=chr(i+j)
        show_size(mem_usage_dict, s)
        s+='\' ; '
        show_size(mem_usage_dict, s)
        j+=1
        show_size(mem_usage_dict, j)
    print(s)
    i = i + j
    show_size(mem_usage_dict, i)
##################################################################        


itog = 0
for v in mem_usage_dict.values():
    itog += v
print(f'Оценка использования памяти под переменные: {itog} байт(-а)')


# Python 3.6.2 ОС 64 bit
# Оценка использования памяти под переменные: 5574 байт(-а)
# Данная программа использует больше всего памяти без учета сборщика мусора из-за накопления строк в цикле