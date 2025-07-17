def total_revenue(purchases):
    return sum(p.get('price', 0) * p.get('quantity', 0) for p in purchases)

def items_by_category(purchases):
    result = {}
    for p in purchases:
        category = p.get('category')
        item = p.get('item')
        result.setdefault(category, []).append(item)
    return result

def expensive_purchases(purchases, min_price):
    result = []
    for p in purchases:
        if p.get('price', 0) > min_price:
            result.append(p)
    return result

def average_price_by_category(purchases):
    def average(numbers):
        return sum(numbers) / len(numbers)
    result = {}
    for p in purchases:
        category = p.get('category')
        price = p.get('price')
        result.setdefault(category, []).append(price)
    for k, v in result.items():
        result[k] = average(v)
    return result

def most_frequent_category(purchases):
    result = {}
    for p in purchases:
        category = p.get('category')
        quantity = p.get('quantity', 0)
        result.setdefault(category, []).append(quantity)
    for k, v in result.items():
        result[k] = sum(v)
    return max(result, key=lambda x: result.get(x))