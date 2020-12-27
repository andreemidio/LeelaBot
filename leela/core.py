from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from leela.messageHandlers import messages
import os

TOKEN = '1271856756:AAE9QiL22JIgdWIxWqM4qzAJL9XlrmUm6ug'


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                                    text="Oi, Eu sou Leela! Já tem seu chip de profissão?")

def main():
    PORT = int(os.environ.get('PORT', 5000))
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    #updater.start_webhook(listen="0.0.0.0",
    #                       port=int(PORT),
    #                       url_path=TOKEN)
    #updater.bot.setWebhook('https://leela-bot.herokuapp.com/' + TOKEN)

    echo_handler = MessageHandler(Filters.text & (~Filters.command), messages.echo)
    dispatcher.add_handler(echo_handler)
    sys_handler = MessageHandler(Filters.status_update, messages.empty_message)
    dispatcher.add_handler(sys_handler)

    updater.start_polling()

    updater.idle()