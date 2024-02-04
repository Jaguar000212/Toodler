import customtkinter as ct
from tkinter import messagebox

import lyricsgenius
import requests

class Lyrically(ct.CTk):

    def __init__(self, api_key: str = None):
        super().__init__()
        
        if not api_key:
            raise Exception("No API Key provided")
        
        self.LyricsGenius = lyricsgenius.Genius(api_key)

        ct.set_appearance_mode("System")
        ct.set_default_color_theme("blue")
        self.geometry("1280x1024")
        self.wm_title("Lyrically")
        self.iconbitmap(r"lyrically\Lyrically.ico")

        self.name = ct.StringVar()
        self.lyrics = ct.StringVar()

        ct.CTkLabel(self, text="Welcome to Lyrically", font=ct.CTkFont(size=40, weight="bold")).pack(pady = 50)
        ct.CTkLabel(self, text = "Enter song Name", font=ct.CTkFont(size = 20)).pack()
        ct.CTkEntry(self, placeholder_text="Enter song name", textvariable=self.name, font=ct.CTkFont(size=20)).pack(pady = 10)
        ct.CTkButton(self, text="Search", font=ct.CTkFont(size=20), command=self.getLyrics).pack(pady = 10)

        self.data = ct.CTkLabel(self, text = "")
        self.data.pack()

    def getLyrics(self):
        self.reset()

        name = self.name.get()
        try:
            lyrics = self.LyricsGenius.search_song(name).lyrics
        except requests.exceptions.ConnectionError:
            return messagebox.showerror("Failed", "No Internet Connection.")
        except AttributeError:
            self.reset()
            return messagebox.showerror("Failed", "No lyrics found.")
        except requests.exceptions.Timeout:
            self.reset()
            return messagebox.showerror("Failed", "Connection timed out.")


        self.lyrics = ct.CTkTextbox(self, font=ct.CTkFont(size = 18), height = 800)
        self.lyrics.insert('1.0', lyrics)
        self.lyrics.pack(fill = 'both')
        self.lyrics.configure(state = 'disabled')
        return True

    def reset(self):
        try:
            self.lyrics.pack_forget()
        except AttributeError:
            pass
        