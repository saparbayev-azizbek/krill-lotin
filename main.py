from aiogram import Bot, Dispatcher, executor, types
from environs import Env
from transliterate import to_latin, to_cyrillic

env = Env()
env.read_env()

token = env('token')
bot = Bot(token=token)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer(f'<b>✋ Assalomu alaykum <i>{message.from_user.first_name}</i></b>\n\n'
                         f'<b>🤖 Bu bot sizga lotin alifbosidagi matnlarni</b> \n'
                         f'<b>krill alifbosiga o\'tkazishda yordam beradi</b>', parse_mode='HTML')

@dp.message_handler()
async def matn(message: types.Message):
    if message.text.isascii():
        text = message.text.replace('o‘', 'ў')
        await message.answer(to_cyrillic(text))
    else:
        await message.answer(to_latin(message.text))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
