from aiogram.types import *
# кнопки на старте
currency_button = KeyboardButton("Цены")
popular_button = KeyboardButton("Популярные")
about_button = KeyboardButton("Новые")
commands_btn = ReplyKeyboardMarkup(resize_keyboard=True)
commands_btn.add(currency_button,popular_button,about_button)
# инлайн кнопки для цен
inline_bitcoin_button = InlineKeyboardButton(text='bitcoin', callback_data='bitcoin currency')
inline_ethereum_button = InlineKeyboardButton(text="ethereum", callback_data='ethereum currency')
inline_tether_button = InlineKeyboardButton(text="tether", callback_data='tether currency')
inline_bnb_button = InlineKeyboardButton(text="bnb", callback_data='bnb currency')
inline_xrp_button = InlineKeyboardButton(text="xrp", callback_data='xrp currency')
inline_dogecoin_button = InlineKeyboardButton(text="dogecoin", callback_data='dogecoin currency')
price_inline_keyboard = InlineKeyboardMarkup(row_width=2)
price_inline_keyboard.add(inline_bitcoin_button,
                          inline_ethereum_button,
                          inline_tether_button,
                          inline_bnb_button,
                          inline_xrp_button,
                          inline_dogecoin_button)
#инлайн кнопки для конвертера
# inline_bitcoin_convert = InlineKeyboardButton(text='bitcoin', callback_data='bitcoin convert')
# inline_ethereum_convert = InlineKeyboardButton(text="ethereum", callback_data='ethereum convert')
# inline_tether_convert = InlineKeyboardButton(text="tether", callback_data='tether convert')
# inline_bnb_convert = InlineKeyboardButton(text="bnb", callback_data='bnb convert')
# inline_xrp_convert = InlineKeyboardButton(text="xrp", callback_data='xrp convert')
# inline_dogecoin_convert = InlineKeyboardButton(text="dogecoin", callback_data='dogecoin convert')
# convert_inline_keyboard = InlineKeyboardMarkup(row_width=2)
# convert_inline_keyboard.add(inline_bitcoin_convert,
#                             inline_ethereum_convert,
#                             inline_tether_convert,
#                             inline_bnb_convert,
#                             inline_xrp_convert,
#                             inline_dogecoin_convert)