from aiogram import types
from src.config.config import Messages, MenuKeyboardMessages
from src.main import dp
from src.markups.markups import menu_markup


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(Messages.menu_message, reply_markup=menu_markup)


@dp.message_handler(content_types=['text'])
async def to_menu(message: types.Message):
    if str(message.text) == MenuKeyboardMessages.menu_message:
        await start(message)
