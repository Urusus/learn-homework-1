"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""
def hello_user():
  print('Hello User!')

  stuff = input('Как дела?')

  while stuff != 'Хорошо':
    stuff = input('Понятно, но все же, как дела? ')

hello_user()