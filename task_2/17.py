#Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

N = int(input('введите число '))
spisok =[]
x=1
for i in range (-N,N+1):
    #print (i, end = ' ')
    spisok.append(i)
print(spisok)

data = open('file.txt', 'r')
#data.writelines(N)
#data.write('3\n')
#data.write('4\n')
#data.write('5\n')
#data.close()

for line in data:
    x= x*int(spisok[int(line)])
print(x)


#Позиции хранятся в файле file.txt в одной строке одно число

n=int(input('Введите N (целое число), значение до которрого будет формироваться список: '))
pos=input(f'Введите, через запятую, позиции элементов которые необходимо перемножить, не более {n*2}: ').split(',')

with open('positions.txt', 'w') as positions:
 for i in pos:
  positions.write(f'{i}\n')

spisok=[]
step = 1
start = -n
stop = n+1
if n < 0:
 step = -1
stop -= 2
for i in range(start, stop, step):
 spisok.append(i)

print(spisok)

multiply=1

with open('positions.txt', 'r') as positions:
 for element in positions:
  multiply*=spisok[int(element.strip())]

print(f'Произведение элементов с введенными позициями равно {multiply}')

