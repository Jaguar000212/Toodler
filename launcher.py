import customtkinter as ct
from base import BaseMain

from lyrically import Lyrically
from translator import TextTranslator


# Commands
def launch_lyrically():
    toodler.attributes("-disabled", True)
    lyrically = Lyrically(toodler, toodler.configs["api_keys"]["lyricsGenius"])
    lyrically.mainloop()


def launch_translator():
    toodler.attributes("-disabled", True)
    translator = TextTranslator(toodler)
    translator.mainloop()


# Window setup
toodler = BaseMain("Toodler", "Toodler.ico")

ct.CTkButton(
    toodler.toolset,
    text="Lyrically",
    font=toodler.content_font,
    command=launch_lyrically,
).grid(row=1, column=0, padx=10, pady=10)

ct.CTkButton(
    toodler.toolset,
    text="Translator",
    font=toodler.content_font,
    command=launch_translator,
).grid(row=1, column=1, padx=10, pady=10)


if __name__ == "__main__":
    toodler.mainloop()
