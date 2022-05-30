# 25. Написать программу преобразования десятичного числа в двоичное
from random import randint


n = randint(1, 101)
print('Задано число: ', n, '\n')

print('Двоичный вид: ', "{0:b}".format(n), '\n')
print(bin(n))