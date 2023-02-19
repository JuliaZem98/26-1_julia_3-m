import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
logging.basicConfig(level=logging.INFO)

bot = Bot(token=5919471305:AAGeCb6ok69RLIVupnsJNwmlCex04m-S7i0)

dp = Dispatcher(bot)

@dp.message_handler(commands=['hello'])
async def say_hello(message: types.Message):
    name = message.from_user.first_name
    await message.reply(f'Hello, {name}!')
    await message.answer('пока что всё.')
@dp.message_handler(commands=['quiz'])

async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 1", callback_data="button_call_1")
    markup.add(button_call_1)
    question = "Вы готовы дети????"
    answers = [
        'Да капитан',
        'Нет капитан',]

await bot.send_poll(
    chat_id=message.from_user.id,
    question=question,
    options=answers,
    is_anonymous=False,
    type='quiz',
    correct_option_id=0,
    open_period=15,
    reply_markup=markup)


@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 2", callback_data="button_call_2")
    markup.add(button_call_1)
    question = "откуда мем"
    answers = [
        "Гугл наверное",
        "не знаю",
        "точно из гугла",
        "я слишком стар для такого",]

photo = open("media/mem1.jpeg", "rb")
await bot.send_photo(call.from_user.id, photo=photo)
await bot.send_poll(
    chat_id=call.from_user.id,
    question=question,
    options=answers,
    is_anonymous=False,
    type='quiz',
    correct_option_id=2,
    explanation="по идее это сложно",
    open_period=15,
    reply_markup=markup)


@dp.callback_query_handler(text="button_call_2")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 3", callback_data="button_call_2")
    markup.add(button_call_1)
    question = "откуда мем"
    answers = [
        "Гугл наверное",
        "не знаю",
        "точно из гугла",
        "я слишком стар для такого",]

photo = open("media/14254874.jpg", "rb")
await bot.send_photo(call.from_user.id, photo=photo)
await bot.send_poll(
    chat_id=call.from_user.id,
    question=question,
    options=answers,
    is_anonymous=False,
    type='quiz',
    correct_option_id=2,
    explanation="по идее это сложно",
    open_period=15,
    reply_markup=markup)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
if name == 'main':
    executor.start_polling(dp, skip_updates=True)
