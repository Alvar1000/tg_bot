from aiogram import Router, types


router = Router()
user_data = {}

@router.message(comands=['log_water'])
async def log_water(message: types.Message):
    try:
        water_amount = int(message.get_args())
        user_id = message.from_user.id
        user_data.setdefoult(user_id,{'water':0})
        user_data[user_id]['water'] += water_amount
        await message.answer(f"Записано {water_amount} мл воды")
    except ValueError:
        await message.answer("Введите кол-во воды в миллилитрах")