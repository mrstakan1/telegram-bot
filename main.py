from ast import parse
from cgitb import reset
import telebot
from telebot import types
import keyboard as kb
from text import *
from functions import *
from config import TOKEN
bot = telebot.TeleBot(TOKEN)

#Bot start
@bot.message_handler(commands=['start', 'старт'])
def start_msg(message):
    bot.send_message(
    message.chat.id, 
    text = 'Здарова, нажми на любую кнопку :)', 
    reply_markup=kb.main_menu_button,
    parse_mode='html')
    
@bot.message_handler(content_types=['text'])
def main_menu(message): 
    if message.text == "FIND VIDEO":
        msg = bot.send_message(
            message.chat.id,
            text = '',
            reply_markup=kb.main_menu_button,
            parse_mode='html')
        bot.register_next_step_handler('')
            
    elif message.text == "CRYPTO":
        msg = bot.send_message(
            message.chat.id,
            text = crypto_menu_text,
            reply_markup=kb.crypto_menu,
            parse_mode = 'html')
        bot.register_next_step_handler(msg, crypto_menu)

    elif message.text == "DEVELOPER":
        msg = bot.send_message(
            message.chat.id,
            text = socials,
            reply_markup=kb.main_menu_button,
            parse_mode = 'html')

    elif message.text == "IP SCAN":
        msg = bot.send_message(
            message.chat.id,
            text = query_scan,
            reply_markup=kb.back_to_main_menu,
            parse_mode = 'html')
        bot.register_next_step_handler(msg, get_ip_from_user)

def crypto_menu(message):
    if message.text == 'MAIN MENU':
        msg = bot.send_message(message.chat.id, text = '[x] Welcome to Main Menu!', reply_markup=kb.main_menu_button)
        bot.register_next_step_handler(msg, main_menu)

    elif message.text == 'CRYPTO NEWS':
        news_list = get_crypto_news()
        for new in news_list:
            bot.send_message(message.chat.id, text=f'<a href="{new["link"]}"><b>{new["title"]}</b></a>', parse_mode="html")
        msg = bot.send_message(message.chat.id, text="This is last 5 news for now!", reply_markup=kb.crypto_menu)
        bot.register_next_step_handler(msg, crypto_menu)

    elif message.text == 'CRYPTO PRICES':
        msg = bot.send_message(
            message.chat.id,
            text = crypto_prices_text,
            reply_markup=kb.crypto_button,
            parse_mode = 'html')
        bot.register_next_step_handler(msg, get_crypto_ticker)

def get_crypto_ticker(message):
    if message.text == 'GO BACK':
        msg = bot.send_message(message.chat.id, text = '[x] You are in CRYPTO menu!', reply_markup=kb.crypto_menu)
        bot.register_next_step_handler(msg, crypto_menu)
    else:
        ticker = get_crypto_price(message.text)
        if ticker == False:
            msg = bot.send_message(message.chat.id, text = '[Х] Something went wrong', reply_markup=kb.crypto_button)
            bot.register_next_step_handler(msg, get_crypto_ticker)
        else:
            msg = bot.send_message(
            message.chat.id,
            text = ticker,
            reply_markup=kb.crypto_button,
            parse_mode = 'html') 
            bot.register_next_step_handler(msg, get_crypto_ticker)
    # bot.register_next_step_handler(msg, crypto_menu)

def get_ip_from_user(message):
    if message.text == 'MAIN MENU':
        msg = bot.send_message(message.chat.id, text = '[x] Welcome to Main Menu!', reply_markup=kb.main_menu_button)
        bot.register_next_step_handler(msg, main_menu)

    else:
        ip = message.text
        bot.send_message(message.chat.id,
        text = 'Начинаю сканирование...',
        reply_markup=kb.back_to_main_menu,
        parse_mode='html')
        result = get_ip_info(ip)

        if result == False:
            msg = bot.send_message(message.chat.id, text = '[Х] Something went wrong', reply_markup=kb.main_menu_button)
        else:
            msg = bot.send_message(message.chat.id,
            text = result,
            reply_markup=kb.back_to_main_menu,
            parse_mode='html')
        bot.register_next_step_handler(msg, get_ip_from_user)



bot.infinity_polling()
