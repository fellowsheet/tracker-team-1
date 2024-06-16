from aiogram import Router, F

from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states.create_task import CreateTask
from keyboards.reply.main_kb import main_kb
from keyboards.reply.back_kb import back_kb
from keyboards.reply.states_kb import state_kb
from keyboards.reply.priority_kb import priority_kb


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
	

# Переход назад к состоянию "state"
@router.message(CreateTask.priority, F.text == 'Назад')
async def proirity_task_back(message: Message, state: FSMContext):
	await state.set_state(CreateTask.state)
	await message.answer(
		text='Выберите состояние задачи.',
		reply_markup=state_kb(),
		)
	

# Переход к следующему состоянию "deadline_date" если пользователь ввел корректный приоритет задачи (Low)
@router.message(CreateTask.priority, F.text == 'Low')
async def priority_task1(message: Message, state: FSMContext):
	await state.set_state(CreateTask.deadline_date)
	await state.update_data(priority=message.text)
	await message.answer(
		text='Напишите дедлайн задачи в формате 31-12-2012',
		reply_markup=back_kb(),
	)


# Переход к следующему состоянию "deadline_date" если пользователь ввел корректный приоритет задачи (Normal)
@router.message(CreateTask.priority, F.text == 'Normal')
async def priority_task2(message: Message, state: FSMContext):
	await state.set_state(CreateTask.deadline_date)
	await state.update_data(priority=message.text)
	await message.answer(
		text='Напишите дедлайн задачи в формате 31-12-2012',
		reply_markup=back_kb(),
	)


# Переход к следующему состоянию "deadline_date" если пользователь ввел корректный приоритет задачи (Major)
@router.message(CreateTask.priority, F.text == 'Major')
async def priority_task3(message: Message, state: FSMContext):
	await state.set_state(CreateTask.deadline_date)
	await state.update_data(priority=message.text)
	await message.answer(
		text='Напишите дедлайн задачи в формате 31-12-2012',
		reply_markup=back_kb(),
	)


# Переход к следующему состоянию "deadline_date" если пользователь ввел корректный приоритет задачи (Critical)
@router.message(CreateTask.priority, F.text == 'Critical')
async def priority_task4(message: Message, state: FSMContext):
	await state.set_state(CreateTask.deadline_date)
	await state.update_data(priority=message.text)
	await message.answer(
		text='Напишите дедлайн задачи в формате 31-12-2012',
		reply_markup=back_kb(),
	)


# Предупреждение пользователя о том что надо выбрать одно из приоритетов
# и так же не пропускает пользователя дальше
@router.message(CreateTask.priority)
async def priority_task_missklick(message: Message):
	await message.answer(
		text='Я вас не понял, выберите пожалуйста приоритет задачи!',
		reply_markup=priority_kb(),
		)