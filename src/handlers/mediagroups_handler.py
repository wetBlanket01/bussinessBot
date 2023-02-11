from aiogram import types
from aiogram.types import MediaGroup

from src.handlers.keyboards_handler import cb
from src.main import dp


@dp.callback_query_handler(cb.filter(action='media_groups'))
async def send_media_group(call: types.CallbackQuery):
    media_group = MediaGroup()
    media_group.attach_photo(types.InputFile('src/images/mario_img.png'))
    media_group.attach_photo(types.InputFile('src/images/fish_in_hat_img.png'))
    media_group.attach_photo(types.InputFile('src/images/bless_u_img.png'))

    await call.message.answer_media_group(media=media_group)
