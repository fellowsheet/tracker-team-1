from aiogram import Router, F

from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states.create_task import CreateTask
from keyboards.reply.main_kb import main_kb
from keyboards.reply.back_kb import back_kb
from keyboards.reply.priority_kb import priority_kb
from keyboards.reply.states_kb import state_kb


router = Router(name=__name__)


# Один из вариантов выхода из машины состояния, предупреждение об этой 
# команде написано при запуске состояния
@router.message(Command('cancel'))
@router.message(F.text == 'cancel')
async def cancel_handler(message: Message, state: FSMContext) -> None:
	current_state = await state.get_state()
	if current_state is None:
		await message.reply(
			text='Нечего отменять, но хорошо.',
			)
		return
	
	await state.clear()
	await message.answer(
		text='Состояние завершено.',
		reply_markup=main_kb(),
		)
	

# Переход назад к состоянию "tags"
@router.message(CreateTask.state, F.text == 'Назад')
async def state_task_back(message: Message, state: FSMContext):
	await state.set_state(CreateTask.tags)
	await message.answer(
		text='Напишите теги этой задачи через пробел.\n'
			 'Пример: bug python database',
		reply_markup=back_kb(),
		)
	

# Переход к следующему состоянию "proirity" если пользователь ввел корректное состояние # задачи (Новая задача)
@router.message(CreateTask.state, F.text == 'Новая задача')
async def state_task1(message: Message, state: FSMContext):
	await state.set_state(CreateTask.priority)
	await state.update_data(state=message.text)
	await message.answer(
		text='Выберите приоритетность задачи.',
		reply_markup=priority_kb(),
		)
	

# Переход к следующему состоянию "proirity" если пользователь ввел корректное состояние # задачи (В работе)
@router.message(CreateTask.state, F.text == 'В работе')
async def state_task2(message: Message, state: FSMContext):
	await state.set_state(CreateTask.priority)
	await state.update_data(state=message.text)
	await message.answer(
		text='Выберите приоритетность задачи.',
		reply_markup=priority_kb(),
		)
	

# Переход к следующему состоянию "proirity" если пользователь ввел корректное состояние # задачи (На проверке)
@router.message(CreateTask.state, F.text == 'На проверке')
async def state_task3(message: Message, state: FSMContext):
	await state.set_state(CreateTask.priority)
	await state.update_data(state=message.text)
	await message.answer(
		text='Выберите приоритетность задачи.',
		reply_markup=priority_kb(),
		)
	

# Переход к следующему состоянию "proirity" если пользователь ввел корректное состояние # задачи (Готово)
@router.message(CreateTask.state, F.text == 'Готово')
async def state_task4(message: Message, state: FSMContext):
	await state.set_state(CreateTask.priority)
	await state.update_data(state=message.text)
	await message.answer(
		text='Выберите приоритетность задачи.',
		reply_markup=priority_kb(),
		)
	

# Переход к следующему состоянию "proirity" если пользователь ввел корректное состояние # задачи (Баги)
@router.message(CreateTask.state, F.text == 'Баги')
async def state_task5(message: Message, state: FSMContext):
	await state.set_state(CreateTask.priority)
	await state.update_data(state=message.text)
	await message.answer(
		text='Выберите приоритетность задачи.',
		reply_markup=priority_kb(),
		)
	

# Предупреждение пользователя о том что надо ввести корректное состояние задачи
# и так же не пропускает пользователя дальше
@router.message(CreateTask.state)
async def state_task_missklick(message: Message):
	await message.answer(
		text='Я вас не понял, выберите пожалуйста одно из состояний!',
		reply_markup=state_kb(),
		)