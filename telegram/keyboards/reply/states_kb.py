from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def state_kb():
	button1 = KeyboardButton(text="Новая задача")
	button2 = KeyboardButton(text="В работе")
	button3 = KeyboardButton(text="На проверке")
	button4 = KeyboardButton(text="Готово")
	button5 = KeyboardButton(text="Баги")
	button6 = KeyboardButton(text="Назад")

	keyboard = ReplyKeyboardMarkup(
		keyboard=[[button1], [button2], [button3], [button4], [button5], [button6]],
		resize_keyboard=True,
		one_time_keyboard=True,)
    
	return keyboard