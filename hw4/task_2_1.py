# 2. Написать два алгоритма нахождения i-го по счёту простого числа. 
# Первый - использовать алгоритм решето Эратосфена.

# верхняя граница для решета?
# https://en.wikipedia.org/wiki/Prime-counting_function#Inequalities
# n < i * ln(i * ln (i)) для i >= 6

import math
#import cProfile

def eratosthenes(m):
    if m <= 0: return 0
    if m < 6:
        n = 12  # 2, 3, 5, 7, 11
    else:
        n = math.floor(m*math.log(m*math.log(m))+2)
        
    sieve = [j for j in range(n)]
    sieve[1] = 0
    
    for k in range(2, n):
        if sieve[k] != 0:
            j = k+k
            while(j < n):
                sieve[j] = 0
                j+=k
    res = [i for i in sieve if i != 0]
    #print(res)
    #print(res[m-1])
    return res[m-1]

#cProfile.run('eratosthenes(4000000)')

#######################################################################################
# cProfile
# i = 10
# 9 function calls in 0.000 seconds
# i = 100
# 9 function calls in 0.000 seconds
# i = 10000
# 9 function calls in 0.054 seconds
# i = 100000
# 9 function calls in 0.791 seconds
# i = 1000000
# 9 function calls in 9.912 seconds
# i = 4000000
# 9 function calls in 47.021 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1   38.753   38.753   46.157   46.157 <ipython-input-1-607d419f996c>:11(eratosthenes)
#        1    5.083    5.083    5.083    5.083 <ipython-input-1-607d419f996c>:18(<listcomp>)
#        1    2.321    2.321    2.321    2.321 <ipython-input-1-607d419f996c>:27(<listcomp>)
#        1    0.865    0.865   47.021   47.021 <string>:1(<module>)
#        1    0.000    0.000   47.021   47.021 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method math.floor}
#        2    0.000    0.000    0.000    0.000 {built-in method math.log}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#######################################################################################
# timeit
# i = 10
# 100 loops, best of 3: 35.7 usec per loop
# i = 100
# 100 loops, best of 3: 170 usec per loop
# i = 10000
# 100 loops, best of 3: 43.7 msec per loop
# i = 100000
# 100 loops, best of 3: 766 msec per loop
# i = 1000000
# 100 loops, best of 3: 10.9 sec per loop