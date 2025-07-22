"""Guess the Number game.

Completa las secciones marcadas con TODO para que el juego funcione.
Ejecuta 'python guess_number.py' para probar tu implementación.
"""

import random
import json

LOWER_BOUND = 1
UPPER_BOUND = 100


def generate_secret() -> int:
    """Devuelve un número aleatorio entre LOWER_BOUND y UPPER_BOUND (incluidos)."""
    random_number = random.randint(1, 100)

    return random_number


def ask_name() -> str:
    """Devuelve el nombre del jugador"""
    user_name = input("User name: ")
    return user_name


def get_user_guess() -> int:
    """Solicita al usuario un número y lo devuelve como int."""
    while True:
        try:
            user_guess = int(input("Write a number between 1 and 100: "))
            if user_guess >= LOWER_BOUND and user_guess <= UPPER_BOUND:
                return user_guess
            else:
                print("Try again with a number between 1 and 100")
        except ValueError:
            print("That's not a valid number. Please try again.")


def play_one_game() -> int:
    """Función que representa una partida del juego"""
    attempt_num = 0
    real_num = generate_secret()
    while True:
        user_num = get_user_guess()
        attempt_num += 1
        if user_num < real_num:
            print("Try a higher number")
        elif user_num > real_num:
            print("Try a lower number")
        else:
            break
    print("Congrats! You get it just in " + str(attempt_num) + " attempts.")
    return attempt_num


def main() -> tuple[str, list[int]]:
    """Bucle principal del juego."""
    attempts = []
    name = ask_name()
    while True:
        game_attempts = play_one_game()
        attempts.append(game_attempts)
        play_again = input("Play again? Y/N")
        if play_again.strip().upper() == "N":
            print("Bye bye!")
            break
    return name, attempts


if __name__ == "__main__":
    player_name, all_attempts = main()
    with open("game_record.json", "r", encoding="utf-8") as file:
        game_record = json.load(file)
    for player_sheet in game_record:
        if player_sheet["player"] == player_name:
            total_record = player_sheet["attempts"]["record"]
            total_record.extend(all_attempts)
            total_att = sum(total_record)
            player_sheet["attempts"]["total"] = total_att
            att_average = total_att / len(total_record)
            player_sheet["attempts"]["average"] = att_average
            best_play = min(total_record)
            player_sheet["attempts"]["best"] = best_play
            break
    else:
        total_att = sum(all_attempts)
        player_sheet = {
            "player": player_name,
            "attempts": {
                "record": all_attempts,
                "total": total_att,
                "average": total_att / len(all_attempts),
                "best": min(all_attempts),
            },
        }
        game_record.append(player_sheet)

    with open("game_record.json", "w", encoding="utf-8") as file:
        json.dump(game_record, file, indent="\t")
        print("Game saved")


