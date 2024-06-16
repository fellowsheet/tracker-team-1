from aiogram import Router, F

from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states.create_task import CreateTask
from keyboards.reply.main_kb import main_kb
from keyboards.reply.back_kb import back_kb
from keyboards.reply.status_kb import status_kb
from keyboards.reply.priority_kb import priority_kb
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
	

# Переход назад к состоянию "status"
@router.message(CreateTask.priority, F.text == "Назад")
async def proirity_task_back(message: Message, state: FSMContext):
	await state.set_state(CreateTask.status)
	await message.answer(
		text="Выберите состояние задачи.",
		reply_markup=status_kb(),
		)
	

# Переход к следующему состоянию если пользователь выбрал приоритет задачи из списка приоритетов
@router.message(CreateTask.priority, F.text.in_(settings.priority))
async def priority_task(message: Message, state: FSMContext):
	await state.set_state(CreateTask.deadline)
	await state.update_data(priority=message.text)
	await message.answer(
		text="Напишите дедлайн задачи в формате 31-12-2012",
		reply_markup=back_kb(),
	)


# Предупреждение пользователя о том что надо выбрать одно из приоритетов
# и так же не пропускает пользователя дальше
@router.message(CreateTask.priority)
async def priority_task_missklick(message: Message):
	await message.answer(
		text="Я вас не понял, выберите пожалуйста приоритет задачи!",
		reply_markup=priority_kb(),
		)