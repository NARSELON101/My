import telebot
from telebot.types import *
import requests
import json
bot = telebot.TeleBot("6287726255:AAGfDA1ef_g4c-MX1ywKb-y5yZbvRlX2x2A")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, напиши название города")


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    try:
        res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ad30223a9c4569290fa16a775db0c5ea&lang=ru&units=metric")
        data = json.loads(res.text)
        bot.reply_to(message, f'Сейчас погода:  <b>{data["main"]["temp"]}</b> °C\nОщущается как:  <b>{data["main"]["feels_like"]}</b> °C\nВетер  <b>{data["wind"]["speed"] }</b> м/c', parse_mode="html")
    except:
        bot.reply_to(message, "Невозможно получить погоду в данный момент")
bot.polling(none_stop=True)