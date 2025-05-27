# Задание 8*

# Имеется структура данных продукта.

# Сейчас кол-во товара на складе равно 0. Посчитайте кол-во исходя из вариантов товара на складе.
# Выведите через цикл все варианты товара на складе в виде строки в формате: "Название - цена (кол-во на складе)".
# Используя цикл, найдите вариант товара с максимальной ценой и выведите его название и цену в консоль.
# Выведите через цикл все отзывы о товаре в виде строки в формате: "Пользователь - Оценка - Комментарий".
# Посчитайте через цикл количество отзывов с оценкой 5 и выведите их количество в консоль.
# Через цикл выведите только названия файлов картинок (например, "main.jpg" и "side.jpg") товара в консоль.
# Используя цикл, найдите и выведите в консоль все отзывы пользователя с именем "techguy123".

product1 = {
    "productId": 1001,
    "productName": "Wireless Headphones",
    "description": "Noise-cancelling wireless headphones with Bluetooth 5.0 and 20-hour battery life.",
    "brand": "SoundPro",
    "category": "Electronics",
    "price": 199.99,
    "currency": "USD",
    "stock": {
        "available": True,
        "quantity": 0
    },
    "images": [
        "https://example.com/products/1001/main.jpg",
        "https://example.com/products/1001/side.jpg"
    ],
    "variants": [
        {
            "variantId": "1001_01",
            "color": "Black",
            "price": 199.99,
            "stockQuantity": 20
        },
        {
            "variantId": "1001_02",
            "color": "White",
            "price": 198.99,
            "stockQuantity": 30
        }
    ],
    "dimensions": {
        "weight": "0.5kg",
        "width": "18cm",
        "height": "20cm",
        "depth": "8cm"
    },
    "ratings": {
        "averageRating": 4.7,
        "numberOfReviews": 2
    },
    "reviews": [
        {
            "reviewId": 501,
            "userId": 101,
            "username": "techguy123",
            "rating": 5,
            "comment": "Amazing sound quality and battery life!"
        },
        {
            "reviewId": 502,
            "userId": 102,
            "username": "jane_doe",
            "rating": 4,
            "comment": "Great headphones but a bit pricey."
        }
    ]
}


total_quantity = sum(variant["stockQuantity"] for variant in product1["variants"])
print(f"Количество товара на складе: {total_quantity}")

print("-" * 50)

for variant in product1["variants"]:
    print(f"Название {product1['productName']} - цена{variant['price']} (на складе {variant['stockQuantity']} штук)")

print("-" * 50)

max_price = product1["variants"][0]
for variant in product1["variants"]:
    if variant["price"] > max_price["price"]:
        max_price = variant
print(f"Название - {max_price['color']}, цена - {max_price['price']}")

print("-" * 50)

for review in product1["reviews"]:
    print(f"Пользователь - {review['username']}, оценка - {review['rating']}, комментарии - {review['comment']}")

print("-" * 50)

rating_five_review = 0
for review in product1['reviews']:
    if review['rating'] == 5:
        rating_five_review += 1
print(f"Количество обзоров с оценкой в 5 баллов: {rating_five_review}")

print("-" * 50)

print("Ссылки на изображения:")
for image_adress in product1['images']:
    url_adress = image_adress.split('/')[-1]
    if url_adress == "main.jpg" or url_adress == "side.jpg":
        print(image_adress)

print("-" * 50)

for variant in product1["reviews"]:
    if variant["username"] == "techguy123":
        print(f"Пользователь с ником - {variant['username']}, оценка - {variant['rating']}, комментарий - {variant['comment']}")