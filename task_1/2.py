#Найти максимальное из пяти чисел
import numbers

numbers = [1,10,5,2,8]
print (numbers)
max = numbers[0]
for i in numbers:
    if i> max:
        max = i 
print ("наибольшее число: ",max, '\n')