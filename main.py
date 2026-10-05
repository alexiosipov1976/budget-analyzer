import json

def load_items(filename):
    """Загружает товары из JSON-файла."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def calculate_total(items):
    """Считает общую сумму бюджета."""
    return sum(item["price"] for item in items)

def add_shares(items, total):
    """Добавляет долю в процентах к каждому товару."""
    for item in items:
        item["share"] = (item["price"] / total) * 100
    return items

def sort_by_price_desc(items):
    """Сортирует товары по убыванию цены."""
    return sorted(items, key=lambda x: x["price"], reverse=True)

def print_report(items, total):
    """Выводит красивый отчёт в консоль."""
    print(f"Всего позиций: {len(items)}, общий бюджет: {total:.0f} руб.\n")
    print("--- Вклад каждого товара в бюджет (от дорогого к дешёвому) ---")

    # Находим максимальную длину названия, чтобы колонки стояли ровно
    max_name_len = max(len(item["name"]) for item in items) if items else 20

    for item in items:
        # {:<max_name_len} — название прижато влево и занимает ровно max_name_len символов
        print(
            f"{item['name']:<{max_name_len}} "
            f"{item['price']:7.0f} руб. — {item['share']:5.1f}%"
        )

def main():
    filename = "items.json"
    items = load_items(filename)
    total = calculate_total(items)
    items_with_shares = add_shares(items, total)
    sorted_items = sort_by_price_desc(items_with_shares)
    print_report(sorted_items, total)

if __name__ == "__main__":
    main()
