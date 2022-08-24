from telebot import types

#Main menu buttons
main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.row("DEVELOPER")
main_menu.row('IP SCAN', 'FIND VIDEO', "CRYPTO")

#Back to main menu
back_to_main_menu= types.ReplyKeyboardMarkup(resize_keyboard=True)
back_to_main_menu.row('MAIN MENU')

#Crypto Menu
crypto_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
crypto_menu.row('CRYPTO PRICES', 'CRYPTO NEWS', 'MAIN MENU')

#Cryptovalues
crypto_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
crypto_button.row('BTC', 'ETH','ETC')
crypto_button.row('GO BACK')
