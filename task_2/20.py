#Определить, присутствует ли в заданном списке строк, некоторое число # сделать список строк

from itertools import count


stringList = ["qwe", "asd2", "zx2c1", "q33we6", "ertqwe"]
print(f"Имеем список {stringList}")
N = str(input(f"Введите число для поиска \n"))

for i in range(len(stringList)):
        count = stringList[i].find(N)
        print(count)
        if count !=1:
            print(f"Символы найдено в элементе номер {i+1} ")
        #    findSuccess = 1
    #if findSuccess != 1:
        #print(f"Число не найдено")
             
#findNumber(N,stringList)