import requests
import main
import telebot
import json
from config import token
from main import result
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(token)

def create_main_menu():
    #Создание главного меню
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    buttons = [
        types.InlineKeyboardButton("Все игры со скидками", callback_data="game_sales"),
    ]
    
    # Распределяем кнопки по рядам
    for i in range(0, len(buttons), 2):
        if i + 1 < len(buttons):
            markup.add(buttons[i], buttons[i + 1])
        else:
            markup.add(buttons[i])
    
    return markup

#хахандлер сообщений

@bot.message_handler(commands=['start'])
def send_welcome(message):
    #Обработчик команды /start
    welcome_text = """
    Привет! Я бот-поисковик скидок steam (в будующем может и не только).

    Доступные команды:
    /start - Главное меню
    /game_sales - Все игры со скидками
    """
    
    bot.send_message(
        message.chat.id,
        welcome_text,
        reply_markup=create_main_menu()
    )

@bot.message_handler(commands=['menu']) #да вы задолбали просто
def show_menu(message):
    #обработчик команды /menu
    bot.send_message(
        message.chat.id,
        "Главное меню:",
        reply_markup=create_main_menu()
    )

@bot.message_handler(commands=['game_sales'])
def show_catalog(message):
    #обработчик команды /game_sales
    bot.send_message(
        message.chat.id,
        result
    )



#каллБэк хахандлеры

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    
    #обработчик всех каллБэк запросов
    chat_id = call.message.chat.id
    message_id = call.message.message_id
        
# вставте сюда чёнюдь
    if call.data == "game_sales":
        bot.answer_callback_query(call.id, "Кнопка нажата") 
        bot.send_message(
            call.message.chat.id,
            result
        )    

    


bot.infinity_polling()