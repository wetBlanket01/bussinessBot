from aiogram import types
from requests import get

from src.handlers.keyboards_handler import cb
from src.main import dp
from src.markups.markups import menu_markup

api_request = get("https://www.cbr-xml-daily.ru/daily_json.js").json()


@dp.callback_query_handler(cb.filter(action='api'))
async def send_api_info(call: types.CallbackQuery):
    try:
        await call.message.edit_text(text=f'Курс доллара: <b>{api_request["Valute"]["USD"]["Value"]}</b>руб.',
                                     reply_markup=menu_markup)
    except Exception as e:
        print(e)
