from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from src.config.config import MenuKeyboardMessages, DatabaseKeyboardsMessages

menu_markup = InlineKeyboardMarkup(inline_keyboard=[[]])

keyboard_button = InlineKeyboardButton(MenuKeyboardMessages.keyboard_message, callback_data='btn:keyboard')
machine_state_button = InlineKeyboardButton(MenuKeyboardMessages.machine_state_message,
                                            callback_data='btn:machine_state')
payments_system_button = InlineKeyboardButton(MenuKeyboardMessages.payments_system_message,
                                              callback_data='btn:payments_system')  # NOQA
api_button = InlineKeyboardButton(MenuKeyboardMessages.api_message, callback_data='btn:api')
database_button = InlineKeyboardButton(MenuKeyboardMessages.database_message, callback_data='btn:database')
media_groups_button = InlineKeyboardButton(MenuKeyboardMessages.media_groups_message, callback_data='btn:media_groups')

menu_markup \
    .add(keyboard_button) \
    .add(machine_state_button) \
    .add(payments_system_button) \
    .add(api_button, database_button) \
    .add(media_groups_button)

to_menu_markup = InlineKeyboardMarkup(inline_keyboard=[[]])
to_menu_button = InlineKeyboardButton(MenuKeyboardMessages.menu_message, callback_data='btn:menu')
to_menu_markup.add(to_menu_button)

male_markup = ReplyKeyboardMarkup(resize_keyboard=True) \
    .row(KeyboardButton('Мужской'), KeyboardButton('Женский'))

to_menu_reply = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) \
    .add(KeyboardButton(MenuKeyboardMessages.menu_message))

database_markup = InlineKeyboardMarkup(inline_keyboard=[[]])
add_user_button = InlineKeyboardButton(DatabaseKeyboardsMessages.add_user_message, callback_data='btn:add_user')
check_user_button = InlineKeyboardButton(DatabaseKeyboardsMessages.check_user_message, callback_data='btn:check_user')
update_name_button = InlineKeyboardButton(DatabaseKeyboardsMessages.update_name_message,
                                          callback_data='btn:update_name')
delete_user_button = InlineKeyboardButton(DatabaseKeyboardsMessages.delete_user_message,
                                          callback_data='btn:delete_user')
get_rand_num_button = InlineKeyboardButton(DatabaseKeyboardsMessages.get_rand_num_message,
                                           callback_data='btn:get_rand_num')

database_markup \
    .add(add_user_button) \
    .add(check_user_button) \
    .add(update_name_button) \
    .add(delete_user_button) \
    .add(get_rand_num_button)
