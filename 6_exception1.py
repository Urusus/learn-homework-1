"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def while_fnct(stuff):

  print('Hello User!')
  stuff = input('Как дела?')

  while True:
    
    try:
      stuff = input('Понятно, но все же, как дела? ')
      if stuff == 'Хорошо':
        break

    except KeyboardInterrupt:
      print(' Уже уходишь? Ну тогда пока!')
      break

while_fnct('Я же могу сюда лююой аргумент положить, чтобы запустить функцию, правда?')