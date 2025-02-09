from datetime import datetime
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from utils.data_manager import load_user_data, save_user_data

router = Router()

# MET-значения для фиксированных тренировок
MET_VALUES = {
    "бег": 9.8,
    "йога": 2.5,
    "силовая": 6.0,
    "велосипед": 8.0
}

@router.message(Command("log_workout"))
async def handle_log_workout(message: Message):
    try:
        user_id = message.from_user.id
        args = message.text.split()
        if len(args) < 3:
            await message.reply("Пожалуйста, введите тип тренировки и продолжительность (в минутах). Например: /log_workout бег 30")
            return

        workout_type = args[1].lower()
        if workout_type not in MET_VALUES and workout_type != "калории":
            await message.reply("Неверный тип тренировки. Доступные варианты: бег, йога, силовая, велосипед.")
            return

        user_data = load_user_data().get(str(user_id))
        weight = user_data['weight']

        if workout_type == "калории":
            calories_burned = int(args[2])
        else:
            duration = int(args[2])
            if duration <= 0:
                await message.reply("Продолжительность тренировки должна быть положительным числом.")
                return

            met = MET_VALUES[workout_type]
            calories_burned = weight * met * (duration / 60)
        users = load_user_data()
        users[str(user_id)]["calories_burned"] += calories_burned

        save_user_data(users)

        await message.reply(
            f"🏋️‍♂️ Тренировка успешно записана!\n"
            f"{'Тип: ' + workout_type.capitalize() if workout_type != 'калории' else ''}\n"
            f"{'Длительность: ' + str(duration) + ' минут' if workout_type != 'калории' else ''}\n"
            f"Сожжено калорий: {calories_burned:.1f} ккал\n\n"
        )
    except ValueError:
        await message.reply("Пожалуйста, введите корректное число для длительности или калорий.")