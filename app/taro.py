import asyncio
from aiogram import Bot, Dispatcher
from app.config import API_TOKEN
from app.handlers import router
import json

pip freeze > requirements.txt
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