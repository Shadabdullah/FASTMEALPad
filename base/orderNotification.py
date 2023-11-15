import asyncio
from telegram import Bot

async def send_welcome_message_async(user_name):
  
    TELEGRAM_CHAT_ID = '-1001877500'
    BOT_TOKEN = '6591914802:'
    bot = Bot(token=BOT_TOKEN)
    message = "You have One New Order From "+ str(user_name)
   
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)





