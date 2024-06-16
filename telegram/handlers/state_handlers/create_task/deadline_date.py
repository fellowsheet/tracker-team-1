from aiogram import Router, F

from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states.create_task import CreateTask
from keyboards.reply.main_kb import main_kb
from keyboards.reply.back_kb import back_kb
from keyboards.reply.priority_kb import priority_kb

from datetime import datetime


router = Router(name=__name__)


# Вывод результата в сообщение (далее при подключении к БД видоизменится ответ)
# Необходимо решить вопрос по поводу как будут выводиться сотрудники которым можно
# назначить задачу или же надо самому писать (имя\id) сотрудника, так же надо будет 
# сделать валидацию на руководство
async def send_create_task_info(message: Message, data: dict) -> None:
	text = "Your task:\n\n"\
		f"Name: {data["name"]}\n"\
		f"Description: {data["description"]}\n"\
		f"Responsible person: {data["responsible_person"]}\n"\
		f"Tags: {data["tags"]}\n"\
		f"State: {data["state"]}\n"\
		f"Proirity: {data["priority"]}\n"\
		f"Date of creation: {datetime.now()}\n"\
		f"Deadline date: {data["deadline_date"]}\n"
	
	await message.answer(
		text=text,
		reply_markup=main_kb(),
		)


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
	

# Переход назад к состоянию "proirity"
@router.message(CreateTask.deadline_date, F.text == "Назад")
async def deadline_date_task_back(message: Message, state: FSMContext):
	await state.set_state(CreateTask.priority)
	await message.answer(
		text="Выберите приоритетность задачи.",
		reply_markup=priority_kb(),
		)
	

# Вывод текста на экран (временно) со всеми собранными данными что ввел пользователь
# если пользователь ввел корректную дату и завершение FSM машины
@router.message(CreateTask.deadline_date, F.text)
async def deadline_date_task(message: Message, state: FSMContext):
	data = await state.update_data(deadline_date=message.text)
	await send_create_task_info(message, data)
	await state.clear()


# Предупреждение пользователя о том что надо вывести корректную дату
# и так же не пропускает пользователя дальше
@router.message(CreateTask.deadline_date)
async def deadline_date_task_missklick(message: Message):
	await message.answer(
		text="Я вас не понял, напишите пожалуйста корректную дату в формате 31-12-2012",
		reply_markup=back_kb(),
		)


