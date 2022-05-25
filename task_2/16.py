#Задать список из n чисел последовательности (1+1/n)n и вывести на экран их сумму
#n=int(input("enter n:  "))
#list = [n for n in range(1,5) if int(1+1/n)^n]  #проще
#print(list)

n=int(input("enter n:  "))
li = [n for n in range(1,n+1)]
li = list(map(lambda n:((n+1/n)**n), li))
print(li) 
print(sum(li), end=' ')