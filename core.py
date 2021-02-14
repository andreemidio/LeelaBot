import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from leela.messageHandlers import messages
from request import DontStopmeNOW
from settings import TOKEN

PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Oi, Eu sou Leela! Já tem seu chip de profissão?")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    DontStopmeNOW()
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    echo_handler = MessageHandler(Filters.text & (~Filters.command), messages.echo)
    dispatcher.add_handler(echo_handler)
    sys_handler = MessageHandler(Filters.status_update, messages.empty_message)
    dispatcher.add_handler(sys_handler)
    dispatcher.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://leela-bot.herokuapp.com/' + TOKEN)

    updater.idle()

    # updater.start_polling()

    # updater.idle()


if __name__ == "__main__":
    main()
