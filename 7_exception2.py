"""

Домашнее задание №1

Исключения: приведение типов
* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discount):
  try:   
    price_with_discount = float(price) - float(price) * float(discount) / int(max_discount)
    return price_with_discount

  except ValueError:
    print('Value Error found - stop program')
  except TypeError:
    print('Type Error found - stop program')
    
print(discounted(100, 2, 20))
print(discounted(100, "Five", 20))
print(discounted("100", "4.5", "20"))
print(discounted(100, 10, "twenty"))