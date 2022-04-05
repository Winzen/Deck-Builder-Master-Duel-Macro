from keyboard import is_pressed
from get_cards import deck
from pyautogui import click, write, pixel, press, rightClick, size
from time import sleep as sleep
from get_cards import init

def macro_deck():

    """'Macro_deck' calls 'deck()' function
    after that control your mouse and keybord
    to put the cards from 'deck()' in your DeckBuilder"""

    init()
    tamanho = size()
    largura = int(tamanho.width)*0.7
    altura = tamanho.height * (0.21 if tamanho.width - tamanho.height > 350 else 0.27)
    altura = tamanho.height * 0.18 if tamanho.width - tamanho.height > 550 else altura
    possivel_erro = dict()

    print("""
\33[31mBefore proceeding.
Make sure the game configuration  is correct.\33[m
\33[33m
Requirements:

1 - The game's language must be English.
2 - The game's resolution must be 1280x720.
3 - The game's view mode must be Full Screen Mode.
4 - In the Deck Builder, show up all card must be active.
5 - Go to Deck Builder
\33[m
\33[31mTo stop the macro just HOLD the "Esc" on your keybord.\33[m

After you placing the link you have 5 seconds to return to the game before the macro starts.
    """)
    cartas = deck()

    if len(cartas) != 0 and cartas != "3":
        for x in range(5):
            print("You must to return to the DeckBuild Screen Please.. SECONDS:", x+1)
            sleep(1)

        for nome, quantidade in cartas.items():

            if is_pressed("esc"):
                break

            click(largura, altura)
            write(nome)
            press('enter')
            sleep(2)



            if pixel(int(tamanho.width*0.75), int(tamanho.height * 0.35))[2] > 70:
                possivel_erro[nome] = quantidade

            for x in range(int(quantidade)):
                rightClick(int(tamanho.width)*0.7, tamanho.height * 0.38)

            sleep(2)

        print("\nList Of Possible Missing Cards.\n")
        for x, y in possivel_erro.items():
            print(x, y)
