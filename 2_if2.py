"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

from ast import And
from cgi import test

def check_strings(str1, str2):
  if type(str1) != str or type(str2) != str: 
    return 0
  elif str1 == str2:
    return 1
  elif str1 != str2 and len(str1) > len(str2):
    return 2
  elif str2 == 'learn':
    return 3
  
print(check_strings('test', 1))

print(check_strings('test', 'test'))

print(check_strings('test1', 'test'))

print(check_strings('test1', 'learn'))