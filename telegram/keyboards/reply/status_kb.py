from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Кнопки с состояниями для состояния (status)
def status_kb():
	button1 = KeyboardButton(text="Done")
	button2 = KeyboardButton(text="In review")
	button3 = KeyboardButton(text="In progress")
	button4 = KeyboardButton(text="Pending")
	button5 = KeyboardButton(text="Назад")

	keyboard = ReplyKeyboardMarkup(
		keyboard=[[button1], [button2], [button3], [button4], [button5]],
		resize_keyboard=True,
		one_time_keyboard=True,)
    
	return keyboard