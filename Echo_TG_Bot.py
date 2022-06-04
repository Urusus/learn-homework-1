import logging
# импортирование модуля логирования для отслеживания ошибок. Принято располагать импортирование модулей вверху кода

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# Импортируем нужные компоненты + CommandHandler - обработчик запросов

logging.basicConfig(filename="bot.log", level=logging.INFO)
# Объясняется как и куда будем логировать
# filename="bot.log" - указываем название файла лога
# level= - уровень важности сообщений, которые меня интересуют. 
#   Debug - lowest level (every action/ step described)
#   INFO - important event
#   Warning - something to inform a user of (i.e. new patch, software version, etc)
#   Error - errors

import Settings

def greet_user(update, context):
    # Update - Это то, что пришло к нам из телеграмма
    # Context - это специальная штука, с помощбю которой мы передаем команды боту, что нужно сделать
    print("Вызван /start")
    # просто пишет в консоли текст. Но не отвечает пользователю в телеграме!
    print(update)
    # пишет в консоль информацию о пользователе, которую пересылает нам бот из телеграма
    update.message.reply_text("Здравствуй, пользователь")

def talk_to_me(update, context):
    text = update.message.text
    # update.message.text - it is the text from the user
    print(text)
    update.message.reply_text(text)
    # update.message.reply_text() sends reply to the user 

def main():
    mybot = Updater(Settings.TG_API_KEY, use_context=True)
    # Это ключ нашего бота. контекст нужна для того, чтобы не было проблем с проходящей сейчас отладкой на стороне телеграма. Request нужен для того, чтобы запустить прокси

    dp = mybot.dispatcher
    # Для удобства кода (чтобы постоянно не писать mybot.dispatcher), я задаю переменную dp и присваиваю ей значение mybot.dispatcher

    dp.add_handler(CommandHandler("start", greet_user))
    # Когда с телеграма приходит обновление, код проверяет его по этой(этим) строкам и ищет, задан ли обработчик для введенной команды
    # Добавляю к диспетчеру обработчик (handler) и говорю ему, какую команду нужно обработать (commandhandler). Далее даю имя функции, которую задам отдельно
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    # Диспетчер обработки текста, который набрал юзер

    logging.info("Бот стартовал")
    # Message for bot.log on the initiation of the bot
    mybot.start_polling()
    # здесь бот идет в телеграм
    mybot.idle()
    # это для того, чтобы обращения к телеграму не останавливались. Типа While

main()

