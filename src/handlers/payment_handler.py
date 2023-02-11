from aiogram import types
from aiogram.types import LabeledPrice, PreCheckoutQuery, ContentType

from src.config.config import payment_token
from src.handlers.keyboards_handler import cb
from src.main import bot, dp
from src.markups.markups import menu_markup

price = [LabeledPrice(label='Наушники', amount=400*100)]


@dp.callback_query_handler(cb.filter(action='payments_system'))
async def buy_process(call: types.CallbackQuery):
    await bot.send_invoice(call.message.chat.id,
                           title='Наушники',
                           description='супер крутые',
                           provider_token=payment_token,
                           currency='rub',
                           need_phone_number=True,
                           prices=price,
                           start_parameter='example',
                           payload='some_invoice',
                           is_flexible=False)


@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_process(pre_checkout: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def success_payment(message: types.Message):
    await message.answer(text=f'Товар - <b>{price[0].label}</b>\nЦена - <b>{int(price[0].amount) // 100}</b>руб.',
                         reply_markup=menu_markup)
