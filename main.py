import telebot

TOKEN = "5943242364:AAEDa7ko4pgcCKnzSOw7WdvU8eYMH8OWD6M"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

number = 57

@bot.message_handler(commands=['start', '/start_game'])
def send_welcome(message):
    print(message.text)
    bot.reply_to(message, "Привет, я бот для игры в 'Угадай число'!\n"
                          "Я загадал число от 1 до 100.\n"
                          "Попробуй угадать:")


def all_messages(message):
    return True


@bot.message_handler(func=all_messages)
def handle_all_messages(message):
    guess = int(message.text)
    reply = ""
    if guess == number:
        reply = "Ты угадало мое число! Молодец!"
    elif guess > number:
        reply = "Mое число меньше!"
    else:
        reply = "Мое число больше!"
    bot.reply_to(message, reply)


bot.infinity_polling()
