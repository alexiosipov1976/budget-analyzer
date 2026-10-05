from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float
    tags: Optional[List[str]] = None

items_db: List[Item] = [
    Item(id=1, name="Кружка", price=490.0, tags=["посуда", "подарок"]),
    Item(id=2, name="Ноутбук", price=75000.0, tags=["электроника", "работа"]),
    Item(id=3, name="Кроссовки", price=9990.0, tags=["обувь", "спорт"]),
]

@app.get("/")
def read_root():
    return {"message": "Привет, бэкенд!", "status": "ok"}

@app.get("/items")
def get_items(min_price: Optional[float] = None, max_price: Optional[float] = None):
    result = items_db
    if min_price is not None:
        result = [i for i in result if i.price >= min_price]
    if max_price is not None:
        result = [i for i in result if i.price <= max_price]
    return result

# Сначала конкретный путь — чтобы не было путаницы
@app.get("/items/stats")
def get_items_stats():
    if not items_db:
        return {
            "count": 0,
            "average_price": 0.0,
            "min_price": None,
            "max_price": None
        }
    prices = [item.price for item in items_db]
    return {
        "count": len(items_db),
        "average_price": sum(prices) / len(prices),
        "min_price": min(prices),
        "max_price": max(prices)
    }

# Потом шаблонный путь с {item_id}
@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Товар не найден")

@app.post("/items")
def add_item(item: Item):
    if any(i.id == item.id for i in items_db):
        raise HTTPException(status_code=400, detail="ID уже существует")
    items_db.append(item)
    return item
