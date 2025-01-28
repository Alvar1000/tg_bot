from aiogram import Router, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states import Form

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.reply("Weelcome to fitness bot")

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.reply(
        "Доступные команды:\n"
    )

@router.message(Command("Form"))
async def start_form(message: Message, state: FSMContext):
    await message.reply("Как вас зовут?")
    await state.set_state(Form.name)

@router.message(Form.name)
async def process_name(message: Message, state: FSMContext):
    await message.reply("Введите ваш возраст")
    await state.set_state(Form.age)

@router.message(Form.age)
async def proccess_age(message:Message, state: FSMContext):
    await message.reply("Введите ваш рост(в см)")
    await state.set_state(Form.height)

@router.message(Form.height)
async def proccess_height(message:Message, state: FSMContext):
    await message.reply("Введите ваш вес(в кг)")
    await state.set_state(Form.weight)

@router.message(Form.city)
async def proccess_weight(message:Message, state: FSMContext):
    await message.reply("В каком городе вы находитесь?")
    await state.set_state(Form.city)

@router.message(Form.city)
async def proccess_city(message: Message, state: FSMContext):
    await message.reply("Ваш профиль создан! Вы можете начать работу.")
    await state.clear()




