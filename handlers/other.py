from aiogram import F, Router
from aiogram.types import Message

from keyboards.keyboards import keyboard
from services.services import bot_choosing, define_winner

router = Router()


@router.message(F.text.in_(["камень", "ножницы", "бумага"]))
async def user_answer(message: Message):
    bot_choice = bot_choosing()
    game_result = define_winner(bot_choice, user_choice=message.text)  # type: ignore
    if game_result.lower().startswith("ничья"):
        bot_choice = f"тоже {message.text}"
    await message.answer(text=f"У меня {bot_choice}. {game_result}")


@router.message()
async def any_text(message: Message):
    await message.answer(
        text="Общаться я не умею :( Тебе нужно выбрать одну из кнопок ниже.",
        reply_markup=keyboard,
    )
