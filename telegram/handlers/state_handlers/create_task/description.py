from aiogram import Router, F

from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states.create_task import CreateTask
from keyboards.reply.main_kb import main_kb
from keyboards.reply.back_kb import back_kb
from keyboards.reply.back_or_further_kb import back_or_further_kb


router = Router(name=__name__)


# Один из вариантов выхода из машины состояния, предупреждение об этой 
# команде написано при запуске состояния
@router.message(Command("cancel"))
@router.message(F.text == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:
	current_state = await state.get_state()
	if current_state is None:
		await message.reply(
			text="Нечего отменять, но хорошо.",
			)
		return
	
	await state.clear()
	await message.answer(
		text="Состояние завершено.",
		reply_markup=main_kb(),
		)
	

# Переход назад к состоянию "name"
@router.message(CreateTask.description, F.text == "Назад")
async def description_task_back(message: Message, state: FSMContext):
	await state.set_state(CreateTask.name)
	await message.answer(
		text="Напишите название задачи.",
		reply_markup=back_kb(),
		)


# Переход к следующему состоянию если пользователь ввел корректный текст
@router.message(CreateTask.description, F.text)
async def description_task(message: Message, state: FSMContext):
	await state.set_state(CreateTask.responsible_person)
	await state.update_data(description=message.text)
	await message.answer(
		text="Напишите ответственного человека или пропустите данный этап.",
		reply_markup=back_or_further_kb(),
		)
	

# Предупреждение пользователя о том что надо ввести корректное описание
# и так же не пропускает пользователя дальше
@router.message(CreateTask.description)
async def description_task_missklick(message: Message):
	await message.answer(
		text="Я вас не понял, напишите пожалуйста корректное описание задачи!",
		reply_markup=back_kb(),
		)