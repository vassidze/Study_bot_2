import telebot
from telebot import types

#from telebot import apihelper
#apihelper.proxy = {'http':'http://89.46.238.133'}
Token = '1234251686:AAEDDfcaP3NhTLryQEFk8YU07Ypf4N91tDg'
bot = telebot.TeleBot(Token)


infinite = '''Ребята, проконтролируйте пожалуйста, что все всё заботали🤓, давайте выйдем из этого месяца с максимальным багажом знаний и полностью сделанным планом📈! Я понимаю, вы можете сказать мне, что ботать сейчас не обязательно, но что бы вы сказали в тот момент, когда бы уже держали листочек с вариантом на зачете? Давайте отнесемся ответственно к учебе не только перед собой, но и перед своими одногруппниками, мы все в одной группе💂‍♀, и каждый из нас является ее представителем, так что не подводите друг друга и делайте все добросовестно, мы одна семья и должны друг друга поддерживать. Я понимаю, что, наверное, слишком жалостливо отношусь к вашим загруженностям, но, надеюсь, вы понимаете, что в каком-то смысле, у других все так же: те де проблемы, те же чувства. Я работаю в лаборатории эволюционной геномики🐻🐼, одной из самых загруженных лаб, у меня в 2 раза больше нагрузки, чем у других студентов, но я безумно рад тому, что я учусь на ФББ, что я сейчас с вами, будьте так же благодарны всем своим трудностям, они развивают ваш характер и силу воли, не смотрите на преграды как на оправдание и ищите в этом новые возможности!! И еще, за эти полтора года устаканился такой режим, что большинство начинает ботать за неделю⏰ до экзамена, давайте потихоньку смещать этот временной промежуток, экзамен действительно помогает не забыть что-то сделать, но спустя полтора года вы должны были уже научиться на него не ориентироваться, так же как и правильно ботать к зачетам и кр, это очень облегчает сдачу и помогает вам осознать свои ошибки. Это то, что я хотел сказать, чтобы мы стали лучше, своего рода анкета однокурсникам📑, я вас всех очень люблю и очень хочу, чтобы мы действительно были близкими друг для друга друзьями, поэтому, пожалуйста, отнеситесь к моим словам максимально серьезно😔. Если вам есть, что сказать, все, что угодно, пожалуйста, не молчите, мне важно знать ваше мнение, будь что угодно, о себе, обо мне, о нас всех, только не молчите, не будьте равнодушны🌝🌚'''

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

