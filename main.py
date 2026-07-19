import keyboard
from random import randint
from time import sleep, time

def write(text):
    keyboard.write(str(text))

WRITE_HOTKEYS = {
    "1": "¹",
    "2": "²",
    "3": "³",
    "4": "⁴",
    "5": "⁵",
    "6": "⁶",
    "7": "⁷",
    "8": "⁸",
    "9": "⁹",
    "0": "⁰",
    "up": "↑",
    "right": "→",
    "left": "←",
    "down": "↓",
    "p": "π",
    "t": "τ",
    "a": "α",
    "b": "β",
    "h": "ㅤ",
    "r": lambda: str(randint(1_000_000_000, 9_999_999_999)),
}

def create_handler(key):
    def handler():
        value = WRITE_HOTKEYS[key]
        if callable(value):
            value = value()

        sleep(0.01)
        keyboard.send("space")
        keyboard.send("backspace")
        sleep(0.01)
        keyboard.write(str(value), delay=0)
        print(f"{key} → {value}")
    
    return handler

for key in WRITE_HOTKEYS:
    try:
        keyboard.add_hotkey(f'shift+alt+{key}', create_handler(key), suppress=True)
    except Exception as e:
        print(f"✗ {key}: {e}")

for key, value in list(WRITE_HOTKEYS.items()):
    print(f"ALT + SHIFT + {key} = {value}")

try:
    keyboard.wait()
except KeyboardInterrupt:
    print("\n👋 Завершено")