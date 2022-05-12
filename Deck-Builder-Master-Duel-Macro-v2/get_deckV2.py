from re import findall, UNICODE
from requests import get
from bs4 import BeautifulSoup


def deck(link, show=False, txt=False):

    """This function gets the HTML of the link and looks  for card names"""

    cards = dict()
    card = amount = None

    if txt is False:
        resposta = link
        conec = get(resposta)
        html = BeautifulSoup(conec.text, "html.parser").decode()
        html = findall(r"""\\"main\\":\[{\\"card\\(.+?)\\"side\\":""", str(html), UNICODE)
        card = findall(r'\bname\\":\\"(.+?)\\"},\\"amount\b', str(html[0]), UNICODE)
        amount = findall(r'\bamount\\":(\d)\b', str(html[0]), UNICODE)

    elif txt is True:
        link = (str(link).lower()).replace("'", '"')
        re_list_cards = {r"(.+?) x\s?\d": r"x\s?(\d)",
                         r"x\s?\d\s? (.+)": r"x\s?(\d)",
                         r"\s?\d\s?x (.+)": r"(\d)\s?x",
                         r"[\d] (.+)": r"\b(\d)\b ",
                         r"(.+) [\d]": r" \b(\d)\b"}
        for cards_re, amount_re in re_list_cards.items():
            card = findall(cards_re, link, UNICODE)
            amount = findall(amount_re, link, UNICODE)
            if len(card) == len(amount) and len(card) > 0:
                break
    if len(card) == len(amount) and len(card) > 0:

        for x in range(len(card)):

            if """\\\"""" in card[x]:
                name_card = card[x].replace(r"""\\\"""", '"')
            else:
                name_card = card[x]

            cards[name_card] = amount[x]

        if show:
            print("\n\nList Of Cards:")
            for x, y in cards.items():
                print(x, y)
            print("\n\n\n\n")
        return cards

    else:
        return None
