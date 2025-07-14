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


def main() -> int:
    """Bucle principal del juego."""
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
    play_again = input("Play again? Y/N")
    if play_again.strip().upper() == "Y":
        main()
    else:
        print("Bye bye!")
    return attempt_num


if __name__ == "__main__":
    
    attempts = main() 
    att_record = []
    att_record.append(attempts)
    total_att = sum(att_record)
    att_average = total_att / len(att_record)



player_sheet = {
    "player" : "user_name"
    "attempts" : [] 
    }

def sheet_register (att_record, total_att, att_average):
    attempts = {
        "Record" = att_record
        "Total" = total_att 
        "Average" = att_average
    }

with open (game_record.json, "w" ) as file:
        json.dump (player_sheet, file)
print ("Game saved")