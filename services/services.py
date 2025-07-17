import random

game_choices = ["камень", "ножницы", "бумага"]


def bot_choosing():
    return random.choice(game_choices)


def define_winner(bot_choice: str, user_choice: str) -> str:
    if bot_choice == "камень" and user_choice == 'ножницы':
        game_result = 'Ура, я победил!'
    elif bot_choice == 'ножницы' and user_choice == 'бумага':
        game_result = 'Ура, я победил!'
    elif bot_choice == 'бумага' and user_choice == 'камень':
        game_result = "Ура, я победил!"
    elif bot_choice == user_choice:
        game_result = 'Ничья. В следующий раз я выиграю!'
    else:
        game_result = 'Кажется, ты победил...'

    return game_result
