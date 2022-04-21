#Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
from re import X


x = int(input("Enter number  "))
y = int(input("Enter number  "))
z = int(input("Enter number  "))
if not(x or y or z) == (not x)  and (not y) and (not z):
    print(True)
else:
    print(False)