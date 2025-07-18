
import logging
import os
import telebot
from telebot.types import Message, CallbackQuery
from dotenv import load_dotenv
from keyboards.raspisaniye_kb import kb, value
from moiProyekt.parsers.vremy_namazov import nama_time, namaz
from utils.raspisaniye_utils import pretty_info, namaz_grozny, games
from random import randint


load_dotenv()
bot = telebot.TeleBot(os.getenv('API'))
logger = logging.getLogger(__name__)
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
secret_number = games()
guesses = {}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!', reply_markup=kb())


@bot.message_handler(commands=['info'])
def info(message: Message):
    if info:
        pretty_str = pretty_info()
        bot.send_message(message.chat.id, pretty_str)


@bot.message_handler(func=lambda message: message.text.startswith('/guess'))
def guess(message):
    no_cmd = message.text.replace('/guess', '').strip()
    bot.send_message(message.chat.id, f'Ведите число от 1 до 10: ')
    if guesses['guess'] == int(no_cmd):
        bot.send_message(message.chat.id, f'Вы угадали!👏🏻🎉')
        guesses.pop('guess')
    else:
        bot.send_message(message.chat.id, f'Вы не угадали!😭')


@bot.message_handler(func=lambda message: True)
def namaz_time(message):
    nama_time()
    if message.text == '🕌Расписание намазов!':
        bot.send_message(message.chat.id, namaz_grozny(), reply_markup=value())
    elif message.text == '🏫Расписание уроков!':
        bot.send_message(message.chat.id, f'Расписание уроков в милки.')
    elif message.text == '🎲Давай поиграем?':
        my_number = randint(1, 10)
        guesses['guess'] = my_number
        bot.send_message(message.chat.id, 'угадывай')


@bot.callback_query_handler(func=lambda callback: callback.data == 'Фаджр')
def buy_premium(callback: CallbackQuery):
    time, desc = namaz['Фаджр']
    bot.send_message(callback.message.chat.id, f"⏰ {time}\n📖 {desc}")


@bot.callback_query_handler(func=lambda callback: callback.data == 'Рассвет')
def buy_premium(callback: CallbackQuery):
    time, desc = namaz['Рассвет']
    bot.send_message(callback.message.chat.id, f"⏰ {time}\n📖 {desc}")


@bot.callback_query_handler(func=lambda callback: callback.data == 'Зухр')
def buy_premium(callback: CallbackQuery):
    time, desc = namaz['Зухр']
    bot.send_message(callback.message.chat.id, f"⏰ {time}\n📖 {desc}")


@bot.callback_query_handler(func=lambda callback: callback.data == 'Аср')
def buy_premium(callback: CallbackQuery):
    time, desc = namaz['Аср']
    bot.send_message(callback.message.chat.id, f"⏰ {time}\n📖 {desc}")


@bot.callback_query_handler(func=lambda callback: callback.data == 'Магриб')
def buy_premium(callback: CallbackQuery):
    time, desc = namaz['Магриб']
    bot.send_message(callback.message.chat.id, f"⏰ {time}\n📖 {desc}")


@bot.callback_query_handler(func=lambda callback: callback.data == 'Иша')
def buy_premium(callback: CallbackQuery):
    time, desc = namaz['Иша']
    bot.send_message(callback.message.chat.id, f"⏰ {time}\n📖 {desc}")


if __name__ == '__main__':
    bot.polling()
