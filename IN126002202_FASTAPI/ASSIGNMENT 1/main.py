# requires pip intall fastapi
from fastapi import FastAPI
#now app stores the FastAPI instance which we can use to define our API endpoints
app = FastAPI()

# Product Data
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 599, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 120, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "Marker Pen", "price": 49, "category": "Stationery", "in_stock": True},
    {"id": 4, "name": "USB-C Cable", "price": 199, "category": "Electronics", "in_stock": False},

    # adding products mentioned in question 1
    {"id": 5, "name": "Laptop Stand", "price": 999, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1499, "category": "Electronics", "in_stock": False}
]

# Root
@app.get("/")
def home():
    return {"message": "FastAPI Assignment 1 by CHINMAY J (IN126002202)"}

# Q1 – Show all products and total count of the poducts
@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }


# Q2 – Filter by category ("electronics", "stationery", etc.)
@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):

    filtered = [
        product for product in products
        if product["category"].lower() == category_name.lower()
    ]

    if not filtered:
        return {"error": "No products found in this category"}

    return {
        "category": category_name,
        "products": filtered,
        "count": len(filtered)
    }


# Q3 – Only in-stock products
@app.get("/products/instock")
def get_instock_products():

    instock = [
        product for product in products
        if product["in_stock"] == True
    ]

    return {
        "in_stock_products": instock,
        "count": len(instock)
    }


# Q4 – Store summary
@app.get("/store/summary")
def store_summary():

    total = len(products)

    in_stock = len([p for p in products if p["in_stock"]])
    out_of_stock = total - in_stock

    categories = list(set([p["category"] for p in products]))

    return {
        "store_name": "My E-commerce Store",
        "total_products": total,
        "in_stock": in_stock,
        "out_of_stock": out_of_stock,
        "categories": categories
    }


# Q5 – Search products(not case-sensitive)
@app.get("/products/search/{keyword}")
def search_products(keyword: str):

    results = [
        product for product in products
        if keyword.lower() in product["name"].lower()
    ]

    if not results:
        return {"message": "No products matched your search"}

    return {
        "matched_products": results,
        "count": len(results)
    }


# ⭐ Bonus – Deals endpoint
@app.get("/products/deals")
def product_deals():

    cheapest = min(products, key=lambda x: x["price"])
    expensive = max(products, key=lambda x: x["price"])

    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }