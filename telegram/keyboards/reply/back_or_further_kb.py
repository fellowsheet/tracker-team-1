from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def back_or_further_kb():
	button1 = KeyboardButton(text="Назад")
	button2 = KeyboardButton(text="Дальше")

	keyboard = ReplyKeyboardMarkup(
		keyboard=[[button2], [button1]],
		resize_keyboard=True,
		one_time_keyboard=True,)
    
	return keyboard