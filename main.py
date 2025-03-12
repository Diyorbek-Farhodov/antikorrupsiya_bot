from asyncio import run
from aiogram import Bot, Dispatcher
import message

bot = Bot(token="7301528891:AAEZq1uP8w69P7pFk7KYBQl6pLJJptOPSnU")
db = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(1979184326, "✅ Bot ishga tushdi!")
    print("Bot ishlamoqda")

async def shutdown_answer(bot: Bot):
    await bot.send_message(1979184326, "⛔ Bot ishdan to'xtadi!")
    print("Bot ishdan toxtadi")

async def start():
    db.startup.register(startup_answer)
    db.shutdown.register(shutdown_answer)

    db.include_router(message.router)

    await db.start_polling(bot, polling_timeout=1)

run(start())
