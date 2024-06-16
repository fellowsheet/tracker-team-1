from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Обычная кнопка назад чтобы вернуться к прошлому состоянию в FSM
def back_kb():
	button1 = KeyboardButton(text="Назад")

	keyboard = ReplyKeyboardMarkup(
		keyboard=[[button1]],
		resize_keyboard=True,
		one_time_keyboard=True,)
    
	return keyboard