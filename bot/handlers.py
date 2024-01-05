from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import flags
import bot.utils as utils
import bot.texts as texts

router = Router()
@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(texts.greet.format(name=msg.from_user.full_name))

@router.message()
@flags.chat_action("typing")
async def generate_text(msg: Message):
    prompt = msg.text
    mesg = await msg.answer(texts.gen_wait)
    res = await utils.generate_text(prompt)
    if not res:
        return await mesg.edit_text(texts.gen_error)
    await mesg.edit_text(res[0], disable_web_page_preview=True)

