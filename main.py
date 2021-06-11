import logging
from telegram.ext import *
import responses

API_KEY = '1813091058:AAHPP8X5k_yJnHnFfbewUgvABolvrp-KUT4'


def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot. What\'s up?')


def help_command(update, context):
    update.message.reply_text('Try typing anything and I will do my best to respond!')


def custom_command(update, context):
    update.message.reply_text('This is a custom command, you can add whatever text you want here.')


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response
    response = responses.get_response(text)
    update.message.reply_text(response)


def error(update, context):

    logging.error(f'Update {update} caused error {context.error}')



if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher


    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))


    dp.add_handler(MessageHandler(Filters.text, handle_message))


    dp.add_error_handler(error)


    updater.start_polling(1.0)
    updater.idle()

