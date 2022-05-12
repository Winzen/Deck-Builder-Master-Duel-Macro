import tkinter as tk
from time import sleep
from PIL import ImageTk, Image
from func import config_colum, alert
from formando_deck_class import bot_deck
from get_deckV2 import deck
from pyautogui import confirm, prompt
import webbrowser


class MacroGui:

    def __init__(self):
        self.window = tk.Tk()
        self.page = 0
        self.window.title("MACRO MASTER DUEL")

        self.window.geometry("600x500")

        self.window.resizable(width=False, height=False)

        self.window.rowconfigure([0, 1], minsize=50, weight=1)

        self.window.columnconfigure([0, 1], minsize=50, weight=1)

        self.active_frame = tk.Frame(self.window, bd=2)

        self.buttons_menus()
        self.home()
        self.window.mainloop()

    def buttons_menus(self):
        name_buttons = {
            "Home": self.home,
            "Get Card List": self.get_list,
            "Deck Builder Macro": self.tutorial,
            "Videos/Github": self.videos_git,
            "Restart Config": self.restart_config}

        menu_buttons = tk.Frame(self.window, bd=2)

        for row, name in enumerate(name_buttons.keys()):
            button = tk.Button(master=menu_buttons, text=name, command=name_buttons[name], relief=tk.RAISED,
                               justify="left", font="Arial 10 bold", bg="#b1bbf3")
            button.grid(row=row, column=0, sticky="ew", padx=5, pady=5)
        menu_buttons.grid(row=0, column=0, sticky="ew")

    def home(self):
        self.clear()
        txt = tk.Label(master=self.active_frame, text="""
Welcome to Deck-Builder-Master-Duel-Macro!!!
Version 0.02v

###
Attention !!
Some buttons can trigger your anti-virus at the first click them
it's because the macro modify two files in the folder config_print
config.txt saves some useful settings
print.png is a print that the macro used to read the name of cards
###

What do you want to do?

Get Card list - Get the list of cards and amount of a deck(TXT)

Deck Builder Macro - Automatically build a deck using the Macro

Videos/GitHub - Direct Buttons to youtube tutorial and Github page

Restart Config - Restart your configuration data from the macro""",
                       justify="left", font="Arial 10 bold", wraplength=400)
        txt.grid(row=0, column=0, sticky="ew")
        self.active_frame.grid(row=0, column=1, sticky="ew")

    def tutorial(self):

        self.clear()
        text = """
Before proceeding.
Make sure the game configuration  is correct.

Requirements:

1 - The game's language must be English.
2 - The game's resolution must be 1280x720.
3 - The game's view mode must be Full Screen Mode.
4 - In the Deck Builder, show up all card must be active.
5 - Go to Deck Builder

To stop the macro just HOLD the "Esc" on your keybord.

Next - For imagens of each requirement
Start MACRO - Configuration or Begins Macro"""

        self.list_pages = [{"text": text, "imagem": None},
                      {"text": "Make sure your settings are the same as above", "imagem": "config.png"},
                      {"text": "Now go to the Deck Builder", "imagem": "deck_builder.png"},
                      {"text": "Make sure your option is the same as above", "imagem": "mult_card.png"},
                      {"text": "(Optional) Set your filter this way", "imagem": "filter.png"},
                      {"text": "To stop the macro just HOLD the 'Esc' on your keybord", "imagem": "enc.png"},
                      {"text": "Keep your game screen in Deck Builder", "imagem": "deck_builder.png"}]

        if self.list_pages[self.page]["imagem"] is not None:
            self.insert_imagem(self.list_pages[self.page]['imagem'], 400, 350)

        txt2 = tk.Label(master=self.active_frame, text=self.list_pages[self.page]["text"],
                        justify="left",
                        font="Arial 10 bold",
                        wraplength=400)
        txt2.grid(row=1, column=0, sticky="ew")

        list_button = {"Back": self.page_down,
                       "Next": self.page_up,
                       "Start MACRO": self.start_config,
                       "Youtube Tutorial": lambda: webbrowser.open("https://www.youtube.com/watch?v=017VpAc7IsU")}

        self.insert_buttons(list_button, self.active_frame, bd=30)

    def get_list(self):
        self.clear()

        self.text = tk.Text(master=self.active_frame, width=50)

        self.text.grid(row=0, column=0)

        list_button = {"Get cards": self.get_list_cards,
                       "Exemple Links": lambda: webbrowser.open("https://www.masterduelmeta.com/top-decks")}

        self.insert_buttons(list_button, self.active_frame, bd=30)

    def get_list_cards(self):

        self.text.delete("1.0", tk.END)

        cards = self.macro_from_link(only_cards=True)

        if cards is not None:
            for nome, quantidade in cards.items():
                self.text.insert(tk.INSERT, f"{nome} {quantidade}\n")

    def videos_git(self):

        self.clear()

        frame = tk.Frame(self.active_frame, height=800)
        list_pages = [{"text": "YouTube", "imagem": "youtube.png",
                       "comando": lambda: webbrowser.open("https://youtu.be/WcLmCGmUJv0")},
                      {"text": "GitHub", "imagem": "git.png",
                       "comando": lambda: webbrowser.open("https://github.com/Winzen/Deck-Builder-Master-Duel-Macro")}]

        txt = tk.Label(master=self.active_frame,
                       text="Youtube: ShowCase e Tutorial\nGitHub: Files, Updates and tutorial",
                       justify="left", font="Arial 14 bold")
        txt.grid(row=0, column=0)

        for n, buttons in enumerate(list_pages):
            imagem = Image.open(fr"imagens\{buttons['imagem']}")
            imagem = imagem.resize((40, 20))
            imagemtk = ImageTk.PhotoImage(imagem)

            button = tk.Button(master=frame, text=buttons['text'], image=imagemtk, command=buttons['comando'])
            button.imagem = imagemtk
            button.grid(row=0, column=n * 2 + 1, sticky="e")

            label = tk.Label(master=frame, text=buttons['text'],
                             justify="left", font="Arial 10 bold")
            label.grid(row=0, column=n * 2, sticky="e")

        frame.grid(row=1, column=0, sticky="ew")

    def restart_config(self):

        re = confirm(text=f"(This only is recommended if the macro doesn't work properly)\n"
                          f"Are you sure about to restart your config file?", title='Warning')

        if re == "OK":
            config = open(r"config_print\config.txt", "w")
            config.close()

    def page_up(self):

        if self.page < len(self.list_pages) - 1:
            self.page += 1
            self.tutorial()

    def page_down(self):

        if self.page > 0:
            self.page -= 1
            self.tutorial()

    def start_config(self):

        if config_colum(True) is False:
            self.clear()
            txt = tk.Label(master=self.active_frame)

            txt.grid(row=0, column=0, sticky="ew")
            txt2 = tk.Label(master=self.active_frame, text="We detected that you don't have any configuration saved\n"
                                                           "Please click 'Start Config' to create a configuration file"
                                                           "\n\n"
                                                           "Youtube Tutorial - Redirecting to video setup tutorial\n"
                                                           "Start Config - Starts de Setup. After clicking you have 5 "
                                                           "seconds to return to the game before the Config starts.",
                            justify="left",
                            font="Arial 10 bold",
                            wraplength=400)

            txt2.grid(row=1, column=0, sticky="ew")

            list_button = {"Start CONFIG": self.config,
                           "Youtube Tutorial": lambda: webbrowser.open("https://youtu.be/017VpAc7IsU?t=62")}

            self.insert_buttons(list_button, self.active_frame)

        else:
            self.macro_deck()

    def config(self):

        self.invervalo()
        config_colum()
        alert(text="Configuration Done\nThe data has been saved\nPlease Return  to the macro to continue.",
              title='Aviso', button='OK')
        self.macro_deck()

    def invervalo(self):

        self.clear()

        imagem = Image.open(fr"imagens\deck_builder.png")
        imagem = imagem.resize((400, 350))
        imagemtk = ImageTk.PhotoImage(imagem)

        txt = tk.Label(master=self.active_frame, image=imagemtk)

        txt.grid(row=0, column=0, sticky="ew")

        for x in range(5):
            txt2 = tk.Label(master=self.active_frame,
                            text=f"You must to return to the Deck Build Screen Please.. SECONDS: {x + 1}",
                            justify="left", font="Arial 10 bold", wraplength=400)
            txt2.grid(row=1, column=0, sticky="ew")
            self.window.update()
            sleep(1)

    def clear(self):

        self.active_frame.destroy()
        self.active_frame = tk.Frame(self.window, bd=2)
        self.active_frame.grid(row=0, column=1, sticky="ew")

    def macro_deck(self):

        text = """
Before proceeding.
Make sure the game configuration  is correct.

Requirements:

1 - The game's language must be English.
2 - The game's resolution must be 1280x720.
3 - The game's view mode must be Full Screen Mode.
4 - In the Deck Builder, show up all card must be active.
5 - Go to Deck Builder

To stop the macro just HOLD the "Esc" on your keybord.

After you placing the link you have 5 seconds to return to the game before the macro starts."""

        self.clear()

        list_pages = {"From Link": self.macro_from_link,
                      "From TXT": self.from_txt,
                      "Deck Examples": lambda: webbrowser.open("https://www.masterduelmeta.com/top-decks"),
                      "Youtube Tutorial":
                          lambda: webbrowser.open(
                              "https://www.youtube.com/playlist?list=PLX18qf4z-4-FySlHbosVuf-T_qsqDIOxd")}

        txt = tk.Label(master=self.active_frame,
                       text=text + "\n\nFrom Link - Get the card list from masterduelmeta.com/\n"
                                   "From TXT - Get the card list from TEXTS\n",

                       justify="left",
                       font="Arial 8 bold",
                       wraplength=400)
        txt.grid(row=0, column=0, sticky="ew")

        self.insert_buttons(list_pages, self.active_frame, bd=2)

    def macro_from_link(self, only_cards=False):

        text = "Insert a valid link from https://www.masterduelmeta.com/\n" \
               "Examples of valid links: https://www.masterduelmeta.com/top-decks"
        while True:
            try:
                link = prompt(text=text, title="Insert Link")
                if link is not None:
                    deck_cards = deck(link)
                    if only_cards is True:
                        return deck_cards

                    else:
                        self.invervalo()
                        bot_deck(deck_cards)
                        self.macro_deck()
                return link

            except Exception:
                text = "Insert a valid link from https://www.masterduelmeta.com/\n" \
                       "Examples of valid links: https://www.masterduelmeta.com/top-decks""\nPLEASE, LINK VALID"
                raise

    def from_txt(self):

        self.clear()

        self.text_cards = tk.Text(master=self.active_frame, width=50)
        self.text_cards.grid(row=0, column=0)

        text = tk.Label(master=self.active_frame,
                        text="Card names must be exactly the same as the Master Duel card names!!",
                        justify="left",
                        font="Arial 8 bold")
        text.grid(row=1, column=0)

        list_button = {"Start Macro": self.txt_card,
                       "Text Valid Format":
                           lambda: webbrowser.open("https://github.com/Winzen/Projetos-Aleatorios/tree/main/"
                                                   "GUI%20Tkinker#examples-of-text-format"),
                       "Youtube Tutorial": lambda: webbrowser.open("https://www.youtube.com/watch?v=A9Ue5i3Pc0E")}

        self.insert_buttons(list_button, self.active_frame, bd=10)

    def insert_imagem(self, caminho, largura, altura, fundo=False):
        imagem = Image.open(fr"imagens\{caminho}")
        imagem = imagem.resize((largura, altura))
        imagemtk = ImageTk.PhotoImage(imagem)
        if fundo is False:
            txt = tk.Label(master=self.active_frame, image=imagemtk)
            txt.image = imagemtk
            txt.grid(row=0, column=0, sticky="ew")
        else:
            return imagemtk

    def txt_card(self):

        deck_cards = deck(self.text_cards.get("1.0", tk.END), txt=True)
        if deck_cards is not None:
            self.invervalo()
            bot_deck(deck_cards)
            self.macro_deck()

    def insert_buttons(self, list_button, master, row_master=2, column_master=0, bd=20):

        frame = tk.Frame(master, bd=bd)

        for column, nome in enumerate(list_button.keys()):
            button = tk.Button(master=frame, text=nome, command=list_button[nome], relief=tk.GROOVE)
            button.grid(row=0, column=column, sticky="ew")

        frame.grid(row=row_master, column=column_master, sticky="ew")
