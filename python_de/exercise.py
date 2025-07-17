import my_module as m

# set variables: purchase: list, min_price: float 
purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

min_price = 1.0

# 
print(f'Общая выручка: {m.total_revenue(purchases)}\n'
      f'Товары по категориям: {m.items_by_category(purchases)}\n'
      f'Покупки дороже {min_price}: {m.expensive_purchases(purchases, min_price)}\n'
      f'Средняя цена по категориям: {m.average_price_by_category(purchases)}\n'
      f'Категория с наибольшим количеством проданных товаров: {m.most_frequent_category(purchases)}')
