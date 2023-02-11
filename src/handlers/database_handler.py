from aiogram import types

from src.handlers.keyboards_handler import cb
from src.main import dp, db
from src.markups.markups import database_markup


@dp.callback_query_handler(cb.filter(action='database'))
async def database_handler(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=database_markup)


@dp.callback_query_handler(cb.filter(action='add_user'))
async def add_user(call: types.CallbackQuery):
    try:
        await db.add_user(call.message.chat.username)
    finally:
        await call.message.edit_text(text='<b>Пользователь добавлен</b>', reply_markup=database_markup)


@dp.callback_query_handler(cb.filter(action='check_user'))
async def check_user(call: types.CallbackQuery):
    try:
        check_value = await db.check_user(call.message.chat.username)
        await call.message.edit_text(
            text='<b>Пользователь есть в базе</b>' if check_value == 1 else '<b>Пользователь отсутствует</b>',
            reply_markup=database_markup)
    except Exception:
        pass


@dp.callback_query_handler(cb.filter(action='update_name'))
async def update_name(call: types.CallbackQuery):
    try:
        await db.update_name(call.message.chat.username)
        await call.message.edit_text(text='<b>Имя изменено</b>', reply_markup=database_markup)
    except Exception:
        pass


@dp.callback_query_handler(cb.filter(action='delete_user'))
async def delete_user(call: types.CallbackQuery):
    try:
        await db.delete_user(call.message.chat.username)
        await call.message.edit_text(text='<b>Пользователь удален</b>', reply_markup=database_markup)
    except Exception:
        pass


@dp.callback_query_handler(cb.filter(action='get_rand_num'))
async def get_rand_num(call: types.CallbackQuery):
    try:
        rand_num = await db.get_rand_num(call.message.chat.username)
        await call.message.edit_text(text=f'<b>{rand_num[0][0]}</b>', reply_markup=database_markup)
    except Exception:
        pass
