import asyncio
from aiogram import Bot, Dispatcher
from configs import TOKEN
from aiogram.filters import Command
from middlewares import LoggingMiddleware
from handlers import food, profile, progress, water, workout

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.message.middleware(LoggingMiddleware())
routers = [
    food.router,
    profile.router,
    progress.router,
    water.router,
    workout.router,
]

dp.include_routers(*routers)

async def main():
    print("Bot started!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())