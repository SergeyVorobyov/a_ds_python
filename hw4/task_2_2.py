# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Второй - без использования "решета". 
# Проанализировать скорость и сложность алгоритмов.
import math
#import cProfile

def is_prime(n):
    """Проверка, является ли число простым - перебор делителей из wiki
    """
    if n <= 1: return False
    i = 2
    j = 0
    while (i*i <= n and j != 1):
        if n % i == 0:
            j = 1
        i+= 1
    if j == 1:
        return False
    else:
        return True

def main(m):
    
    prime_count = 0 #счетчик простых чисел
    
    if m <= 0: return 0
    if m < 6:
        n = 12  # 2, 3, 5, 7, 11
    else:
        n = math.floor(m*math.log(m*math.log(m))+2)    # верхняя граница m-го простого числа
    i = 0    
    while (prime_count < m):
        if is_prime(i):
            prime_count+=1
        i+=1  
    return(i-1)

#cProfile.run('main(1000000)')

#######################################################################################
# cProfile
# i = 10
# 37 function calls in 0.000 seconds
# i = 100
# 549 function calls in 0.001 seconds
# i = 1000
# 7927 function calls in 0.018 seconds
# i = 10000
# 104737 function calls in 0.502 seconds
# i = 100000
# 1299717 function calls in 16.456 seconds
# i = 1000000
# 15485871 function calls in 547.142 seconds

# 
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    3.276    3.276  547.142  547.142 <ipython-input-62-55b58ed15667>:21(main)
# 15485864  543.866    0.000  543.866    0.000 <ipython-input-62-55b58ed15667>:6(is_prime)
#        1    0.000    0.000  547.142  547.142 <string>:1(<module>)
#        1    0.000    0.000  547.142  547.142 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method math.floor}
#        2    0.000    0.000    0.000    0.000 {built-in method math.log}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



#######################################################################################
# timeit
# i = 10
# 100 loops, best of 3: 14.8 usec per loop
# i = 100
# 100 loops, best of 3: 459 usec per loop
# i = 1000
# 100 loops, best of 3: 14 msec per loop
# i = 10000
# 100 loops, best of 3: 438 msec per loop