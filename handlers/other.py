from aiogram import Router
from aiogram.types import Message

from keyboards.keyboards import keyboard
from lexicon.lexicon import LEXICON_RU

router = Router()


@router.message()
async def any_text(message: Message):
    await message.answer(
        text=LEXICON_RU["unknown command"],
        reply_markup=keyboard,
    )
