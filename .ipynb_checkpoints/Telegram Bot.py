import telebot


with open('../API_KEY.txt') as f:
    key = f.read()

bot = telebot.TeleBot(key)

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Hey, welcome to my Bot")

bot.polling()
