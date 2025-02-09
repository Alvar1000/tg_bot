import json
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states import WaterState
from utils.data_manager import load_user_data
from utils.data_manager import save_user_data
USER_DATA_FILE = "data/users.json"

router = Router()

@router.message(Command("log_water"))
async def log_water(message: types.Message, state: FSMContext):
    """Запрос на ввод количества воды"""
    user_id = str(message.from_user.id)
    users = load_user_data()

    # Проверяем, зарегистрирован ли пользователь
    if user_id not in users:
        await message.answer("Вы не зарегистрированы! Используйте /register, чтобы зарегистрироваться.")
        return

    # Сохраняем пользователя в состояние
    await state.set_state(WaterState.waiting_for_water)
    await message.answer("Пожалуйста, введите количество воды в миллилитрах (например, 300):")

@router.message(WaterState.waiting_for_water)
async def receive_water_amount(message: types.Message, state: FSMContext):
    """Получаем количество воды и сохраняем в базе"""
    user_id = str(message.from_user.id)
    users = load_user_data()

    # Проверяем, является ли введенное значение числом
    try:
        water_amount = int(message.text)
        users[user_id]["water_consumed"] += water_amount  # Обновляем данные
        save_user_data(users)  # Сохраняем обновленные данные

        await message.answer(f"💧 Записано {water_amount} мл воды! Всего сегодня выпито: {users[user_id]['water_consumed']} мл.")
        await state.clear()  # Сбрасываем состояние после получения данных
    except ValueError:
        await message.answer("Введите количество воды в миллилитрах (например, 300). Попробуйте снова.")


