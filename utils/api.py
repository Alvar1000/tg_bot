import request


def get_food_info(food_name):
    url = f"https://world.openfoodfacts.org/api/v0/product/{food_name}.json"
    response = request.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("product"):
            return {
                "name": data["product"]["product_name"],
                "calories": data["product"]["nutriments"]["energy-kcal_100g"]
            }
    return None