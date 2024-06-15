from aiogram.fsm.state import State, StatesGroup


class CreateTask(StatesGroup):
	name = State()
	description = State()
	responsible_person = State()
	tags = State()
	state = State()
	proirity = State()
	deadline_date = State()