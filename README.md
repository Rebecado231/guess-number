# Guess the Number 🎲

¡Este es tu **primer mini‑proyecto de Python**! Construirás un sencillo juego de consola donde el usuario intenta adivinar un número secreto entre 1 y 100. El objetivo es que practiques **aspectos fundamentales de Python, manejo del flujo de control, funciones y loops**, así como la configuración básica de un entorno profesional (`venv`, `black`, `pylint`, `mypy`).

## 1. Requisitos

- `python ≥ 3.12`
- `git`

## 2. Arranque rápido

```bash
# Clona tu propio fork
git clone <tu‑fork‑url> guess-number
cd guess-number

# Crea y activa un entorno virtual
python -m venv .venv
source .venv/bin/activate      # Windows: .\.venv\Scripts\activate

# Instala dependencias de desarrollo
pip install -r requirements-dev.txt

# Formatea y analiza (solo deberían aparecer TODOs sin implementar)
black .
pylint guess_number.py
mypy guess_number.py

# Ejecuta el juego (fallará hasta que completes el código)
python guess_number.py
```

## 3. Tareas a completar

1. Implementa las funciones marcadas con **`TODO`** en `guess_number.py`.
2. La lógica básica es:
   - Generar un número secreto con `random.randint`.
   - Pedir con `input()` un número al usuario y convertirlo a `int`.
   - Mostrar **“Más alto”** o **“Más bajo”** según corresponda.
   - Contar intentos y mostrar al acertar.
   - Preguntar _“¿Jugar de nuevo? (s/n)”_ para reiniciar sin cerrar el script.
3. Ejecuta `black`, `pylint` y `mypy --strict` hasta que no queden
   advertencias.
4. (Opcional) Añade colores con la librería `colorama` o registra la partida
   en un archivo `scores.csv`.
