import customtkinter as ct
from base import BaseMain

from lyrically import Lyrically


# Commands
def launch_lyrically():
    toodler.attributes("-disabled", True)
    lyrically = Lyrically(toodler, toodler.configs["api_keys"]["lyricsGenius"])
    lyrically.mainloop()


# Window setup
toodler = BaseMain("Toodler", "Toodler.ico")

lyrically_button = ct.CTkButton(
    toodler.toolset,
    text="Lyrically",
    font=toodler.content_font,
    command=launch_lyrically,
)
lyrically_button.grid(row=1, column=0, padx=10, pady=10)


if __name__ == "__main__":
    toodler.mainloop()
