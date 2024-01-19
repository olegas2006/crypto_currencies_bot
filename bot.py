from aiogram import *
from aiogram.types import *
import keyboard as kb
from aiogram.utils.markdown import  hlink
import sys

# создание бота
TOKEN = "5925374550:AAHkYHStUGLbN1UTy0CXpVW27jH0ibmXdZY"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
#обработка старта
@dp.message_handler(commands = ['start'])
async def welcome(message : types.Message):
    await message.answer("Привет, " +message.from_user.first_name+ "\nВыбери нужную тебе команду и я тебе помогу", reply_markup=kb.commands_btn)
@dp.message_handler()
# обработка стартовых кнопок
async def first_keyboard(message : types.Message):
    if message.text == "Цены":
        await message.answer("Выберите валюту на которую хотите узнать цену: ", reply_markup=kb.price_inline_keyboard)
    elif message.text == "Популярные":
        import popular as ppl
        await message.answer("Топ 30 валют на крипто-рынке:\n"
                             +hlink(ppl.popular_names[0], ppl.final_links[0])+'\n'
                             +hlink(ppl.popular_names[1], ppl.final_links[1])+'\n'
                             +hlink(ppl.popular_names[2], ppl.final_links[2])+'\n'
                             +hlink(ppl.popular_names[3], ppl.final_links[3])+'\n'
                             +hlink(ppl.popular_names[4], ppl.final_links[4])+'\n'
                             +hlink(ppl.popular_names[5], ppl.final_links[5])+'\n'
                             +hlink(ppl.popular_names[6], ppl.final_links[6])+'\n'
                             +hlink(ppl.popular_names[7], ppl.final_links[7])+'\n'
                             +hlink(ppl.popular_names[8], ppl.final_links[8])+'\n'
                             +hlink(ppl.popular_names[9], ppl.final_links[9])+'\n'
                             +hlink(ppl.popular_names[10], ppl.final_links[10]) + '\n'
                             +hlink(ppl.popular_names[11], ppl.final_links[11]) + '\n'
                             +hlink(ppl.popular_names[12], ppl.final_links[12]) + '\n'
                             +hlink(ppl.popular_names[13], ppl.final_links[13]) + '\n'
                             +hlink(ppl.popular_names[14], ppl.final_links[14]) + '\n'
                             +hlink(ppl.popular_names[15], ppl.final_links[15]) + '\n'
                             +hlink(ppl.popular_names[16], ppl.final_links[16]) + '\n'
                             +hlink(ppl.popular_names[17], ppl.final_links[17]) + '\n'
                             +hlink(ppl.popular_names[18], ppl.final_links[18]) + '\n'
                             +hlink(ppl.popular_names[19], ppl.final_links[19]) + '\n'
                             +hlink(ppl.popular_names[20], ppl.final_links[20]) + '\n'
                             +hlink(ppl.popular_names[21], ppl.final_links[21]) + '\n'
                             +hlink(ppl.popular_names[22], ppl.final_links[22]) + '\n'
                             +hlink(ppl.popular_names[23], ppl.final_links[23]) + '\n'
                             +hlink(ppl.popular_names[24], ppl.final_links[24]) + '\n'
                             +hlink(ppl.popular_names[25], ppl.final_links[25]) + '\n'
                             +hlink(ppl.popular_names[26], ppl.final_links[26]) + '\n'
                             +hlink(ppl.popular_names[27], ppl.final_links[27]) + '\n'
                             +hlink(ppl.popular_names[28], ppl.final_links[28]) + '\n'
                             +hlink(ppl.popular_names[29], ppl.final_links[29]) + '\n',
                             parse_mode='HTML')
        del sys.modules['popular']
    elif message.text == "Новые":
        import new as n
        await message.answer("Топ 30 новых валют на крипто-рынке:\n"
                             +hlink(n.popular_names[0], n.final_links[0])+'\n'
                             +hlink(n.popular_names[1], n.final_links[1])+'\n'
                             +hlink(n.popular_names[2], n.final_links[2])+'\n'
                             +hlink(n.popular_names[3], n.final_links[3])+'\n'
                             +hlink(n.popular_names[4], n.final_links[4])+'\n'
                             +hlink(n.popular_names[5], n.final_links[5])+'\n'
                             +hlink(n.popular_names[6], n.final_links[6])+'\n'
                             +hlink(n.popular_names[7], n.final_links[7])+'\n'
                             +hlink(n.popular_names[8], n.final_links[8])+'\n'
                             +hlink(n.popular_names[9], n.final_links[9])+'\n'
                             +hlink(n.popular_names[10], n.final_links[10]) + '\n'
                             +hlink(n.popular_names[11], n.final_links[11]) + '\n'
                             +hlink(n.popular_names[12], n.final_links[12]) + '\n'
                             +hlink(n.popular_names[13], n.final_links[13]) + '\n'
                             +hlink(n.popular_names[14], n.final_links[14]) + '\n'
                             +hlink(n.popular_names[15], n.final_links[15]) + '\n'
                             +hlink(n.popular_names[16], n.final_links[16]) + '\n'
                             +hlink(n.popular_names[17], n.final_links[17]) + '\n'
                             +hlink(n.popular_names[18], n.final_links[18]) + '\n'
                             +hlink(n.popular_names[19], n.final_links[19]) + '\n'
                             +hlink(n.popular_names[20], n.final_links[20]) + '\n'
                             +hlink(n.popular_names[21], n.final_links[21]) + '\n'
                             +hlink(n.popular_names[22], n.final_links[22]) + '\n'
                             +hlink(n.popular_names[23], n.final_links[23]) + '\n'
                             +hlink(n.popular_names[24], n.final_links[24]) + '\n'
                             +hlink(n.popular_names[25], n.final_links[25]) + '\n'
                             +hlink(n.popular_names[26], n.final_links[26]) + '\n'
                             +hlink(n.popular_names[27], n.final_links[27]) + '\n'
                             +hlink(n.popular_names[28], n.final_links[28]) + '\n'
                             +hlink(n.popular_names[29], n.final_links[29]) + '\n',
                             parse_mode='HTML')
        del sys.modules['new']









#обработка кнопок с ценами
@dp.callback_query_handler(text = 'bitcoin currency')
async def bitcoin_currency(call: CallbackQuery):
    import auth
    await call.message.answer("Цена Bitcoin: "+auth.bitcoin_data)
    del sys.modules['auth']
@dp.callback_query_handler(text = 'ethereum currency')
async def ethereum_currency(call: CallbackQuery):
    import auth
    await call.message.answer("Цена Ethereum: "+auth.ethereum_data)
    del sys.modules['auth']
@dp.callback_query_handler(text = 'tether currency')
async def tether_currency(call: CallbackQuery):
    import auth
    await call.message.answer("Цена Tether: "+auth.tether_data)
    del sys.modules['auth']
@dp.callback_query_handler(text = 'bnb currency')
async def bnb_currency(call: CallbackQuery):
    import auth
    await call.message.answer("Цена Bnb: "+auth.bnb_data)
    del sys.modules['auth']
@dp.callback_query_handler(text = 'xrp currency')
async def xrp_currency(call: CallbackQuery):
    import auth
    await call.message.answer("Цена Xrp: "+auth.xrp_data)
    del sys.modules['auth']
@dp.callback_query_handler(text = 'dogecoin currency')
async def dogecoin_currency(call: CallbackQuery):
    import auth
    await call.message.answer("Цена Dogecoin: "+auth.dogecoin_data)
    del sys.modules['auth']
#запуск бота в режиме нонстоп
executor.start_polling(dp, skip_updates=True)
