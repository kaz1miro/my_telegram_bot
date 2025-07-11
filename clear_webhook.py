import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

bot.remove_webhook()

print("Webhook удален!")