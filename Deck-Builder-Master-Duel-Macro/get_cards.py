from re import findall, UNICODE
from requests import get
from bs4 import BeautifulSoup
from colorama import init


def deck(show=False):

    """This function gets the HTML of the link and looks  for card names"""

    init()
    cards = dict()

    while True:
        try:
            print("Insert a valid link from \33[34mhttps://www.masterduelmeta.com/\33[m\n"
                  "Examples of valid links: \33[34mhttps://www.masterduelmeta.com/top-decks\33[m\n"
                  "\33[96mType '3' to return to menus.\33[m")
            resposta = input("link:")

            if resposta == "3":
                return resposta

            else:
                conec = get(resposta)
            html = BeautifulSoup(conec.text, "html.parser").decode()
            card = findall(r'\bname\\":\\"(.+?)\\"},\\"amount\b', str(html), UNICODE)
            amount = findall(r'\bamount\\":(\d)\b', str(html), UNICODE)
            break

        except:
            print("\n" * 100)
            print("\n\n\33[31mPlease, get a valid link!\33[m")

    for x in range(len(card)):

        if """\\\"""" in card[x]:
            name_card = card[x].replace(r"""\\\"""", '')
        else:
            name_card = card[x]

        cards[name_card] = amount[x]

    if show:
        print("\n\nList Of Cards:")
        for x, y in cards.items():
            print(x, y)
        print("\n\n\n\n")
    return cards
