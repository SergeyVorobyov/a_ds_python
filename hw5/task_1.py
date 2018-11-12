# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала 
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) 
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, 
# чья прибыль ниже среднего.

import collections

Company = collections.namedtuple('Company', ['Name', 'revenue_q1', 'revenue_q2', 'revenue_q3', 'revenue_q4', 'year_revenue'])

company_list = list()
error_flag = 0
while(True):
    comp_num_str = input('Введите число предприятий (для выхода введите 0 (ноль):')
    try:
        comp_num_int = int(comp_num_str)
    except:
        print('Ошибка ввода данных')
        error_flag = 1
        break
    if comp_num_int == 0:
        break
    for i in range(comp_num_int):
        comp_name = ''
        rev_q1 = 0
        rev_q2 = 0
        rev_q3 = 0
        rev_q4 = 0
        comp_name = input(f'Введите название предприятия № {i+1}:')
        try:
            rev_q1 = float(input(f'Введите прибыль предприятия {comp_name} за 1 квартал:'))
            rev_q2 = float(input(f'Введите прибыль предприятия {comp_name} за 2 квартал:'))
            rev_q3 = float(input(f'Введите прибыль предприятия {comp_name} за 3 квартал:'))
            rev_q4 = float(input(f'Введите прибыль предприятия {comp_name} за 4 квартал:'))
        except:
            print(f'Ошибка ввода данных по предприятию {comp_name}')
            error_flag = 1
            break
        comp = Company(comp_name, rev_q1, rev_q2, rev_q3, rev_q4, rev_q1+rev_q2+rev_q3+rev_q4)
        company_list.append(comp)
    if error_flag == 1:
        break
    #print(company_list)
    rev_summ = 0
    for i in range(len(company_list)):
        #суммируем прибыль всех компаний
        rev_summ += company_list[i][5]
    avg_rev = rev_summ/float(comp_num_int) #средняя прибыль
    print(f'Средняя годовая прибыль по всем компаниям {avg_rev}')
    below_avg = [comp[0] for comp in company_list if comp[5] < avg_rev] # прибыль ниже средней
    above_avg = [comp[0] for comp in company_list if comp[5] > avg_rev] # прибыль выше средней
    if len(below_avg) >0:
        print('Компании с прибылью ниже средней:')
        for comp in below_avg:
            print('\t'+comp[0])
    else:
        print('Нет компаний с прибылью ниже средней') 
    if len(above_avg) >0:
        print('Компании с прибылью выше средней:')
        for comp in above_avg:
            print('\t'+comp[0])
    else:
        print('Нет компаний с прибылью выше средней')            
