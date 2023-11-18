import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram import F
from aiogram.filters.command import Command
import emoji
import gif
# Bot token can be obtained via https://t.me/BotFather
TOKEN = ("6913490279:AAEs9FpE8IcLGEyD0wX63rsokLD5hPqXDQk")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message()
async def echo_message_handler(msg: Message):
    await msg.answer_animation("CgACAgQAAxkBAAN2ZVdEmUrevoBmWPiBQVgzTSSq_YAAAksDAAIZpART2IBLuYNDmrkzBA")

@dp.message(F.photo)
async def photo_handler(msg: Message):
    await msg.answer("Photo handler successfull")
    await msg.answer(f"{msg.photo[0].file.id}")

@dp.message(F.document)
async def photo_handler(msg: Message):
    await msg.answer(f"Document handler successfull\n{msg.document.file_id}")


@dp.message(F.video)
async def photo_handler(msg: Message):
    await msg.answer("Video handler successfull")
    await msg.answer(f"{msg.video.file_id}")

@dp.message(F.audio)
async def photo_handler(msg: Message):
    await msg.answer("Audio handler successfull")
    await msg.answer(f"{msg.audio.file_id}")


@dp.message(F.sticker)
async def photo_handler(msg: Message):
    await msg.answer("Sticker handler successfull")

@dp.message(F.voice)
async def photo_handler(msg: Message):
    await msg.answer("Voice handler successfull")

@dp.message(lambda msg : emoji.emoji_count(msg.text)>0)
async def photo_handler(msg: Message):
    await msg.answer("Emoji handler successfull")


@dp.message(Command('start'))
@dp.message(Command('admin'))
@dp.message(Command('panel'))
# async def digit_handler(msg : Message ):
#      await msg.answer("Hello world", reply_markup=number_button())
#
#
@dp.message(lambda msg: msg.text.isdigit() and 1 <= int(msg.text) <=100)
async def digit_handler(msg : Message):
   await msg.answer(msg.text)


@dp.message(F.text.isdigit())
async def digit_handler(msg : Message):
   await msg.answer(msg.text)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

