import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message,KeyboardButton, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand, ReplyKeyboardMarkup
from secret import TELEGRAM_TOKEN as token


bot = Bot(token=token)
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, loop=loop)


@dp.message_handler(content_types=['document'])
async def document(message):
    await message.document.download()
    

@dp.message_handler()
async def messages(message: Message):
    await bot.set_my_commands([
        BotCommand(command="/start", description="1"),
        BotCommand(command="/stop", description="2"),
        BotCommand(command="/help", description="3")])
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"Сам {message.text}",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="111"),
                 KeyboardButton(text="222")]])
    )


@dp.callback_query_handler(lambda callback_query: callback_query.data)
async def callback_query(callback_query: CallbackQuery):
    try:
        await callback_query.message.delete()
    except Exception:
        pass

    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=callback_query.data,
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="-1-", callback_data=callback_query.data+"1")],[ 
                             InlineKeyboardButton(text="-2-", callback_data=callback_query.data+"2")]])
    )


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)