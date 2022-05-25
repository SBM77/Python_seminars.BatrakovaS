#Реализовать алгоритм задания случайных чисел.Без использования встроенного генератора псевдослучайных чисел
from datetime import datetime
sumSec = 0

for i in range(0,100000):
    currentMicrosecond = datetime.now().microsecond
    # print(currentMicrosecond)
    sumSec += currentMicrosecond 

# print(sumSec)

rand = sumSec % 10
print(f"Случайное число: {rand}")