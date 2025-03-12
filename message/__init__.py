from aiogram import Router, F
from aiogram.filters import CommandStart
from . import user, admin


router = Router()
router.message.register(user.command_start_answer, CommandStart())
router.message.register(user.echo, F.from_user.id != 1979184326)
router.message.register(admin.admin_message)

