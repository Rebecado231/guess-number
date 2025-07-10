"""Guess the Number game.

Completa las secciones marcadas con TODO para que el juego funcione.
Ejecuta 'python guess_number.py' para probar tu implementación.
"""

import random

LOWER_BOUND = 1
UPPER_BOUND = 100


def generate_secret() -> int:
    """Devuelve un número aleatorio entre LOWER_BOUND y UPPER_BOUND (incluidos)."""
    random_number = random.randint(1, 100)
    
    return random_number


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


def main() -> None:
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


if __name__ == "__main__":
    main()
