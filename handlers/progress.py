from aiogram import Router, types
from aiogram.filters import Command
from utils.data_manager import load_user_data
from utils.calculations import calculate_water, calculate_calories
from utils.weather_api import get_current_temp

router = Router()



@router.message(Command("check_progress"))
async def check_progress(message: types.Message):
    user_id = message.from_user.id
    user_data = load_user_data().get(str(user_id), {
        "weight": None,
        "height": None,
        "age": None,
        "activity_minutes": None,
        "city": 'London',
        "water_consumed": 0,
        "calories_consumed": 0,
        "calories_burned": 0,
    })

    temperature = get_current_temp(user_data["city"])
    daily_water_norm = calculate_water(user_data["weight"], user_data['calories_consumed'], temperature)
    daily_calories_norm = calculate_calories(user_data["weight"], user_data["height"], user_data["age"], user_data['calories_consumed'])

    water_remaining = max(0, daily_water_norm - user_data["water_consumed"])
    calorie_balance = max(0, user_data["calories_consumed"] - user_data["calories_burned"])

    await message.answer(
        f"Ваш прогресс:\n\n"
        f"💧 Вода:\n"
        f"- Выпито: {user_data['water_consumed']} мл из {daily_water_norm} мл.\n"
        f"- Осталось: {water_remaining} мл.\n\n"
        f"🔥 Калории:\n"
        f"- Потреблено: {user_data['calories_consumed']} ккал из {daily_calories_norm} ккал.\n"
        f"- Сожжено: {user_data['calories_burned']} ккал.\n"
    )