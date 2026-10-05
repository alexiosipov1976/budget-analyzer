items = [
    {"id": 1, "name": "Кружка", "price": 490.0, "tags": ["посуда", "подарок"]},
    {"id": 2, "name": "Ноутбук", "price": 75000.0, "tags": ["электроника", "работа"]},
    {"id": 3, "name": "Кроссовки", "price": 9990.0, "tags": ["обувь", "спорт"]},
    {"id": 4, "name": "Рюкзак", "price": 3500.0, "tags": ["аксессуары", "спорт"]},
    {"id": 5, "name": "Термос", "price": 1800.0, "tags": ["посуда", "туризм"]},
    {"id": 6, "name": "Фонарик", "price": 500.0, "tags": ["туризм", "аксессуары"]},
]

def calc_stats(items):
    if not items:
        return {"count": 0, "average_price": 0.0, "min_price": None, "max_price": None}
    prices = [i["price"] for i in items]
    return {
        "count": len(items),
        "average_price": sum(prices) / len(prices),
        "total_price": sum(prices),
        "min_price": min(prices),
        "max_price": max(prices),
    }

def stats_by_tag(items):
    # словарь: тег -> список товаров с этим тегом
    by_tag = {}
    for item in items:
        for tag in item.get("tags", []):
            if tag not in by_tag:
                by_tag[tag] = []
            by_tag[tag].append(item)

    result = {}
    for tag, tagged_items in by_tag.items():
        result[tag] = calc_stats(tagged_items)
    return result

overall = calc_stats(items)
by_tag = stats_by_tag(items)

print("Общая статистика:", overall)
print("По тегам:", by_tag)

# Находим самый дорогой товар автоматически
most_expensive = max(items, key=lambda x: x["price"])
max_price = most_expensive["price"]
max_name = most_expensive["name"]

max_share = (max_price / overall["total_price"]) * 100
print(f"Самый дорогой товар: {max_name} за {max_price:.0f} руб. — это {max_share:.1f}% от общей суммы.")

cheap_total = overall["total_price"] - max_price
cheap_share = (cheap_total / overall["total_price"]) * 100
print(f"На остальные товары ушло {cheap_total:.0f} руб. — это {cheap_share:.1f}% бюджета.")

print("\n--- Вклад каждого товара в бюджет ---")
# Сначала найдём самую длинную длину названия — чтобы под неё сделать ширину столбца
max_name_len = max(len(item["name"]) for item in items)

for item in items:
    share = (item["price"] / overall["total_price"]) * 100
    # {:<max_name_len} — имя займёт ровно max_name_len символов и будет прижато влево
    print(f"{item['name']:<{max_name_len}} {item['price']:7.0f} руб. — {share:5.1f}%")

sorted_items = sorted(items, key=lambda x: x["price"], reverse=True)

print("\n--- Вклад каждого товара в бюджет (от дорогого к дешёвому) ---")
for item in sorted_items:
    share = (item["price"] / overall["total_price"]) * 100
    print(f"{item['name']:20} {item['price']:7.0f} руб. — {share:5.1f}%")

print(f"Всего позиций: {len(items)}, общий бюджет: {overall['total_price']:.0f} руб.\n")
