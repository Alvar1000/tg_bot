def calculate_water(weight, activity_minutes, temperature):
    base_water = weight * 30  # мл
    activity_water = (activity_minutes // 30) * 500
    weather_water = 500 if temperature > 25 else 0
    return base_water + activity_water + weather_water

def calculate_calories(weight, height, age, activity_minutes):
    bmr = 10 * weight + 6.25 * height - 5 * age
    activity_calories = (activity_minutes // 30) * 200
    return bmr + activity_calories
