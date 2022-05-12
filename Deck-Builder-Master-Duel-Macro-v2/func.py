import positions_clicks as pc
from time import sleep
from pyautogui import size, alert, screenshot, press, write
import pytesseract
from PIL import Image
from keyboard import is_pressed


def possibly_second_card(x, y, raw=False, iconx=96, icony=255):

    """Verifica mundaças na interface depois do click"""

    second_card_slot = list()

    second_card_slot.append(pc.ClickPositions(iconx, icony).pixel())
    if raw is True:
        pc.ClickPositions(x, y, raw_value_y=True).left_click()
    else:
        pc.ClickPositions(x, y).left_click()

    sleep(1)
    second_card_slot.append(pc.ClickPositions(iconx, icony).pixel())
    if second_card_slot[0] == second_card_slot[1]:
        second_card = False
    else:
        second_card = True

    return second_card


def config_colum(verify=False):

    """Configura linhas e resolução print para OSR"""

    screen = size()
    with open(r"config_print/config.txt", "a", encoding="utf-8") as config:
        config.close()

    with open(r"config_print/config.txt", "r", encoding="utf-8") as config:
        config = config.read()

    if verify is True:
        return False if str(screen) not in config else True

    if str(screen) not in config:

        rows = list()

        resolution = config_resolution()

        search("One")

        start = pc.ClickPositions(1026, 320)
        start.left_click()
        rows.append(int(start.height))
        sleep(0.5)
        for y in range(int(start.height), screen.width, int(start.height*0.05)):

            if is_pressed("esc"):
                alert(text='MACRO FOI PARADO', title='Aviso', button='OK')
                break

            verication = possibly_second_card(1026, y, raw=True)
            if verication is True:
                rows.append(int(y))
                if len(rows) >= 5:
                    with open(r"config_print/config.txt", "w", encoding="utf-8") as config:
                        config.write(f"{str(screen)}\n{rows}\n{resolution}")
                    return rows, resolution
    else:
        with open(r"config_print/config.txt", "r", encoding="utf-8") as config:
            lines = config.readlines()
            return lines[1].strip("\n").strip("[]").split(","), float(lines[2])


def get_text(diretorio):

    """Retira o texto do print de nome da carta"""

    pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\tesseract.exe"
    phrase = pytesseract.image_to_string(Image.open(fr'{diretorio}'))
    return phrase


def mult_card_search(nome, quantidade, resolutions, rows):

    """Função procura e colocar cartas do link passado"""

    card = str

    for z, ylinha in enumerate(rows):
        ylinha = int(ylinha)
        #           Click Cards Coluna
        xprimeira = 1026
        for v, _ in enumerate(range(6)):
            if is_pressed("esc"):
                break

            sleep(1)
            pc.ClickPositions(xprimeira, ylinha, raw_value_y=True).move()

            fail = possibly_second_card(xprimeira, ylinha, iconx=86, icony=270, raw=True)

            if fail is False:
                return False

            sleep(0.5)
            pc.ClickPositions(86, 270).left_click()
            sleep(0.5)

            right_card = finding_cards(resolutions, nome)

            if right_card is True:
                sleep(1)
                for _ in range(int(quantidade)):
                    pc.ClickPositions(xprimeira, ylinha, raw_value_y=True).right_click()
                return True

            if card != nome:
                press("esc")

            xprimeira += 60 + (v * 2)

    return False


def search(nome):

    """Função que escreve e pesquisa o nome da carta no Master Duel"""

    sleep(1)
    pc.ClickPositions(1008, 189).left_click()
    write(nome)
    press("enter")
    sleep(1.5)


def interval():

    """Função que marca um intervalo"""

    for x in range(5):
        print("You must to return to the DeckBuild Screen Please.. SECONDS:", x+1)
        sleep(1)


def list_fails(cards):

    """Função recebe um dicionario e retorna uma Alerta com possiveis cartas faltando no deck"""

    if len(cards) > 0:
        txt = ''
        for nome, quantidade in cards.items():
            txt += f"{nome} {quantidade}\n"
        alert(text=f'MACRO FINISHED\n{20*"-"}\nList of lost cards:\n{txt}\n{20*"-"}', title='Aviso', button='OK')

    else:
        alert(text="MACRO FINISHED\nNo lost cards has been registered", title='Aviso', button='OK')


def finding_cards(resolutions, nome):

    """Função indentifica correta carta"""

    tamanho = size()

    widths = [0.55, 0.65, 0.75, 1]

    for print_width in widths:
        if is_pressed("esc"):
            break
        screenshot(r"config_print/print.png", region=(
            tamanho.width * 0.5 - (tamanho.width / 2) * 0.34,
            tamanho.height * 0.5 - (tamanho.height / 2) * resolutions,
            (len(nome) * (tamanho.width * 0.0155)) * print_width,
            tamanho.height * 0.5 * 0.13))

        card = str(get_text(r"config_print/print.png")).strip().replace("—", "-")
        if card.lower() == nome.lower():

            press("esc")
            sleep(1)
            return True

    return False


def config_resolution():

    """Função retorna a porcetagem da resolução para o macro"""

    tamanho = size()
    resolutions = [0.57, 0.67, 0.77, 0.80]
    widths = [1, 0.75, 0.65, 0.55]
    nome = 'Maxx "C"'

    search(nome)

    pc.ClickPositions(1026, 320).left_click()
    sleep(0.5)
    pc.ClickPositions(86, 270).left_click()
    sleep(0.5)

    for printaltura in resolutions:
        for print_width in widths:
            if is_pressed("esc"):
                break
            screenshot(r"config_print/print.png", region=(
                tamanho.width * 0.5 - (tamanho.width / 2) * 0.34,
                tamanho.height * 0.5 - (tamanho.height / 2) * printaltura,
                (len(nome) * (tamanho.width * 0.015)) * print_width,
                tamanho.height * 0.5 * 0.15))

            card = str(get_text(r"config_print/print.png")).strip()

            if card.lower() == nome.lower():
                resolution = printaltura
                press("esc")
                sleep(1)
                return resolution
