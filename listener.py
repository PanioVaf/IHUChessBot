# Copyright (C) 2020 Vafiadis Panagiotis
#
# Computer Science Department Faculty of Sciences - Campus of Kavala
# International Hellenic University
#
# MPhil in Advanced Technologies in Informatics and Computers
# Advanced Programming and Rich Internet Applications
#
# This is free software and you are welcome to redistribute it
# under certain conditions.
# Copyright (C) 2020 Vafiadis Panagiotis
#
# Computer Science Department Faculty of Sciences - Campus of Kavala
# International Hellenic University
#
# MPhil in Advanced Technologies in Informatics and Computers
# Advanced Programming and Rich Internet Applications
#
# This is free software and you are welcome to redistribute it
# under certain conditions.

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import os
import configparser
import re
import logging
import datetime
import users


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Hello I am a chessbot, please talk to me!")

    
def chessbot(update, context):
    user = update.effective_user
    user_id = str(user.id)
    logging.info("User with user_id = %s and name: %s" % (user_id, user.name))
    user = users.get_or_create_user(user_id)
    user.reply(update, context)

    
def start():
    """ Main program function. """
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.info("Starting Telegram Listener")

    config = configparser.ConfigParser()
    config.read('chessbot.conf')
    token = config['ACCOUNT']['Token']
    
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    chessbot_handler = MessageHandler(Filters.text & (~Filters.command), chessbot)
    
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(chessbot_handler)
    updater.start_polling()
    
        
if __name__ == "__main__":
    start()

