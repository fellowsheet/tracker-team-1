from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart


router = Router(name=__name__)


@router.message(CommandStart)
async def start_handler(message: Message):
	await message.reply(text=message.chat.id)
