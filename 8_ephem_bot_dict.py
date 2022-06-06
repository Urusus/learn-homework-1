"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""

import logging
from pydoc import plain
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(filename="bot.log", level=logging.INFO)
import Settings
import ephem

def greet_user(update, context):
    print("Вызван /start")
    print(update)
    update.message.reply_text("Здравствуй, пользователь")

def planet_info(update, context):
    print("Planet provided:")
    planet = update.message.text.split()[1]
    print(planet)
    
    
    planet_dict = {
      "Mercury": ephem.Mercury('2022/06/06'),
      "Venus": ephem.Venus('2022/06/06'),
      "Mars": ephem.Mars('2022/06/06'),
      "Jupiter": ephem.Jupiter('2022/06/06'),
      "Saturn": ephem.Saturn('2022/06/06'),
      "Uranus": ephem.Uranus('2022/06/06'),
      "Neptune": ephem.Neptune('2022/06/06')
      }
    
    constellation = ephem.constellation(planet_dict[planet])
    print(constellation)

    update.message.reply_text('Today this planet is in this constellation:')
    update.message.reply_text(str(constellation))

def main():
    mybot = Updater(Settings.TG_API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_info))
    
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()


