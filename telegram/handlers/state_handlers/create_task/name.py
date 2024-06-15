from aiogram import Router, F

from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, any_state

from states.create_task import CreateTask
from keyboards.reply.main_kb import main_kb
from keyboards.reply.back import back_kb


router = Router(name=__name__)


@router.message(F.text == 'Создать задачу', default_state)
async def create_task_start(message: Message, state: FSMContext) -> None:
	await state.set_state(CreateTask.name)
	await message.answer(
		text='Напишите название задачи.\n'
			 'Если вы хотите завершить, напишите /cancel команду.',
		reply_markup=back_kb(),
		)
	

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
	

@router.message(CreateTask.name, F.text == 'Назад')
async def name_task_back(message: Message, state: FSMContext):
	await message.answer(
		text='Тогда в другой раз.',
		reply_markup=main_kb(),
		)
	await state.clear()


@router.message(CreateTask.name, F.text)
async def name_task(message: Message, state: FSMContext):
	await state.set_state(CreateTask.description)
	await state.update_data(name=message.text)
	await message.answer(
		text='Опишите задачу.',
		reply_markup=back_kb()
		)


@router.message(CreateTask.name)
async def name_task_missklick(message: Message, state: FSMContext):
	await message.answer(
		text='Я вас не понял, напишите пожалуйста название задачи!',
		reply_markup=back_kb(),
		)
