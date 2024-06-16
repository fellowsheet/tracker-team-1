from aiogram import Router, F

from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states.create_task import CreateTask
from keyboards.reply.main_kb import main_kb
from keyboards.reply.back_kb import back_kb
from keyboards.reply.back_or_further_kb import back_or_further_kb
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
	

# Переход назад к состоянию "responsible_person"
@router.message(CreateTask.tags, F.text == 'Назад')
async def tags_task_back(message: Message, state: FSMContext):
	await state.set_state(CreateTask.responsible_person)
	await message.answer(
		text='Напишите ответственного человека или пропустите данный этап.',
		reply_markup=back_or_further_kb(),
		)
	

# Переход к следующему состоянию "state" если пользователь ввел корректного теги
@router.message(CreateTask.tags, F.text)
async def tags_task(message: Message, state: FSMContext):
	await state.set_state(CreateTask.state)
	await state.update_data(
		tags=' '.join(["#" + tag.strip() for tag in message.text.split(' ')]))
	await message.answer(
		text='Выберите состояние задачи.',
		reply_markup=state_kb(),
		)
	

# Предупреждение пользователя о том что надо ввести корректного теги
# и так же не пропускает пользователя дальше
@router.message(CreateTask.tags)
async def tags_task_missklick(message: Message):
	await message.answer(
		text='Я вас не понял, напишите пожалуйста корректного теги через пробел!\n'
			 'Пример: bug python database',
		reply_markup=back_kb(),
		)