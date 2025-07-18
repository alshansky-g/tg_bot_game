import random

game_choices = ["🪨", "✂️", "📄"]
play_again = [
    "Повторим?",
    "Еще разок?",
    "Может попробуем снова?",
    "Как насчет еще одного раунда?",
    "Сыграем снова?",
    "Давай сыграем снова!",
    "Может повторим?",
    "Хочешь сыграть еще раз?",
]
play_again_bot_wins = [
    "Хочешь отыграться? :)",
    "Не повезло тебе... Повторим? :)",
    "Ты не расстраивайся, просто я в этом деле мастер. :) "
    "Хочешь сыграть еще раз?",
    "Не печалься. С кем не бывает. Сыграем снова? :)",
    "Обидно, наверно. Сыграем еще раз? :)",
]
play_again_bot_loses = [
    'Что-то я уже устал. Или хочешь сыграть еще раз?',
    "Новичкам везёт! Дай отыграться!",
    "А ты не жульничаешь? Давай еще раз!",
    "Мне сегодня не везёт! Повторим?",
    "Думаю, нужно подправить алгоритмы... Сыграем снова?",
    "Наверно, Глеб специально сделал, чтобы я проиграл! Давай попробуем еще?"
]


def bot_choosing():
    return random.choice(game_choices)


def define_winner(bot_choice: str, user_choice: str) -> tuple[str, str]:
    if bot_choice == "🪨" and user_choice == "✂️":
        game_result = "Ура, я победил!"
    elif bot_choice == "✂️" and user_choice == "📄":
        game_result = "Ура, я победил!"
    elif bot_choice == "📄" and user_choice == "🪨":
        game_result = "Ура, я победил!"
    elif bot_choice == user_choice:
        game_result = "Ничья. В следующий раз я выиграю!"
    else:
        game_result = "Поздравляю с победой!"

    if game_result.startswith("Ура"):
        return game_result, random.choice(play_again_bot_wins)
    elif game_result.startswith('Ничья'):
        return game_result, random.choice(play_again)
    return game_result, random.choice(play_again_bot_loses)
