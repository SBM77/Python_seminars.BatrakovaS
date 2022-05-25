#Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
#str1 = "я учу "
#str2 = "я"
#print("Количество вхождения одной строки в другую: ", str1.count(str2),'\n')

str1 = input("Введите первую строку для проверки:")
str2 = input("Введите вторую строку для поиска в первой строке:")

# первый способ
print(f"Вторая строка входит в первую {str1.count(str2)} раз(а).")

# второй способ
count = 0
for i in range(len(str1) - len(str2)):
 if str2 in str1[i:i+len(str2)]:
  count += 1
print(f"Вторая строка входит в первуюф {count} раз(а).")

def text_find(a,b):
 count = 0
i = 0
while i <= len(a):
 if b in a[i: i+len(b)]:
#print("Найдено повторение номер", count+1)
  count += 1
 i += len(b)
else:
 i += 1
  return count

a = "a тесты тесты тессс тесты"
b = "тесты"

print(f"Count of first word in second phrase: {text_find(a,b)}")
print(f"Count of first word in second phrase: {text_find('аааааааааа','аа')}")

# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

# str1= input('First string: ')
# str2= input('Second string: ')

str1 = 'Python free 777 $$$ python free python python python $$$ python'
str2 = 'python free new $$$'

str_list = str1.lower().split()
substr_list = str2.lower().split()

# print('String: ' + str1)
# print('Substrings: ' + str2)
# print()
#
# for i in substr_list:
# count = 0
# for j in str_list:
# count = str_list.count(i)
# print(f'{i} found {count} times.')