from utils.api import get_food_info

import json
from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states import FoodState

router = Router()
@router.message(Command("log_food"))
async def start_log_food(message: types.Message, state: FSMContext):
    await message.answer("Введите название продукта:")
    await state.set_state(FoodState.waiting_for_food)  # Устанавливаем состояние ожидания


@router.message(FoodState.waiting_for_food)
async def receive_food_name(message: types.Message, state: FSMContext):
    food_name = message.text.strip()
    food_info = get_food_info(food_name)

    if food_info:
        user_id = str(message.from_user.id)
        calories = food_info['calories']

        try:
            with open("data/users.json", "r", encoding="utf-8") as file:
                users = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            await message.answer("Не зарегистрированы")

        if user_id in users:
            users[user_id]["calories_consumed"] += calories
        else:
            await message.answer("Не зарегистрированы")

        with open("data/users.json", "w", encoding="utf-8") as file:
            json.dump(users, file, indent=4, ensure_ascii=False)

        await message.answer(f"🍎 {food_info['name']} содержит {calories} ккал на 100 г. Записано в ваш дневник!")
    else:
        await message.answer("Не удалось найти продукт. Попробуйте снова.")

    await state.clear()
