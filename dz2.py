# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.



array = []
n = int(input())
i = 2
if n > 0:
    while i * i <= n:
       while n % i == 0:
           array.append(i)
           n = n / i
       i = i + 1
    if n > 1:
       array.append(n)
    print(array)
else:
    print('введено не натуральное число')