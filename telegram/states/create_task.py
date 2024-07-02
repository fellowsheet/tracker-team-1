from aiogram.fsm.state import State, StatesGroup


# FSM для создания задачи
class CreateTask(StatesGroup):
	name = State()
	description = State()
	worker = State()
	tags = State()
	status = State()
	priority = State()
	deadline = State()