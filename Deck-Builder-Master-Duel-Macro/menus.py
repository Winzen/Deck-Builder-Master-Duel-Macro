import botdeck


def main_menus():

    """This function only manages deck() and Macro_deck() functions"""

    botdeck.init()

    while True:
        try:
            resposta = int(input("""
    Welcome to MACRO-TXT YU GI OH MASTER DUEL!!!
    Version 0.0001v
    
    What do you want to do?
    1 - Get the list of cards and amount of a deck
    2 - Automatically build a deck using the Macro
    3 - Quit
    
    Your Choice:"""))
            print("\n" * 100)

            if resposta > 3:
                print("\n" * 100)
                print("\n\n\n\n\33[31mJust numbers in between 1 and 3. Please\33[m")

            if resposta == 1:
                botdeck.deck(True)
                botdeck.sleep(3)

            elif resposta == 2:
                botdeck.macro_deck()
                botdeck.sleep(3)

            elif resposta == 3:
                break

        except:

            print("\n" * 100)
            print("\n\n\n\n\33[31mInvalid data!\nPlease, just numbers in between 1 and 3..\33[m")
