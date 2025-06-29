"""Guess the Number game.

Completa las secciones marcadas con TODO para que el juego funcione.
Ejecuta 'python guess_number.py' para probar tu implementación.
"""

import random

LOWER_BOUND = 1
UPPER_BOUND = 100


def generate_secret() -> int:
    """Devuelve un número aleatorio entre LOWER_BOUND y UPPER_BOUND (incluidos)."""

    # TODO:
    #     - Utiliza random.randint.
    #     - Elimina la excepción y devuelve el número generado.
    raise NotImplementedError


def get_user_guess() -> int:
    """Solicita al usuario un número y lo devuelve como int."""

    # TODO:
    #     1. Usa input() para leer del usuario.
    #     2. Valida que sea un número dentro del rango; si no, vuelve a pedirlo.
    #     3. Gestiona ValueError cuando el usuario escriba texto no numérico.
    raise NotImplementedError


def main() -> None:
    """Bucle principal del juego."""

    # TODO:
    #     1. Llama a generate_secret() para obtener el número a adivinar.
    #     2. Inicia un contador de intentos en 0.
    #     3. Mientras el usuario no acierte:
    #          a. Llama a get_user_guess().
    #          b. Incrementa intentos.
    #          c. Imprime 'Más alto' o 'Más bajo' según corresponda.
    #     4. Felicita al usuario e indica cuántos intentos necesitó.
    #     5. Pregunta si quiere jugar otra vez ('s' / 'n').
    #        Si 's', reinicia el juego; si 'n', imprime '¡Hasta luego!' y sale.

    raise NotImplementedError


if __name__ == "__main__":
    main()
