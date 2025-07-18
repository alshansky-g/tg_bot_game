from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from keyboards.keyboards import keyboard_game_choices, keyboard_yes_no
from lexicon.lexicon import LEXICON_RU
from services.services import bot_choosing, define_winner

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU["/start"], reply_markup=keyboard_yes_no
    )


@router.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer(
        text=LEXICON_RU["/help"], reply_markup=keyboard_yes_no
    )


@router.message(F.text == "Давай!")
async def start_game(message: Message):
    await message.answer(
        text=LEXICON_RU["start game"], reply_markup=keyboard_game_choices
    )


@router.message(F.text == "Не хочу!")
async def not_start_game(message: Message):
    await message.answer(
        text=LEXICON_RU["no start game"],
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
    if game_result.startswith('Поздравляю'):
        message_effect_id = "5046509860389126442"
    else:
        message_effect_id = None
    await message.answer(
        text=f"У меня {bot_choice}. {game_result}\n\n{play_again}",
        message_effect_id=message_effect_id,
        reply_markup=keyboard_yes_no,
    )
