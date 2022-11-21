import telebot
bot = telebot.TeleBot('ааа')
from telebot import types

def make_dict(message):
    from re import sub
    strings = message.text.split()
    words = {}
    pretext = ['и', 'да', 'ни', 'тоже', 'также', 'а', 'но', 'да', 'однако', 'зато', 'же', 'или', 'либо', 'то', 'каe', 'хотя', 'не', 'что', 'чтобы', 'будто', 'когда', 'пока', 'едва', 'если', 'раз', 'ибо', 'чтобы', 'дабы', 'хотя', 'хоть', 'пускай', 'как', 'словно', 'кто', 'что', 'каков', 'который', 'куда', 'откуда', 'где', 'сколько', 'почему', 'зачем', 'как']
    for i in strings:
        if sub("[^а-яА-Я-]", '', i).lower() not in list(words.keys()) and sub("[^а-яА-Я]", '', i).lower() != '' and i not in pretext:
             words[sub("[^а-яА-Я-]", '', i).lower()] = 1
        elif sub("[^а-яА-Я-]", '', i).lower() in list(words.keys()):
             words[sub("[^а-яА-Я-]", '', i).lower()] += 1
        else:
            pass
    response = f'В тексте {len(words)} слов\n'
    words = {k: v for k, v in sorted(words.items(), key=lambda item: item[1], reverse=True)}
    for k,v in words.items():
        response +=(f'Слово "{k}" встречается {v} раз(а)\n')
        if v == max(words.values()):
            response += ('    Это самое частовстречающееся слово\n')
    bot.send_message(message.from_user.id, response)

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Введите какой-нибудь русский текст");
        bot.register_next_step_handler(message, make_dict);
    else:
        bot.send_message(message.from_user.id, 'Напишите /reg');


bot.polling(none_stop=False, interval=0)

