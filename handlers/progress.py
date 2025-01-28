from aiogram import Router, types
from utils.data_manager import load_user_data

router = Router()


@router.message(commands=["check_progress"])
async def check_progress(message: types.Message):
    user_id = message.from_user.id
    data = load_user_data().get(str(user_id), {'water': 0, 'calories': 0})
    await message.answer(f"Ваш прогресс:\n\nВода: {data['water']} мл\nКалории: {data['calories']} ккал")

@router.message(commands=["check_progress"])
async def check_progress(message: types.Message):
    user_id = message.from_user.id
    data = load_user_data().get(str(user_id), {'water': 0, 'calories': 0})
    await message.answer(f"Ваш прогресс:\n\nВода: {data['water']} мл\nКалории:{data['calories']} ккал")
