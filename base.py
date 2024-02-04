import customtkinter as ct
from tkinter import messagebox, Scrollbar, Listbox

import json

class BASE(ct.CTk):
    
        def __init__(self, tool_name: str, icon_path: str = None):
            super().__init__()
            
            self.tool_name = tool_name
            
            self.width = self.winfo_screenwidth()
            self.height = self.winfo_screenheight()
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
            
            self.head_font = ct.CTkFont(family = "Kristen ITC", size=80, weight="bold")
            self.tagline_font = ct.CTkFont(family = "RomanT", size=25)
            self.content_font = ct.CTkFont(family = "Ariel", size=20)
            self.subhead_font = ct.CTkFont(family = "Ariel", size=40, weight="bold")