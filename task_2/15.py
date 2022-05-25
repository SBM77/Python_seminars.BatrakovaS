#Написать программу получающую набор произведений чисел от 1 до N.
#Пример: пусть N = 4, тогда
#[ 1, 2, 6, 24 ]

n = int(input('Введите n:'))
list=[]
list=[1]
for i in range (n):
    
    list.append()
print(list)


#print(f'набор произведений чисел от 1 до N: = ',  )

string_number = str(float(input('Enter a real number: '))).replace('.', '')
list_number = [int(a) for a in string_number]
print(f'Sum of all digits in the real number is {sum(list_number)}.')


# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]
import os
import random
os.system("cls")

n = random.randint(6, 16)
print(n)

list = [1]

for i in range(2, n+1):
 list.append(i * list[i-2])

print(list, '\n')

def multy(a):
 if a == 1:
  return 1

 return a * multy(a-1)

n = 10

print("Sequence for ")
for i in range(1, n+1):
 print(multy(i), end=' ')