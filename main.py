import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


def go_back():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text='Назад в меню', callback_data='back'))
    return kb


def start_markup():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text='Команды с фото', callback_data='photos'),
           InlineKeyboardButton(text='Команды с аудио', callback_data='voices'),
           InlineKeyboardButton(text='Хобби', callback_data='hobby'),
           InlineKeyboardButton(text='Исходник бота', url='https://github.com/Ju1ce13/YandexPraktikumTestBot'))
    return kb


@dp.message_handler(commands='start')
async def start_bot(message: types.Message):
    await message.answer('Добро пожаловать в бота созданного мной:3')
    await message.answer('Выбери дальнейшее действие для взаимодействия с ботом:', reply_markup=start_markup())


@dp.callback_query_handler(text='back')
async def start_bot(cb: types.CallbackQuery):
    await cb.message.answer('Выбери дальнейшее действие для взаимодействия с ботом:', reply_markup=start_markup())


@dp.message_handler(commands='selfie')
async def my_selfie(message: types.Message):
    photo = InputFile('last_selfie.jpg')
    await message.answer_photo(photo=photo, reply_markup=go_back())


@dp.message_handler(commands='selfie2')
async def my_selfie(message: types.Message):
    photo = InputFile('high_school.jpg')
    await message.answer_photo(photo=photo, reply_markup=go_back())


@dp.callback_query_handler(text='hobby')
async def start_bot(cb: types.CallbackQuery):
    await cb.message.answer('''Моё главное увлечение - баскетбол.
Играю в него ещё со школьной скамьи, потому что супер динамичная игра, так ешё и заставляет
держать своё тело в тонусе. Мой любимый клуб - УНИКС (потому что я родом из Татарстана)''', reply_markup=go_back())


@dp.message_handler(commands='first_love')
async def my_love(message: types.Message):
    voice = InputFile('first_love.ogg')
    await message.answer_voice(voice=voice, reply_markup=go_back())


@dp.message_handler(commands='gpt')
async def gpt(message: types.Message):
    voice = InputFile('gpt.ogg')
    await message.answer_voice(voice=voice, reply_markup=go_back())


@dp.message_handler(commands='sql_no_sql')
async def sql(message: types.Message):
    voice = InputFile('sql.ogg')
    await message.answer_voice(voice=voice, reply_markup=go_back())


@dp.callback_query_handler(text='photos')
async def my_selfie(cb: types.CallbackQuery):
    await cb.message.answer('''Напишите в чат /selfie, чтоб увидеть моё последнее селфи
или /selfie2 для селфи со школы''')


@dp.callback_query_handler(text='voices')
async def my_selfie(cb: types.CallbackQuery):
    await cb.message.answer('''Напишите в чат /first_love, чтоб узнать про мою первую любовь
/gpt для того, чтобы узнать что такое GPT
/sql_no_sql для того, чтобы узнать разницы между NoSql и SQL''')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
