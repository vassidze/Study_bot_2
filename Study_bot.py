import telebot
from telebot import types

#from telebot import apihelper
#apihelper.proxy = {'http':'http://89.46.238.133'}
Token = '1234251686:AAEDDfcaP3NhTLryQEFk8YU07Ypf4N91tDg'
bot = telebot.TeleBot(Token)

infinite = 'test'

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text == "Привет" or message.text == "Флюгегехаймен" or message.text == "Бля" or message.text == "Полундра":

        bot.send_message(message.from_user.id, "Салам, ща все будет")

        keyboard = types.InlineKeyboardMarkup()

        key_rus = types.InlineKeyboardButton(text='Мантра', callback_data='infinite')

        keyboard.add(key_rus)

        key_mat = types.InlineKeyboardButton(text='Материалы', callback_data='materials')

        keyboard.add(key_mat)
    
        bot.send_message(message.from_user.id, text='Шо выберешь, добрый молодец или прекрасная царевна?', reply_markup=keyboard)
        
    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Напиши привет или слово, описывающее сессию")

    else:

        bot.send_message(message.from_user.id, "Ничего не понятно. Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)

def callback_worker(call):

    if call.data == "infinite": 
        bot.send_message(call.message.chat.id, infinite)
   
    elif call.data == "materials":
        kin = "https://drive.google.com/drive/u/0/folders/1STmW-IiL1dB9mHoGC9_AaaBLXGpGDFih"
        eng = "https://drive.google.com/drive/u/0/folders/1ZvWWl6v8wHjKE269B3qgyuqhHQt__OFP"
        bha = "https://drive.google.com/drive/u/0/folders/1dr0nZcEEVFExp0M5f15S01DQPo3U6lEf"
        gen = "https://drive.google.com/drive/u/0/folders/1BUgcLFIXJBtKFEGH0-oc1pUYPUGZhnKK"
        mic = "https://drive.google.com/drive/u/0/folders/19UVmcl3fKjdOtJMIZYe-aCS_N1x--ISu"
        mat = "Кинетика:" + ' ' + kin + '\n' + "Английский:" + ' ' + eng + '\n' + "Биохимия:" + ' ' + bha + '\n' + "Микра:" + ' ' + mic + '\n' + "Генинж:" + ' ' + gen + '\n'
        bot.send_message(call.message.chat.id, mat)

bot.polling(none_stop=True, interval=0)
