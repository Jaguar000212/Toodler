import customtkinter as ct
from tkinter import messagebox, Scrollbar, Listbox, PhotoImage

import json


class BaseMain(ct.CTk):

    def __init__(self, tool_name: str, icon_path: str = None):
        super().__init__()

        with open("configs.json", "r") as config_file:
            self.configs = json.load(config_file)

        ct.set_appearance_mode("System")
        ct.set_default_color_theme("blue")
        self.attributes("-fullscreen", True)

        self.wm_title(tool_name)
        self.iconbitmap(icon_path)

        self.messagebox = messagebox
        self.scrollbar = Scrollbar
        self.listbox = Listbox

        self.head_font = ct.CTkFont(family="Kristen ITC", size=80, weight="bold")
        self.tagline_font = ct.CTkFont(family="RomanT", size=25)
        self.content_font = ct.CTkFont(family="Ariel", size=20)
        self.subhead_font = ct.CTkFont(family="Ariel", size=40, weight="bold")

        # Main content
        # Title
        ct.CTkLabel(self, text="Welcome to Toodler", font=self.head_font).pack()

        # Tagline
        ct.CTkLabel(
            self, text="A perfect Toolkit for all your needs!", font=self.tagline_font
        ).pack(ipady=50)

        # Tools frame
        self.toolset = ct.CTkFrame(self)
        self.toolset.pack()

        ct.CTkLabel(
            self.toolset, text="Select a tool to launch -", font=self.subhead_font
        ).grid(row=0, column=0, columnspan=2, sticky="n", padx=50, pady=10)

        # Close Buttons
        ct.CTkButton(
            self, text="Close", font=self.content_font, command=self.destroy
        ).pack(pady=10, side="bottom")


class BaseSub(ct.CTkToplevel):

    def __init__(self, parent: ct.CTk, tool_name: str, icon_path: str = None):
        super().__init__()

        with open("configs.json", "r") as config_file:
            self.configs = json.load(config_file)

        ct.set_appearance_mode("System")
        ct.set_default_color_theme("blue")
        self.attributes("-fullscreen", True)

        self.wm_title(tool_name)
        self.iconbitmap(icon_path)

        self.parent = parent

        self.messagebox = messagebox
        self.scrollbar = Scrollbar
        self.listbox = Listbox

        self.head_font = ct.CTkFont(family="Kristen ITC", size=80, weight="bold")
        self.tagline_font = ct.CTkFont(family="RomanT", size=25)
        self.content_font = ct.CTkFont(family="Ariel", size=20)
        self.subhead_font = ct.CTkFont(family="Ariel", size=40, weight="bold")

        # Close Buttons
        ct.CTkButton(
            self, text="Close", font=self.content_font, command=self.close
        ).pack(pady=10, side="bottom")

    def close(self):
        self.parent.attributes("-disabled", False)
        self.destroy()
