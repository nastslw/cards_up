import asyncio
from aiogram import Bot, Dispatcher

from handlers import router
import json

import os
from dotenv import load_dotenv

load_dotenv()  # загрузить все переменные из .env файла в окружение

API_TOKEN = os.getenv("API_TOKEN")  # забираем токен из переменных окружения

bot = Bot(token=API_TOKEN)

dp = Dispatcher()


# Загрузка JSON


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')