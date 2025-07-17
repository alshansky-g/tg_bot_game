from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button1 = KeyboardButton(text="🪨")
button2 = KeyboardButton(text="✂️")
button3 = KeyboardButton(text="📄")

keyboard = ReplyKeyboardMarkup(
    keyboard=[[button1, button2, button3]], resize_keyboard=True
)

button4 = KeyboardButton(text="Давай!")
button5 = KeyboardButton(text="Не хочу!")

keyboard2 = ReplyKeyboardMarkup(
    keyboard=[[button4, button5]], resize_keyboard=True
)
# keyboard3 = ReplyKeyboardMarkup(
#     keyboard=[[button4, button5]], resize_keyboard=True
# )
