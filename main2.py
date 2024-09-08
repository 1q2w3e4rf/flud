import telebot
from telebot import types
from db import DB
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

db = DB()

users = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Приветствую! Введите название вашего флуда в моно ")
    bot.register_next_step_handler(message, get_text)

def get_text(message):
    users[message.chat.id] = {}
    users[message.chat.id]['name'] = message.text
    bot.send_message(message.chat.id, 'Теперь ссылку на инфо канал')
    bot.register_next_step_handler(message, get_text2)

def get_text2(message):
    users[message.chat.id]['link'] = message.text
    bot.send_message(message.chat.id, 'Ссылку на лайф канал')
    bot.register_next_step_handler(message, get_text3)

def get_text3(message):
    users[message.chat.id]['link2'] = message.text
    bot.send_message(message.chat.id, 'И теперь юз следящего')
    bot.register_next_step_handler(message, get_text4)

def get_text4(message):
    users[message.chat.id]['link3'] = message.text
    db.save_user(message.chat.id, users[message.chat.id]['name'], users[message.chat.id]['link'], users[message.chat.id]['link2'], users[message.chat.id]['link3'])
    bot.send_message(message.chat.id, get_text5(message))
def get_text5(message):
    users[message.chat.id]['link3'] = message.text
    bot.send_message(1625771168, f"Название флуда: {users[message.chat.id]['name']} submitted the following data:\nСсылка номер 1: {users[message.chat.id]['link']}\nСсылка 2: {users[message.chat.id]['link2']}\nЮз владельца: {users[message.chat.id]['link3']}")

bot.infinity_polling()
