from aiogram import Router, F
from aiogram.filters import CommandStart
from . import user, admin
from .states import Form


router = Router()

router.message.register(user.command_start_answer, CommandStart())
router.message.register(user.echo, F.from_user.id != 1979184326)
router.callback_query.register(admin.admin_callback, F.data.startswith("suser"))
router.message.register(admin.get_admin_message, Form.get_admin_message)
router.message.register(admin.admin_message)

