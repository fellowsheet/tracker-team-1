from aiogram import Router, F

from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from states.create_task import CreateTask
from keyboards.reply.main_kb import main_kb
from keyboards.reply.back_kb import back_kb


router = Router(name=__name__)


# В каждом состоянии будет кнопка "Назад" что бы пользователь мог 
# вернуться назад и изменить данные. Если пользователь дойдет до первого
# состояния и нажмёт кнопку "Назад", то он покинет FSM и вернётся в главное
# меню.
#
# Перехватывание кнопки и начало FSM машины
@router.message(F.text == 'Создать задачу', default_state)
async def create_task_start(message: Message, state: FSMContext) -> None:
	# 
	await state.set_state(CreateTask.name)
	await message.answer(
		text='Напишите название задачи.\n'
			 'Если вы хотите завершить, напишите /cancel команду.',
		reply_markup=back_kb(),
		)
	

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
	

# Выход из состояния есть пользователь нажал на кнопку "Назад"
@router.message(CreateTask.name, F.text == 'Назад')
async def name_task_back(message: Message, state: FSMContext):
	await message.answer(
		text='Тогда в другой раз.',
		reply_markup=main_kb(),
		)
	await state.clear()


# Переход к следующему состоянию если пользователь ввел корректный текст
@router.message(CreateTask.name, F.text)
async def name_task(message: Message, state: FSMContext):
	await state.set_state(CreateTask.description)
	await state.update_data(name=message.text)
	await message.answer(
		text='Опишите задачу.',
		reply_markup=back_kb()
		)


# Предупреждение пользователя о том что надо ввести корректное название
# и так же не пропускает пользователя дальше
@router.message(CreateTask.name)
async def name_task_missklick(message: Message):
	await message.answer(
		text='Я вас не понял, напишите пожалуйста корректное название задачи!',
		reply_markup=back_kb(),
		)
