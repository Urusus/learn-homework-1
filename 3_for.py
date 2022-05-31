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

Iphone_total_sales = sum(phones[0]["items_sold"])
Xiaomi_total_sales = sum(phones[1]["items_sold"])
Samsung_total_sales = sum(phones[2]["items_sold"])

Iphone_average_sales = sum(phones[0]["items_sold"]) / len(phones[0]["items_sold"])
Xiaomi_average_sales = sum(phones[1]["items_sold"]) / len(phones[1]["items_sold"])
Samsung_average_sales = sum(phones[2]["items_sold"]) / len(phones[2]["items_sold"])

all_model_sales = phones[0]["items_sold"] + phones[1]["items_sold"] + phones[2]["items_sold"]

print("Общее количество продаж", phones[0]["product"], "-", Iphone_total_sales)
print("Общее количество продаж", phones[1]["product"], "-", Xiaomi_total_sales)
print("Общее количество продаж", phones[2]["product"], "-", Samsung_total_sales)
print()
print("Среднее количество продаж", phones[0]["product"], "-", Iphone_average_sales)
print("Среднее количество продаж", phones[1]["product"], "-", Xiaomi_average_sales)
print("Среднее количество продаж", phones[2]["product"], "-", Samsung_average_sales)
print()
print("Cуммарное количество продаж всех товаров", "-", sum(all_model_sales))
print("Среднее количество продаж всех товаров", "-", sum(all_model_sales) / len(all_model_sales))