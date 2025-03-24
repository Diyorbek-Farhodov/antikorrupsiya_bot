from asyncio import run
from aiogram import Bot, Dispatcher
import message
from dotenv import load_dotenv
import os


load_dotenv()

db = Dispatcher()

CHAT_ID = int(os.getenv("CHAT_ID"))
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def startup_answer(bot: Bot):
    await bot.send_message(CHAT_ID, "✅ Bot ishga tushdi!")
    print("Bot ishlamoqda ...")

async def shutdown_answer(bot: Bot):
    await bot.send_message(CHAT_ID, "⛔ Bot ishdan to'xtadi!")
    print("Bot ishdan toxtadi !")

async def start():
    db.startup.register(startup_answer)
    db.shutdown.register(shutdown_answer)

    db.include_router(message.router)
    bot = Bot(token=BOT_TOKEN)
    await db.start_polling(bot, polling_timeout=1)

run(start())

