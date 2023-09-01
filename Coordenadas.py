from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        print(f"Clique com o botão esquerdo do mouse em: x = {x}, y = {y}")

def main():
    print("Clique com o botão esquerdo do mouse para identificar as coordenadas.")
    with mouse.Listener(on_click=on_click) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\nEncerrando o programa.")

if __name__ == "__main__":
    main()
