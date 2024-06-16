from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def priority_kb():
	button1 = KeyboardButton(text="Low")
	button2 = KeyboardButton(text="Normal")
	button3 = KeyboardButton(text="Major")
	button4 = KeyboardButton(text="Critical")
	button5 = KeyboardButton(text="Назад")


	keyboard = ReplyKeyboardMarkup(
		keyboard=[[button1], [button2], [button3], [button4], [button5]],
		resize_keyboard=True,
		one_time_keyboard=True,)
    
	return keyboard