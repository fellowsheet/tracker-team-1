from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_kb():
	button1 = KeyboardButton(text="Создать задачу")

	keyboard = ReplyKeyboardMarkup(
		keyboard=[[button1]],
		resize_keyboard=True,
		one_time_keyboard=True,)
    
	return keyboard