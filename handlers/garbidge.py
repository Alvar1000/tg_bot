import json
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states import WorkoutState
from utils.data_manager import load_user_data
from utils.data_manager import save_user_data
USER_DATA_FILE = "data/users.json"

router = Router()


@router.message(Command("log_workout"))
async def log_workout(message: types.Message, state: FSMContext):
    user_id = str(message.from_user.id)
    users = load_user_data()

    if user_id not in users:
        await message.answer("Вы не зарегистрированы! Используйте /register, чтобы зарегистрироваться.")
        return

    await state.set_state(WorkoutState.waiting_for_workout)
    await message.answer("Пожалуйста, введите нагрузку в минутах(Например, 30):")


@router.message(WorkoutState.waiting_for_workout)
async def receive_workout_amount(message: types.Message, state: FSMContext):
    user_id = str(message.from_user.id)
    users = load_user_data()

    try:
        workout_amount = int(message.text)
        users[user_id]['calories_consumed'] += workout_amount #Записываем в минутах, переводим в check_progress
        save_user_data(users)

        await message.answer(f'Записано {workout_amount} минут активности!')
        await state.clear()

    except ValueError:
        await message.answer("Пожалуйста, введите нагрузку в минутах(Например, 30). Попробуйте снова.")