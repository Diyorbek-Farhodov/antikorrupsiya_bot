from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.chat_action import ChatActionSender
from aiogram import Bot
from asyncio import sleep


async def command_start_answer(message: Message, bot: Bot):
    async with ChatActionSender.typing(message.from_user.id, bot):
        await sleep(2)
        await message.answer(
            "Assalomu alaykum. Navoiy Davlat Konchilik va Texnologiyalar Universitetining"
            " Korrupsiyaga qarshi kurashish bo'limi botiga Xush kelibsiz. "
            "Sizga qanday yordam beraolamiz!"
        )





async def echo(message: Message, bot: Bot):
    async with ChatActionSender.typing(message.from_user.id, bot):
        await sleep(3)
        m = await message.forward(chat_id=1979184326)

        await bot.send_message(
            chat_id=1979184326,
            text="Foydalanuvchi sizga xabar yubordi istasangiz unga reply qilib javob berishingiz mumkin yoki ushbu tugmani bosing",
            reply_to_message_id=m.message_id,
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="Javob berish",
                            callback_data=f"suser:{message.from_user.id}:{message.message_id}",
                        )
                    ]
                ]
            ),
        )
        await message.answer("Xabaringiz adminga yuborildi. Tez orada Javob beramiz")


#
