from aiogram import Router, F

from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states.create_task import CreateTask
from keyboards.reply.main_kb import main_kb
from keyboards.reply.back_kb import back_kb
from keyboards.reply.priority_kb import priority_kb
from keyboards.reply.status_kb import status_kb
from config_data.config import settings


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
	

# Переход назад к состоянию "tags"
@router.message(CreateTask.status, F.text == "Назад")
async def status_task_back(message: Message, state: FSMContext):
	await state.set_state(CreateTask.tags)
	await message.answer(
		text="Напишите теги этой задачи через пробел.\n"
			 "Пример: bug python database",
		reply_markup=back_kb(),
		)
	

# Переход к следующему состоянию если пользователь выбрал состояние задачи из списка состояний
@router.message(CreateTask.status, F.text.in_(settings.status))
async def status_task(message: Message, state: FSMContext):
	await state.set_state(CreateTask.priority)
	await state.update_data(status=message.text)
	await message.answer(
		text='Выберите приоритетность задачи.',
		reply_markup=priority_kb(),
	)
	

# Предупреждение пользователя о том что надо ввести корректное состояние задачи
# и так же не пропускает пользователя дальше
@router.message(CreateTask.status)
async def status_task_missklick(message: Message):
	await message.answer(
		text="Я вас не понял, выберите пожалуйста одно из состояний!",
		reply_markup=status_kb(),
		)