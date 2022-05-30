# 32.	Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


spisok = [5,8,8,96,1,2,85,96] 
elements = [] 
for i in range (0, len(spisok)):     
   duplicate = 0     
   for j in range(0, len(spisok)):         
    if i != j:             
     if spisok[i] == spisok[j]:                 
      duplicate = 1     
   if duplicate == 0:       
     elements.append(spisok[i]) 
print(elements)