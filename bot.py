import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

response = requests.get("https://www.google.com")
print(response.status_code)

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with the API token you got from the BotFather
TOKEN = '5886595251:AAGcR2lD89FWjFzmQ1h28cT7uThnUhCg-qk'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to the Weather Bot! Type /temperature to get the current temperature.")

def get_temperature(update: Update, context: CallbackContext) -> None:
    city = "Bucharest"  # Replace with the desired city name, e.g., "London", "New York", etc.
    url = f"https://wttr.in/{city.replace(' ', '+')}?format=%t"

    response = requests.get(url)
    if response.status_code == 200:
        temperature = response.text.strip()
        update.message.reply_text(f"The current temperature in {city} is {temperature}.")
    else:
        update.message.reply_text("Failed to fetch weather data. Please try again later.")

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("temperature", get_temperature))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
