import telebot
import keyboard as kb
from text import *
from functions import *
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

#Bot start
@bot.message_handler(commands=['start', 'refresh'])
def start_msg(message):
    bot.send_message(
    message.chat.id, 
    text = start_text, 
    reply_markup=kb.main_menu,
    parse_mode='html'
    )
    
@bot.message_handler(content_types=['text'])
def main_menu(message): 
    if message.text == "FIND VIDEO📺":
        msg = bot.send_message(
            message.chat.id,
            text = video_text,
            reply_markup=kb.back_to_main_menu,
            parse_mode='html'
            )
        bot.register_next_step_handler(msg, get_video_title)
            
    elif message.text == "CRYPTO💵":
        msg = bot.send_message(
            message.chat.id,
            text = crypto_menu_text,
            reply_markup=kb.crypto_menu,
            parse_mode = 'html'
            )
        bot.register_next_step_handler(msg, crypto_menu)

    elif message.text == "CREATOR🔐":
        msg = bot.send_message(
            message.chat.id,
            text = socials,
            reply_markup=kb.main_menu,
            parse_mode = 'html'
            )

    elif message.text == "IP SCAN🔧":
        msg = bot.send_message(
            message.chat.id,
            text = query_scan,
            reply_markup=kb.back_to_main_menu,
            parse_mode = 'html'
            )
        bot.register_next_step_handler(msg, get_ip_from_user)
    else:
        msg = bot.send_message(
            message.chat.id,
            text = '❗️Something went wrong, try again.',
            reply_markup=kb.main_menu,
            parse_mode='html'
            )

def crypto_menu(message):
    if message.text == 'MAIN MENU📲':
        msg = bot.send_message(message.chat.id, text = '⚠️Welcome to Main Menu!', reply_markup=kb.main_menu)
        bot.register_next_step_handler(msg, main_menu)

    elif message.text == 'CRYPTO NEWS📰':
        news_list = get_crypto_news()
        for new in news_list:
            bot.send_message(message.chat.id, text=f'<a href="{new["link"]}"><b>{new["title"]}</b></a>', parse_mode="html")
        msg = bot.send_message(message.chat.id, text="⚠️This is last 5 news for now!", reply_markup=kb.crypto_menu)
        bot.register_next_step_handler(msg, crypto_menu)

    elif message.text == 'CRYPTO PRICES💵':
        msg = bot.send_message(
            message.chat.id,
            text = crypto_prices_text,
            reply_markup=kb.crypto_button,
            parse_mode = 'html')
        bot.register_next_step_handler(msg, get_crypto_ticker)

def get_crypto_ticker(message):
    if message.text == '🔙 GO BACK':
        msg = bot.send_message(message.chat.id, text = '⚠️You are in CRYPTO menu!', reply_markup=kb.crypto_menu)
        bot.register_next_step_handler(msg, crypto_menu)
    else:
        ticker = get_crypto_price(message.text)
        if ticker == False:
            msg = bot.send_message(message.chat.id, text = '❗️Something went wrong, try again.', reply_markup=kb.crypto_button)
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
    if message.text == 'MAIN MENU📲':
        msg = bot.send_message(message.chat.id, text = '⚠️ Welcome to Main Menu!', reply_markup=kb.main_menu)
        bot.register_next_step_handler(msg, main_menu)

    else:
        ip = message.text
        bot.send_message(message.chat.id,
        text = '👀Scanning...',
        reply_markup=kb.back_to_main_menu,
        parse_mode='html')
        result = get_ip_info(ip)

        if result == False:
            msg = bot.send_message(message.chat.id, text = '❗️Something went wrong, try again.', reply_markup=kb.main_menu)
        else:
            msg = bot.send_message(message.chat.id,
            text = result,
            reply_markup=kb.back_to_main_menu,
            parse_mode='html')
        bot.register_next_step_handler(msg, get_ip_from_user)

def get_video_title(message):
    if message.text == 'MAIN MENU📲': 
        msg = bot.send_message(message.chat.id, text = '⚠️Welcome to Main Menu!', reply_markup=kb.main_menu)
        bot.register_next_step_handler(msg, main_menu)
    else:
        videos_list = get_video(message.text)
        for video in videos_list:
            bot.send_message(message.chat.id, text=f'<a href="{video["link"]}"><b>{video["title"]}</b></a>', parse_mode="html")
        msg = bot.send_message(message.chat.id, text="⚠️Here is 5 most popular results", reply_markup=kb.main_menu)
        bot.register_next_step_handler(msg, main_menu)
            




bot.infinity_polling()
