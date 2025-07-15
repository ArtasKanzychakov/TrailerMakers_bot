from aiogram.fsm.state import StatesGroup, State

class ProjectCreation(StatesGroup):
    name = State()
    brief = State()
    client = State()
    editors = State()
