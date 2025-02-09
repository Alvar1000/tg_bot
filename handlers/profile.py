from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import Router
from states import Form  # Импортируем класс Form из файла states.py
from utils.data_manager import get_or_create_user, update_user_profile

router = Router()


# Команда /start для начала заполнения профиля
@router.message(Command("start"))
async def start_form(message: Message, state: FSMContext):
    user_id = message.from_user.id
    username = message.from_user.username or "NoUsername"

    # Создаем или получаем пользователя в базе данных
    get_or_create_user(user_id, username)

    await message.answer("Давайте создадим ваш профиль! Для начала введите ваше имя:")
    await state.set_state(Form.name)


# Обработчик для состояния "name"
@router.message(Form.name)
async def process_name(message: Message, state: FSMContext):
    user_id = message.from_user.id
    name = message.text

    # Сохраняем имя в FSM и обновляем данные в JSON
    await state.update_data(name=name)
    update_user_profile(user_id, "username", name)  # Обновляем имя в JSON

    await message.answer("Отлично! Теперь укажите ваш возраст:")
    await state.set_state(Form.age)  # Переходим к следующему состоянию


# Обработчик для состояния "age"
@router.message(Form.age)
async def process_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пожалуйста, введите корректный возраст (число):")
        return

    age = int(message.text)
    user_id = message.from_user.id

    # Сохраняем возраст в FSM и обновляем данные в JSON
    await state.update_data(age=age)
    update_user_profile(user_id, "age", age)  # Обновляем возраст в JSON

    await message.answer("Хорошо! Теперь укажите ваш рост (в см):")
    await state.set_state(Form.height)  # Переходим к следующему состоянию


# Обработчик для состояния "height"
@router.message(Form.height)
async def process_height(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пожалуйста, введите корректный рост (число):")
        return

    height = int(message.text)
    user_id = message.from_user.id

    # Сохраняем рост в FSM и обновляем данные в JSON
    await state.update_data(height=height)
    update_user_profile(user_id, "height", height)  # Обновляем рост в JSON

    await message.answer("Принято! Теперь укажите ваш вес (в кг):")
    await state.set_state(Form.weight)  # Переходим к следующему состоянию


# Обработчик для состояния "weight"
@router.message(Form.weight)
async def process_weight(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пожалуйста, введите корректный вес (число):")
        return

    weight = int(message.text)
    user_id = message.from_user.id

    # Сохраняем вес в FSM и обновляем данные в JSON
    await state.update_data(weight=weight)
    update_user_profile(user_id, "weight", weight)  # Обновляем вес в JSON

    await message.answer("Отлично! И последнее - укажите ваш город:")
    await state.set_state(Form.city)  # Переходим к следующему состоянию


# Обработчик для состояния "city"
@router.message(Form.city)
async def process_city(message: Message, state: FSMContext):
    city = message.text
    user_id = message.from_user.id

    # Сохраняем город в FSM и обновляем данные в JSON
    await state.update_data(city=city)
    update_user_profile(user_id, "city", city)  # Обновляем город в JSON

    # Получаем все данные пользователя
    user_data = await state.get_data()

    # Формируем сообщение с результатами
    profile_message = (
        f"Спасибо! Ваш профиль успешно создан:\n\n"
        f"Имя: {user_data['name']}\n"
        f"Возраст: {user_data['age']} лет\n"
        f"Рост: {user_data['height']} см\n"
        f"Вес: {user_data['weight']} кг\n"
        f"Город: {user_data['city']}"
    )

    await message.answer(profile_message)

    await state.clear()
