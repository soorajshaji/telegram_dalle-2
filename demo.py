import telebot
import openai

openai.api_key = ""
BOT_TOKEN = ""

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler()
def handler(message):
    bot.send_message(message.chat.id, "Creating image...")
    
    response = openai.Image.create(
    prompt=message.text,
    n=1,
    size="256x256"
    )
    bot.send_photo(message.chat.id, response['data'][0]['url'])
  
bot.infinity_polling()