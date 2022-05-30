#Найти сумму чисел списка стоящих на нечетной позиции


import random


N = int(input('введите число '))
spisok =[]

for i in range(N):
    spisok.append(random.randint(1,10))
print(f"Создан новый список: \n {spisok}")
sum = 0
for i in range(N):
    if i % 2 > 0: sum += spisok[i]
print(f"Сумма чисел списка стоящих в нечетных позициях = {sum}")



#второй способ
#n = randint(7, 13)
#list = [randint(1, 21) for i in range(n)]
#print(list, '\n')

#print('Сумма элементов на нечетных позициях равна ', sum(list[1::2]), '\n')