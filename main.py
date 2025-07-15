import os  
from aiogram import Bot, Dispatcher, types  
from aiogram.filters import Command  
from aiogram.fsm.context import FSMContext  
from dotenv import load_dotenv  
from database import Session, Project  
from states import ProjectCreation  
from keyboards import admin_menu  

load_dotenv()  
bot = Bot(token=os.getenv("BOT_TOKEN"))  
dp = Dispatcher()  

# Проверка админа  
def is_admin(user_id: int) -> bool:  
    return user_id in [123456789]  # Ваш ID  

# Команда /admin  
@dp.message(Command("admin"))  
async def admin_access(message: types.Message):  
    if message.text.split()[-1] == os.getenv("ADMIN_KEYWORD"):  
        await message.answer("🔐 Вы вошли как админ!", reply_markup=admin_menu())  

# Создание проекта  
@dp.message(lambda m: m.text == "➕ Создать проект" and is_admin(m.from_user.id))  
async def create_project_start(message: types.Message, state: FSMContext):  
    await message.answer("Введите название проекта:")  
    await state.set_state(ProjectCreation.name)  

# Полный код с FSM-машиной и остальными хэндлерами...  

if __name__ == "__main__":  
    dp.run_polling(bot)  
