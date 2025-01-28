from aiogram import Router, types

router = Router()

@router.message(commands=["log_food"])
async def log_food(message: types.Message):
    food_name = message.get_args()
    food_info = get_food_info(food_name)
    if food_info:
        await message.answer(f"{food_info['name']} содержит {food_info['calories']} ккал на 100 г. Сколько грамм вы съели?")
    else:
        await message.answer("Не удалось найти продукт. Попробуйте другой запрос.")
