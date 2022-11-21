import telebot
bot = telebot.TeleBot('ааа')
from telebot import types
import requests

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Доступность какого сайта будем проверять? Введите url");
        bot.register_next_step_handler(message, check_site);
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');

def check_site(message):
    url = message.text
    try:
        response = requests.get(url)
        bot.send_message(message.from_user.id, f"Сайт {url} доступен {response.status_code}")
    except:
        bot.send_message(message.from_user.id, f"Сайт {url} недоступен")


bot.polling(none_stop=True, interval=0)