from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_rock = KeyboardButton(text="🪨")
button_scissors = KeyboardButton(text="✂️")
button_paper = KeyboardButton(text="📄")

keyboard_game_choices = ReplyKeyboardMarkup(
    keyboard=[[button_rock], [button_scissors], [button_paper]],
    resize_keyboard=True,
)

button_yes = KeyboardButton(text="Давай!")
button_no = KeyboardButton(text="Не хочу!")

keyboard_yes_no = ReplyKeyboardMarkup(
    keyboard=[[button_yes, button_no]],
    resize_keyboard=True,
    one_time_keyboard=True,
)
