from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button1 = KeyboardButton(text='камень')
button2 = KeyboardButton(text='ножницы')
button3 = KeyboardButton(text='бумага')

keyboard = ReplyKeyboardMarkup(keyboard=[[button1, button2, button3]],
                               resize_keyboard=True)
