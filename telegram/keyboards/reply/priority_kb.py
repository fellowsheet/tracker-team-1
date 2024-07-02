from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Кнопки с приоритетами для состояния (priority)
def priority_kb():
	button1 = KeyboardButton(text="Low")
	button2 = KeyboardButton(text="Normal")
	button3 = KeyboardButton(text="Hight")
	button4 = KeyboardButton(text="Назад")


	keyboard = ReplyKeyboardMarkup(
		keyboard=[[button1], [button2], [button3], [button4]],
		resize_keyboard=True,
		one_time_keyboard=True,)
    
	return keyboard