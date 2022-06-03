from telegram.ext import Updater, CommandHandler
# Импортируем нужные компоненты + CommandHandler - обработчик запросов

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(update, context):
    # Update - Это то, что пришло к нам из телеграмма
    # Context - это специальная штука, с помощбю которой мы передаем команды боту, что нужно сделать
    print("Вызван /start")


def main():
    mybot = Updater("5324680041:AAEivf8O2K2-cKNccpUaOOaSCF_PZcc5cIc", use_context=True, request_kwargs=PROXY)
    # Это ключ нашего бота. контекст нужна для того, чтобы не было проблем с проходящей сейчас отладкой на стороне телеграма. Request нужен для того, чтобы запустить прокси

    dp = mybot.dispatcher
    # Для удобства кода (чтобы постоянно не писать mybot.dispatcher), я задаю переменную dp и присваиваю ей значение mybot.dispatcher

    dp.add_handler(CommandHandler("start", greet_user))
    # Когда с телеграма приходит обновление, код проверяет его по этой(этим) строкам и ищет, задан ли обработчик для введенной команды
    # Добавляю к диспетчеру обработчик (handler) и говорю ему, какую команду нужно обработать (commandhandler). Далее даю имя функции, которую задам отдельно




    mybot.start_polling()
    # здесь бот идет в телеграм
    mybot.idle()
    # это для того, чтобы обращения к телеграму не останавливались. Типа While

main()

