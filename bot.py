import telebot
from telebot import types # для указание типов
import confid

bot = telebot.TeleBot(confid.token) # токен лежит в файле config.py

@bot.message_handler(commands=['start']) #создаем команду
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Чек - лист")
    btn2 = types.KeyboardButton("Мои курсы, но пока каналы в тг")
    btn3 = types.KeyboardButton("Записаться на распаковку")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Чек - лист"):
        bot.send_message(message.chat.id, text="Тут пока ничего нет")
    elif (message.text == "Мои курсы, но пока каналы в тг"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Мой тг канал")
        btn2 = types.KeyboardButton("Канал с ассистентами")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выбери что интересно", reply_markup=markup)

    elif (message.text == "Записаться на распаковку"):
        bot.send_message(message.chat.id, text="Тут должна быть распаковка")

    elif (message.text == "Канал с ассистентами"):
        markup = types.InlineKeyboardMarkup()
        button2 = types.InlineKeyboardButton("Мой канал", url='https://t.me/+ydkSS4aIedw1Nzk6')
        markup.add(button2)
        bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на мой сайт)".format(message.from_user), reply_markup=markup)

    elif message.text == "Мой тг канал":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Мой канал", url='https://t.me/NataKim_life')
        markup.add(button1)
        bot.send_message(message.chat.id,"Привет, {0.first_name}! Нажми на кнопку и перейди на мой сайт)".format(message.from_user),reply_markup=markup)

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Чек - лист")
        button2 = types.KeyboardButton("Мои курсы, но пока каналы в тг")
        button3 = types.KeyboardButton("Записаться на распаковку")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


bot.polling(none_stop=True)