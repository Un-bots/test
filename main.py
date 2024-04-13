from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(name)

# Telegram Bot Token (Replace 'YOUR_BOT_TOKEN' with your actual bot token)
TOKEN = '7166526946:AAHFEcSoXZBosmIDdhErMBehT8JcIHNPjO4'

# Create an Updater object
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Command handler for promoting the bot owner in groups
def promote_owner(update, context):
    user_id = update.message.from_user.id
    chat_id = update.message.chat_id

    # Check if the bot owner triggered the command
    if user_id == 5442167219:
        # Check if the bot is currently in a group
        if update.message.chat.type == 'group':
            context.bot.promote_chat_member(chat_id, user_id, can_change_info=True, can_delete_messages=True, can_restrict_members=True, can_invite_users=True, can_pin_messages=True)
            context.bot.send_message(chat_id=chat_id, text="Bot owner has been promoted in this group.")
        else:
            context.bot.send_message(chat_id=chat_id, text="This command can only be used in groups.")
    else:
        context.bot.send_message(chat_id=chat_id, text="Only the bot owner can use this command.")

# Add command handler to the dispatcher
promote_owner_handler = CommandHandler('promote_owner', promote_owner)
dispatcher.add_handler(promote_owner_handler)

# Start the bot
updater.start_polling()
updater.idle()
