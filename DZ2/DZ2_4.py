# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 1 до 100, можно создать свой генератор случайных чисел или использовать готовый) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0

import random

k = 9
file_name = 'res_dz2_4.txt'
with open(file_name, 'w') as data:
    for i in range(k, 0, -1):
        x = random.randint(1,100)
        if i > 1:
            data.write(f'{x}*x**{i} + ')
        else:
            data.write(f'{x}*x + {random.randint(1,100)} = 0')