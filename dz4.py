# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


k = int(input('введите натуральную степень '))

array = list()
for i in range(k,0,-1):
    x = randint(-100,100)
    if x > 0 and i != k:
        array.append(f'+{x}*x^{i}')
    else:
        array.append(f'+{x}*x^{i}')
    x = randint(-100,100)
if x > 0 and i != k:
    array.append(f'+{x}')
else:
    array.append(f'{x}')
array.append(' = 0')
print(''.join(array))