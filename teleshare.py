import telebot
from telebot import types

token = '5475470333:AAEUfdtCwGzSgqcErBKR8WCsnSgqqS5TH0c'
bot = telebot.TeleBot(token)


# command /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "haloooo, ada yang bisa saya bantu?")


# command untuk trigger send contanct
@bot.message_handler(commands=['contact'])
def share(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    reg_button = types.KeyboardButton(text="bagikan kontak anda", request_contact=True)
    keyboard.add(reg_button)
    bot.send_message(message.from_user.id, "Bagikan kontak anda", reply_markup=keyboard)


# content_types untuk share contact
@bot.message_handler(content_types=['contact'])
def contact(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.from_user.id,
                     "Nama: " + message.from_user.first_name + "\r\nTelepon: " + message.contact.phone_number,
                     reply_markup=markup)


# command untuk trigger share location
@bot.message_handler(commands=['sendloc'])
def sendloc(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    reg_button = types.KeyboardButton(text="bagikan lokasi anda", request_location=True)
    keyboard.add(reg_button)
    bot.send_message(message.from_user.id, "Bagikan lokasi anda", reply_markup=keyboard)


# content_types untuk share location
@bot.message_handler(content_types=['location'])
def location(message):
    userid = message.from_user.id
    lat = message.location.latitude
    lon = message.location.longitude
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_location(userid, lat, lon)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    chat = message.text
    bot.reply_to(message, "Kamu mengirim chat: '" + str(chat) + "'")


if __name__ == '__main__':
    bot.polling(none_stop=True)
