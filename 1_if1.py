"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

from curses import use_default_colors


def what_to_do(user_age):
  user_age = int(user_age)
  if user_age <= 6:
    reply = 'Идите учиться в детский сад',
  else: 
    if user_age <= 16:
      reply = 'Идите учиться в школу',
    else:
      if user_age <= 22:
        reply = 'Идите учиться в ВУЗ'
      else:
        reply = 'Идите работать'
  print(reply)

what_to_do(user_age = input('Сколько Вам полных лет? '))