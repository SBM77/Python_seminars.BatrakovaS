#Реализовать алгоритм перемешивания списка. 

N = int(input('введите число '))
spisok =[]
for i in range(N):
    spisok.append(i)
print(f"List of elements: {spisok}")

data = list(enumerate(spisok))
print(data)

array = [1,2,3,4,5,6,7,8,9,10]
print(f'На входе имеем массив:\n{array}')
for i in range(0,len(array)-1):
 swap=array[i]
rnd=int(i+1,len(array)-1)
array[i]=array[rnd]
array[rnd]=swap
print(f'После перемешивания имеем массив:\n{array}')