import customtkinter as ct
from tkinter import messagebox, Scrollbar, Listbox
import json


class BaseMain(ct.CTk):
    """
    Represents the main window of the Toodler application.

    Args:
        tool_name (str): The name of the tool.
        icon_path (str, optional): The path to the icon file. Defaults to None.
    """

    def __init__(self, tool_name: str, icon_path: str = None):
        """
        Initializes the BaseMain class.

        Args:
            tool_name (str): The name of the tool.
            icon_path (str, optional): The path to the icon file. Defaults to None.
        """
        super().__init__()

        with open("configs.json", "r") as config_file:
            self.configs = json.load(config_file)

        ct.set_appearance_mode("System")
        ct.set_default_color_theme("blue")
        self.attributes("-fullscreen", True)

        self.wm_title(tool_name)
        if icon_path:
            self.iconbitmap(icon_path)

        self.messagebox = messagebox
        self.scrollbar = Scrollbar
        self.listbox = Listbox

        self.head_font = ct.CTkFont(family="Kristen ITC", size=80, weight="bold")
        self.tagline_font = ct.CTkFont(family="RomanT", size=25)
        self.content_font = ct.CTkFont(family="Ariel", size=20)
        self.subhead_font = ct.CTkFont(family="Ariel", size=40, weight="bold")

        ct.CTkLabel(self, text="Welcome to Toodler", font=self.head_font).pack()
        ct.CTkLabel(
            self, text="A perfect Toolkit for all your needs!", font=self.tagline_font
        ).pack(ipady=50)

        self.toolset = ct.CTkFrame(self)
        self.toolset.pack()

        ct.CTkLabel(
            self.toolset, text="Select a tool to launch -", font=self.subhead_font
        ).grid(row=0, column=0, columnspan=2, sticky="n", padx=50, pady=10)

        ct.CTkButton(
            self, text="Close", font=self.content_font, command=self.destroy
        ).pack(pady=10, side="bottom")


class BaseSub(ct.CTkToplevel):
    """
    Represents a sub-window of the Toodler application.

    Args:
        parent (ct.CTk): The parent window.
        tool_name (str): The name of the tool.
        icon_path (str, optional): The path to the icon file. Defaults to None.
    """

    def __init__(self, parent: ct.CTk, tool_name: str, icon_path: str = None):
        """
        Initializes the BaseSub class.

        Args:
            parent (ct.CTk): The parent window.
            tool_name (str): The name of the tool.
            icon_path (str, optional): The path to the icon file. Defaults to None.
        """
        super().__init__()

        with open("configs.json", "r") as config_file:
            self.configs = json.load(config_file)

        ct.set_appearance_mode("System")
        ct.set_default_color_theme("blue")
        self.attributes("-fullscreen", True)

        self.wm_title(tool_name)
        if icon_path:
            self.iconbitmap(icon_path)

        self.parent = parent

        self.messagebox = messagebox
        self.scrollbar = Scrollbar
        self.listbox = Listbox

        self.head_font = ct.CTkFont(family="Kristen ITC", size=80, weight="bold")
        self.subhead_font = ct.CTkFont(family="Ariel", size=40, weight="bold")
        self.tagline_font = ct.CTkFont(family="RomanT", size=25)
        self.content_font = ct.CTkFont(family="Ariel", size=20)

        ct.CTkButton(
            self, text="Close", font=self.content_font, command=self.close
        ).pack(pady=10, side="bottom")

    def close(self):
        """Closes the sub-window and enables the parent window."""
        self.parent.attributes("-disabled", False)
        self.destroy()
        self.parent.attributes("-disabled", False)
