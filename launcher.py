import customtkinter as ct
from base import BASE

from lyrically import Lyrically

# Commands
def launch_lyrically():
    lyrically = Lyrically(toodler.configs["api_keys"]["lyricsGenius"])
    lyrically.mainloop()
# Window setup
toodler = BASE("Toodler", "toodler.ico")

# Main content
# Title
title = ct.CTkLabel(toodler, text="Welcome to Toodler", font=toodler.head_font)
title.pack()

# Tagline
tagline = ct.CTkLabel(toodler, text="A perfect Toolkit for all your needs!", font=toodler.tagline_font)
tagline.pack(ipady=50)


#Tools frame
toolset = ct.CTkFrame(toodler)
toolset.pack()

# Tools buttons
head = ct.CTkLabel(toolset, text="Select a tool to launch -", font=toodler.subhead_font)
head.grid(row=0, column=0, columnspan=1, sticky="n", padx=50, pady=10)

lyrically_button = ct.CTkButton(toolset, text="Lyrically", font=toodler.content_font, command=launch_lyrically)
lyrically_button.grid(row=1, column=0, padx=10, pady=10)

            
if __name__ == "__main__":
    toodler.mainloop()