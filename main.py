import telebot
bot = telebot.TeleBot("")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_msg = "Hello! This bot gives you the information about Mark Kanafeev. Use /name - for name\n/linkedIn - for linkedIn\n/telegram - for telegram\n/cv - for cv\n/university - for university. Good luck."
    bot.reply_to(message, welcome_msg)

@bot.message_handler(commands=['cv'])
def cv(message):
    bot.reply_to(message, "https://www.linkedin.com/in/mark-kanafeev/overlay/1635504536112/single-media-viewer/?profileId=ACoAADhY-AwBKzVH8l6eKKKM_2KJM8NbchXPCXI")

@bot.message_handler(commands=['telegram'])
def telegram(message):
    bot.reply_to(message, "@poimidorka")

@bot.message_handler(commands=['linkedIn'])
def linkedIn(message):
    bot.reply_to(message, "https://www.linkedin.com/in/mark-kanafeev/")

@bot.message_handler(commands=['name'])
def name(message):
    bot.reply_to(message, "Mark Kanafeev")

@bot.message_handler(commands=['university'])
def university(message):
    bot.reply_to(message, "National Research Institute Higher School of Economics in Moscow")

@bot.message_handler(content_types=['text'])
def text(message):
    bot.reply_to(message, "To see the list of avaivable commands, use /help")

bot.infinity_polling()

