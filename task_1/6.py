#Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

a = int(input("Введите число дня недели  "))
if 1==a:
    print("Monday") 
if 2==a:
    print("Thuesday")  
if 3==a:
    print("Wednesday")
if 4==a:
    print("Thusday")
if 5==a:
    print("Friday")
if 6==a:
    print("Saturday")
if 7==a:
    print("Sunday")
if a>7 or a<1:
    print("Увы,под таким числом,нет дня недели")