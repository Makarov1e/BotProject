from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main_kb = [
    [KeyboardButton(text="Найти заказ по номеру")]
]
main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт ниже')

button1 = InlineKeyboardButton(text="Ввести номер заказа", callback_data="button1")
inline_kb = [
    [button1]
]
inline = InlineKeyboardMarkup(inline_keyboard=[[button1]])



