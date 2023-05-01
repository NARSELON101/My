import telebot
from telebot.types import *
import webbrowser
import sqlite3

bot = telebot.TeleBot('6067863967:AAHMOyi_djswFmULeAVKG7D0nXu-dUkY1lY')
name = None
@bot.message_handler(commands=["start"])
def start(message):
    conn = sqlite3.connect("database.sql")
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, "Введите имя")
    bot.register_next_step_handler(message, user_name)



def user_name(message):
    global name
    name = message.text.rstrip()
    bot.send_message(message.chat.id, "Введите пароль")
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.rstrip()

    conn = sqlite3.connect("database.sql")
    cur = conn.cursor()

    cur.execute('INSERT INTO users(name, pass) VALUES ("%s", "%s")' % (name, password))
    conn.commit()
    cur.close()
    conn.close()
    button = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("Вывести всех пользователей", callback_data="users")
    button.add(btn1)
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован', reply_markup=button)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect("database.sql")
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    info = ''
    for i in users:
        info += f"Имя: {i[1]} Пароль {i[2]}\n"
    bot.send_message(call.message.chat.id, "Список всех пользователей: \n%s" % info)
    cur.close()
    conn.close()

bot.polling(none_stop=True)