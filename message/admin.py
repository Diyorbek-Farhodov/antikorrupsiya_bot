from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from .states import Form


async def admin_message(message: Message):
    if message.reply_to_message:
        if message.reply_to_message.forward_from:
            chat_id = message.reply_to_message.forward_from.id
            await message.copy_to(chat_id=chat_id)
            await message.answer("✅ Sizning xabaringiz foydalanuvchiga yuborildi")
        else:
            await message.answer(
                "❗ Bu xabar boshqa foydalanuvchidan oldinga yuborilmagan."
            )
    else:
        await message.answer(
            "❗ Kimgadur xabar yozmoqchi bo'lsangiz, reply qilib yuboring"
        )


async def admin_callback(call: CallbackQuery, state: FSMContext):
    data = call.data.split(":")
    chat_id = data[1]
    message_id = data[2]

    await state.update_data(chat_id=chat_id, message_id=message_id)
    await call.message.answer("Xabar yozing:")
    await state.set_state(Form.get_admin_message)


async def get_admin_message(message: Message, state: FSMContext):
    data = await state.get_data()
    chat_id = data.get("chat_id")
    message_id = data.get("message_id")

    await message.send_copy(chat_id=chat_id, reply_to_message_id=message_id)
    await message.answer("✅ Sizning xabaringiz foydalanuvchiga yuborildi")
