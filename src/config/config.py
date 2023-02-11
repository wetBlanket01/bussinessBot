from dataclasses import dataclass
token = "5815969979:AAGO8vWsfvy643RbekCqMyh8ungQQHYo6sg" # NOQA
payment_token = "381764678:TEST:49011"


@dataclass
class Messages:
    menu_message: str = '<b>Список заданий</b>'
    enter_name_message: str = 'Введите имя'
    choose_male_message: str = 'Выберите пол'
    enter_photo_message: str = 'Отправьте ваше фото'


@dataclass
class MenuKeyboardMessages:
    keyboard_message: str = 'Клавиатуры'
    machine_state_message: str = 'Машинное состояние'
    payments_system_message: str = 'Платёжная система'
    api_message: str = 'API'
    database_message: str = 'СУБД'
    media_groups_message: str = 'Медиа группы'
    menu_message: str = 'Меню'


@dataclass
class DatabaseKeyboardsMessages:
    add_user_message: str = 'Добавить пользователя в БД'
    check_user_message: str = 'Проверить на наличие пользователя'
    update_name_message: str = 'Изменить имя пользователя'
    delete_user_message: str = 'Удалить пользователя'
    get_rand_num_message: str = 'Получить число'
