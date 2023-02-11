from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from src.config.config import Messages
from src.handlers.keyboards_handler import cb
from src.main import dp
from src.markups.markups import male_markup, to_menu_reply


class User(StatesGroup):
    user_name = State()
    user_male = State()
    user_photo = State()


@dp.callback_query_handler(cb.filter(action='machine_state'), state=None)
async def user_form_start(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer(Messages.enter_name_message)

    await User.user_name.set()


@dp.message_handler(content_types=['text'], state=User.user_name)
async def get_user_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_name'] = str(message.text)

    await User.next()
    await message.answer(Messages.choose_male_message, reply_markup=male_markup)


@dp.message_handler(content_types=['text'], state=User.user_male)
async def get_user_male(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_male'] = str(message.text)

    await User.next()
    await message.answer(Messages.enter_photo_message, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(content_types=['photo'], state=User.user_photo)
async def send_user_form(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_photo'] = str(message.photo[0].file_id)
    user_form_message = f"""Имя: <b>{data.get('user_name')}</b>\nПол: <b>{data['user_male']}</b>"""
    await message.answer_photo(caption=user_form_message, photo=data['user_photo'], reply_markup=to_menu_reply)
    await state.finish()
