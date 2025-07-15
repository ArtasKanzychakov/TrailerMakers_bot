from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def admin_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="➕ Создать проект")],
            [KeyboardButton(text="🗑 Удалить проект")],
            [KeyboardButton(text="👥 Управление монтажёрами")],
            [KeyboardButton(text="📋 Список проектов")]
        ],
        resize_keyboard=True
    )
