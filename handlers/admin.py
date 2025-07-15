from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from keyboards import admin_menu
from utils.roles import is_admin
from states import ProjectCreation

router = Router()

@router.message(Command("admin"))
async def admin_access(message: types.Message):
    try:
        keyword = message.text.split(" ")[1]
    except IndexError:
        return await message.answer("❗ Укажите код доступа: /admin <код>")

    if keyword == os.getenv("ADMIN_KEYWORD"):
        if is_admin(message.from_user.id):
            await message.answer("✅ Добро пожаловать в админ-панель", reply_markup=admin_menu())
        else:
            await message.answer("🚫 У вас нет прав администратора.")

@router.message(F.text == "➕ Создать проект")
async def create_project(message: types.Message, state: FSMContext):
    if not is_admin(message.from_user.id):
        return await message.answer("⛔ Только админ может создать проект.")
    
    await state.set_state(ProjectCreation.name)
    await message.answer("Введите название проекта:")
