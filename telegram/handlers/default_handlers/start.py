from aiogram import Router

from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards.reply.main_kb import main_kb


router = Router(name=__name__)


# Start команда
@router.message(CommandStart())
async def start_handler(message: Message):
	await message.reply(
		text=f"Hello, {message.from_user.first_name}!",
		reply_markup=main_kb()
		)
