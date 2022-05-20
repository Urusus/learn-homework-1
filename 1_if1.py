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

def what_to_do(user_age):
  if user_age != int:
    raise ValueError('Принимается только ввод цифр')
  user_age = int(user_age)
  if user_age <= 6:
    return 'Идите учиться в детский сад'
  elif user_age <= 16:
    return 'Идите учиться в школу'
  elif user_age <= 22:
    return 'Идите учиться в ВУЗ'
  elif user_age <= 59:
    return 'Идите работать'
  else:
    return 'Пора на пенсию'
  
user_age = input('Сколько Вам полных лет? ')

reply = what_to_do(user_age)

print(reply)