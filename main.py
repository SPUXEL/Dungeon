from aiogram import Bot, Dispatcher, executor, md, types
import os, sys, random
import comp, lang


# -- INIT API_TOKEN --
with open('config/api_token') as file_api_token:
    file_content = file_api_token.read()
    exec('%s = %s' % tuple(file_content.split(' ', 1)))


# -- INIT BOT & DP --
bot = Bot(token=API_TOKEN)
#bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.MARKDOWN_V2)
dp = Dispatcher(bot)


# --- START ---
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if(not comp.Database().get_user(message.from_user.id)):
        comp.Database().add_user(message.from_user.id)

    else:
        await bot.send_message(message.from_user.id, 'Good!')

    locale = lang.ru
    #locale = lang.ru if message.from_user.locale == 'ru' else lang.en


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
