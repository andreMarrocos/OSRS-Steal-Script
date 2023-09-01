import keyboard
import pyautogui
import time
import random
from threading import Thread

# Região para o clique aleatório
custom_region = {
    'min_x': 660,
    'max_x': 696,
    'min_y': 533,
    'max_y': 567
}

corner_region = {
    'min_x': 1620,
    'max_x': 1641,
    'min_y': 608,
    'max_y': 629
}

running = False


def click_thread():
    global running
    while running:
        for _ in range(2):
            random_x = random.randint(corner_region['min_x'], corner_region['max_x'] - 1)
            random_y = random.randint(corner_region['min_y'], corner_region['max_y'] - 1)
            pyautogui.click(random_x, random_y)
            print(f"Clique aleatório na região do canto: ({random_x}, {random_y})")
            interval = 0.5 + random.uniform(0.01, 0.99)
            print(f"Intervalo após o clique no canto: {interval:.2f} segundos")
            time.sleep(interval)

        for _ in range(2):
            random_x = random.randint(custom_region['min_x'], custom_region['max_x'] - 1)
            random_y = random.randint(custom_region['min_y'], custom_region['max_y'] - 1)
            pyautogui.click(random_x, random_y)
            print(f"Clique aleatório na região: ({random_x}, {random_y})")
            interval = 0.5 + random.uniform(0.01, 0.99)
            print(f"Intervalo após o clique na região: {interval:.2f} segundos")
            time.sleep(interval)

def toggle_script():
    global running
    running = not running
    if running:
        click_thread_instance = Thread(target=click_thread)
        click_thread_instance.start()
        print("Script em execução.")
    else:
        print("Script parado.")

# Ativar e desativar o bot
keyboard.add_hotkey('6', toggle_script)

print("Pressione 6 para começar/parar o script.")
keyboard.wait('esc')

# Parar o script quando sair do loop
running = False
keyboard.unhook_all()