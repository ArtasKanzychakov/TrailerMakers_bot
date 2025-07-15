import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from handlers import admin  # можно подключить и другие

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"), parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Регистрируем хэндлеры
dp.include_router(admin.router)

if __name__ == "__main__":
    dp.run_polling(bot)
