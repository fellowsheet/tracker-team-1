from aiogram import Router, F

from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states.create_task import CreateTask
from keyboards.reply.main_kb import main_kb
from keyboards.reply.back import back_kb
from keyboards.reply.back_or_further_kb import back_or_further_kb


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
	

# Переход назад к состоянию "description"
@router.message(CreateTask.responsible_person, F.text == 'Назад')
async def responsible_person_task_back(message: Message, state: FSMContext):
	await state.set_state(CreateTask.description)
	await message.answer(
		text='Опишите задачу.',
		reply_markup=back_kb(),
		)
	

# Пропуск выбора исполнителя и переход к состоянию "tags"
@router.message(CreateTask.responsible_person, F.text == 'Дальше')
async def responsible_person_task_further(message: Message, state: FSMContext):
	await state.update_data(responsible_person=None)
	await state.set_state(CreateTask.tags)
	await message.answer(
		text='Напишите теги этой задачи через пробел.',
		reply_markup=back_kb(),
		)
	

# Переход к следующему состоянию "tags" если пользователь ввел корректного исполнителя
@router.message(CreateTask.responsible_person, F.text)
async def responsible_person_task(message: Message, state: FSMContext):
	await state.set_state(CreateTask.tags)
	await state.update_data(responsible_person=message.text)
	await message.answer(
		text='Напишите теги этой задачи через пробел.',
		reply_markup=back_kb(),
		)
	

# Предупреждение пользователя о том что надо ввести корректного исполнителя
# и так же не пропускает пользователя дальше
@router.message(CreateTask.responsible_person)
async def responsible_person_task_missklick(message: Message):
	await message.answer(
		text='Я вас не понял, напишите пожалуйста корректного исполнителя или пропустите данный этап.!',
		reply_markup=back_or_further_kb(),
		)