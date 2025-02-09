import requests


def get_food_info(food_name):
    url = f"https://world.openfoodfacts.org/cgi/search.pl?action=process&search_terms={food_name}&json=true"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "products" in data and len(data["products"]) > 0:
            product = data["products"][0]  # Берем первый найденный продукт
            name = product.get("product_name", "Неизвестный продукт")
            calories = product.get("nutriments", {}).get("energy-kcal_100g", "Нет данных")

            return {
                "name": name,
                "calories": calories
            }

    return None
