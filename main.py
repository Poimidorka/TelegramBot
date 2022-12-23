from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5953072951:AAGIh_69nBSJHmGv_jHvE25yYYD1QO24JTA",
                  use_context=True)  
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello, this bot gives information about Mark Kanafeev. Type /help for more")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("/name - for name\n/linkedIn - for linkedIn\n/telegram - for telegram\n/cvv - for cvv\n/university - for university\n")

def name(update: Update, context: CallbackContext):
    update.message.reply_text("Mark Kanafeev")

def linkedIn(update: Update, context: CallbackContext):
    update.message.reply_text("https://www.linkedin.com/in/mark-kanafeev/")

def telegram(update: Update, context: CallbackContext):
    update.message.reply_text("@poimidorka")

def cvv(update: Update, context: CallbackContext):
    update.message.reply_text("https://www.linkedin.com/in/mark-kanafeev/overlay/1635504536112/single-media-viewer/?profileId=ACoAADhY-AwBKzVH8l6eKKKM_2KJM8NbchXPCXI")

def university(update: Update, context: CallbackContext):
    update.message.reply_text("National Research Institute Higher School of Economics in Moscow")

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
    
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('name', name))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn))
updater.dispatcher.add_handler(CommandHandler('cvv', cvv))
updater.dispatcher.add_handler(CommandHandler('university', university))
updater.dispatcher.add_handler(CommandHandler('telegram', telegram))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
  
updater.start_polling()

