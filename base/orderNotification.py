import asyncio
from telegram import Bot

async def send_welcome_message_async(user_name):
    print("Calling---------------------")
    TELEGRAM_CHAT_ID = '-1001877500762'
    BOT_TOKEN = '6591914802:AAGTWKCa4X90NPO_xO1OvcGC6M2pNy0Y0Ao'
    bot = Bot(token=BOT_TOKEN)
    message = "You have One New Order From "+ str(user_name)
    print("Calling---------------------")
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)





