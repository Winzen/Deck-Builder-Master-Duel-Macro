
from func import pc, is_pressed, config_colum, search, \
    possibly_second_card, mult_card_search, alert, list_fails


def bot_deck(deck_):

    """'Macro_deck' calls 'deck()' function
        after that control your mouse and keybord
        to put the cards from 'deck()' in your DeckBuilder"""

    numero = 0
    rows, resolution = config_colum()
    fails = dict()
    ban_cards = ["one for one", "there can be only one"]
    cartas = deck_

    if len(cartas) != 0:

        for nome, quantidade in cartas.items():

            if nome.lower() not in ban_cards:

                if is_pressed("esc"):
                    alert(text='MACRO FOI PARADO', title='Aviso', button='OK')
                    break

        #        Pesquisa
                search(nome)

                verification = possibly_second_card(1086, 320)

                if verification is True or numero == 0:
                    numero = 1

                    done = mult_card_search(nome, quantidade, resolution, rows)

                    if done is False:
                        fails[nome] = quantidade

                else:
                    for _ in range(int(quantidade)):
                        pc.ClickPositions(1026, 320).right_click()
            else:
                fails[nome] = quantidade

    list_fails(fails)
