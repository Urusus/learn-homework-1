"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""


phones = [
  {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]

total_sales = 0
total_sales_avg = 0

for sales_per_model in phones:

  model_sales = sum(sales_per_model["items_sold"])
  print(f'Общее количество продаж {sales_per_model["product"]}: {model_sales}')

  avg_model_sales = sum(sales_per_model['items_sold']) / len(sales_per_model['items_sold'])
  print(f'Среднее количестыо продаж {sales_per_model["product"]}: {avg_model_sales}')
  
  total_sales += model_sales
  total_sales_avg += avg_model_sales / len(phones)

print()
print(f'Общее количество продаж: {total_sales}')

print(f'Общее среднее количество продаж: {total_sales_avg}')