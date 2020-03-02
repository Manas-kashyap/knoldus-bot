from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import configparser
import logging
from telegram import ChatAction,ParseMode
from telegram.ext.dispatcher import run_async
from random import choice
import os

BOTNAME = 'KnoldusBot'

@run_async
def send_async(bot, *args, **kwargs):
    bot.sendMessage(*args, **kwargs)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)

config = configparser.ConfigParser()
config.read('bot.ini')


updater = Updater(token=config['BOT']['TOKEN'])
dispatcher = updater.dispatcher


def start(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text= '''
Hey!! I'm currently Working with Knoldus To hire me contact my admin
Use /help to get help''')


def website(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text=config['BOT']['website'])



def invitelink(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text=config['BOT']['invite_link'])



def twitter(bot,update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text=config['BOT']['twitter'])




	

def help(bot, update):
     bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
     bot.sendMessage(chat_id=update.message.chat_id, text='''Use one of the following commands
/invitelink - to get Knoldus Telegram group invite link
/website - to get Knoldus website link
/twitter - twitter link for Knoldus
''')


# Welcome a user to the chat
def welcome(bot, update):
    message = update.message
    chat_id = message.chat.id
    phrases = ['Hello {}! Welcome to {} .Please introduce yourself. Dont forget to read the chat rules using !rules command'.format(message.new_chat_member.first_name,message.chat.title),
               'Hi {}! Welcome to {} .let\'s start with introduction. Dont forget to read the chat rules using !rules command'.format(message.new_chat_member.first_name,message.chat.title)
               #'Hello {}! Welcome to {} .Please introduce yourself.'.format(message.new_chat_member.first_name,message.chat.title),
               #'Hello {}! Welcome to {} .Please introduce yourself.'.format(message.new_chat_member.first_name,message.chat.title),
               #'Hello {}! Welcome to {} .Please introduce yourself.'.format(message.new_chat_member.first_name,message.chat.title)
                ]
    text = choice(phrases)
    send_async(bot, chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)


def goodbye(bot, update):
    message = update.message
    chat_id = message.chat.id
    text = 'Goodbye, $username!'
    text = text.replace('$username',message.left_chat_member.first_name).replace('$title', message.chat.title)
    send_async(bot, chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)
	
def intro(bot, update):
    message = update.message
    chat_id = message.chat.id
    text = 'Hi everyone,I am a python bot working to serve Ilug-D.'
    send_async(bot, chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)	

def empty_message(bot, update):

    if update.message.new_chat_member is not None:
        # Bot was added to a group chat
        if update.message.new_chat_member.username == BOTNAME:
            return intro(bot, update)
        # Another user joined the chat
        else:
            return welcome(bot, update)

    # Someone left the chat
    elif update.message.left_chat_member is not None:
        if update.message.left_chat_member.username != BOTNAME:
            return goodbye(bot, update)


dispatcher.add_handler(CommandHandler('website', website))
dispatcher.add_handler(CommandHandler('facebook', facebok))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(MessageHandler([Filters.status_update], empty_message))
dispatcher.add_handler(CommandHandler('invitelink',invitelink))
dispatcher.add_handler(CommandHandler('mailinglist',mailinglist))
dispatcher.add_handler(CommandHandler('twitter',twitter))
dispatcher.add_handler(CommandHandler('meetuplink',meetuplink))
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('github',github))

updater.start_polling()
updater.idle()
