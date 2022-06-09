from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def sum_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')

updater = Updater("YOUR_TOKEN")

updater.dispatcher.add_handler(CommandHandler("sum", sum_command))

print('server start')
updater.start_polling()
updater.idle()