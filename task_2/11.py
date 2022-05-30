#Сформировать список из  N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.
#способ 1:
from itertools import count
from re import S


list =[]
N=int(input("Введите количествло членов последовательности  "))
for i in range(N):
    if i%2==0:
        list.append(3**i)
    else:
        list.append(-3**i)
print(list)

#способ 2
def sub(x):
    if x in[0,1]:
        return 1
    else:
        return sub(x-1)*-3
list =[]
S=int(input("Enter S  "))
for N in range(1,S):
    list.append(sub(N))
print(list)

#способ 3

count = int(input("Введите количество элементов  "))
num = 1
list=[1]
for i in range (0,count-1):
    num*=-3
    list.append(num)
print(list)

#способ 4

def power (s):
 new = (-3)**s
 return new
n = 10
spisok =[]
for i in range(n):
    spisok.append(power(i))
print(f"List of elements: {spisok}")

