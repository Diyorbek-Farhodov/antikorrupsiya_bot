from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionSender
from aiogram import Bot
from asyncio import sleep

async def command_start_answer(message: Message, bot: Bot):
    async with ChatActionSender.typing(message.from_user.id, bot):
        await sleep(2)
        await message.answer("Assalomu alaykum")

async def echo(message: Message, bot : Bot):
    async with ChatActionSender.typing(message.from_user.id, bot):
        await sleep(3)
        await message.forward(chat_id=1979184326)
        await message.answer("Xabaringiz adminga yuborildi")
