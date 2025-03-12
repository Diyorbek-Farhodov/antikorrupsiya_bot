# from aiogram import Bot
# from aiogram.types import Message
#
# async def admin_message(message: Message, bot: Bot):
#     if message.reply_to_message:
#         # Forward qilingan xabar bor yoki yo'qligini tekshiramiz
#         if message.reply_to_message.forward_from:
#             await message.copy_to(chat_id=message.reply_to_message.forward_from.id)
#             await message.answer("✅ Sizning xabaringiz foydalanuvchiga yuborildi")
#         else:
#             await message.answer("❌ Bu xabar forward qilingan emas yoki foydalanuvchi IDsi mavjud emas")
#     else:
#         await message.answer("❗ Kimgadur xabar yozmoqchi bo'lsangiz, reply qilib yuboring")


from aiogram import Bot
from aiogram.types import Message

async def admin_message(message: Message, bot: Bot):
    if message.reply_to_message:
        # Xabar forward qilinganidan tekshirish
        user_id = None
        if message.reply_to_message.forward_from:
            user_id = message.reply_to_message.forward_from.id
        else:
            user_id = message.reply_to_message.from_user.id

        try:
            await bot.send_message(chat_id=user_id, text=message.text)
            await message.answer("✅ Sizning xabaringiz foydalanuvchiga yuborildi")
        except Exception as e:
            await message.answer(f"❌ Xatolik yuz berdi: {str(e)}")
    else:
        await message.answer("❗ Kimgadur xabar yozmoqchi bo'lsangiz, reply qilib yuboring")
