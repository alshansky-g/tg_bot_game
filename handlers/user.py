from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from keyboards.keyboards import keyboard, keyboard2
from lexicon.lexicon import LEXICON_RU
from services.services import bot_choosing, define_winner

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU["/start"], reply_markup=keyboard2)


@router.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU["/help"], reply_markup=keyboard2)


@router.message(F.text == "Давай!")
async def start_game(message: Message):
    await message.answer(
        text=LEXICON_RU['start game'], reply_markup=keyboard
    )


@router.message(F.text == "Не хочу!")
async def not_start_game(message: Message):
    await message.answer(
        text=LEXICON_RU['no start game'],
    )


@router.message(F.text.in_(["🪨", "✂️", "📄"]))
async def user_answer(message: Message):
    bot_choice = bot_choosing()
    game_result, play_again = define_winner(
        bot_choice,
        user_choice=message.text,  # type: ignore
    )
    if game_result.lower().startswith("ничья"):
        bot_choice = f"тоже {message.text}"
    await message.answer(
        text=f"У меня {bot_choice}. {game_result}\n\n{play_again}",
        reply_markup=keyboard2,
    )
