import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
logging.basicConfig(level=logging.INFO)

bot = Bot( token='5919471305:AAGeCb6ok69RLIVupnsJNwmlCex04m-S7i0' )
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
    reply_markup=markup
)


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
async def ban(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMINS:
            await message.answer("Ты не мой босс!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot.kick_chat_member(message.chat.id,
                                       message.reply_to_message.from_user.id)
            await message.answer(f"{message.from_user.first_name} братан кикнул "
                                 f"{message.reply_to_message.from_user.full_name}")
    else:
        await message.answer("Пиши в группе!")

async def game(message: types.Message):
    if message.from_user.id in ADMINS:
        data = ['⚽️', '🏀', '🎯', '🎰', '🎳', '🎲']
        r = random.choice(data)
        await bot.send_dice(message.chat.id, emoji=r)
    else:
        await bot.send_message(message.chat.id, 'Ты не админ')
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
dp.register_message_handler(game, commands=['game'])

import random
from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ChatActions

async def send_smile(message: types.Message):
    if "python" in message.text.lower():
        smile = random.choice(["😂", "😜", "😎", "🤩", "🥳"])
        await message.answer(smile)

async def ban_user(message: types.Message):
    username = message.get_args()
    await message.chat.kick(username)
    await message.answer(f"{username} вышел сам!")

dp.filters_factory.bind(Command, command="ban")
dp.filters_factory.bind(Text, text="python")
dp.register_message_handler(send_smile)
dp.register_message_handler(ban_user, commands="ban")

async def ban_user(message: types.Message):
    username = message.get_args()
    await message.chat.kick(username)
    msg = await message.answer(f"{username} вышел сам!")
    await bot.pin_chat_message(chat_id=message.chat.id, message_id=msg.message_id)