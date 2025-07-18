
# from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def kb():
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    button1 = KeyboardButton('🕌Расписание намазов!')
    button2 = KeyboardButton('🏫Расписание уроков!')
    button3 = KeyboardButton('🎲Давай поиграем?')
    keyboard.add(button1, button2, button3)
    return keyboard


def value():
    kb_inl = [
        [InlineKeyboardButton(text='🌉Фаджр', callback_data='Фаджр')],
        [InlineKeyboardButton(text='🌄Рассвет', callback_data='Рассвет')],
        [InlineKeyboardButton(text='☀️Зухр', callback_data='Зухр')],
        [InlineKeyboardButton(text='🌇Аср', callback_data='Аср')],
        [InlineKeyboardButton(text='🏙️Магриб', callback_data='Магриб')],
        [InlineKeyboardButton(text='🌃Иша', callback_data='Иша')]
    ]
    return InlineKeyboardMarkup(keyboard=kb_inl)
