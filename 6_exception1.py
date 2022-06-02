"""

Домашнее задание №1

Исключения: KeyboardInterrupt
* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
"""

def hello_user():
  print('Hello User!')
  how_do_you_do = input('Как дела?')

  while True:
    try:
      how_do_you_do = input('Понятно, но все же, как дела? ')
      if how_do_you_do == 'Хорошо':
        break
    except KeyboardInterrupt:
      print()
      print('Пока!')
      break

hello_user()