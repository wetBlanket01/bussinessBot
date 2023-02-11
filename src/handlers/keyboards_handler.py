from aiogram import types
from aiogram.utils.callback_data import CallbackData

from src.config.config import Messages
from src.main import dp
from src.markups.markups import to_menu_markup, menu_markup

cb = CallbackData('btn', 'action')


@dp.callback_query_handler(cb.filter(action='keyboard'))
async def keyboards_handler(call: types.CallbackQuery):
    await call.message.edit_text(text=f'Ваш Username: <b>{call.message.chat.username}</b>', reply_markup=to_menu_markup)


@dp.callback_query_handler(cb.filter(action='menu'))
async def to_menu(call: types.CallbackQuery):
    await call.message.edit_text(text=Messages.menu_message, reply_markup=menu_markup)
