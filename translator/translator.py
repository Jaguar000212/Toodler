import customtkinter as ct
from googletrans import Translator, LANGUAGES, LANGCODES
import requests

from base import BaseSub


class TextTranslator(BaseSub):

    def __init__(self, parent: ct.CTk):
        super().__init__(parent, "Translator", "translator\\Translator.ico")

        self.translator = Translator()
        self.availLang = [lang.capitalize() for lang in LANGUAGES.values()]
        self.iLang = ct.StringVar(value="Select Language")
        self.oLang = ct.StringVar(value="Select Language")

        self.mainFrame = ct.CTkFrame(self)
        self.mainFrame.pack(expand = True, fill="both", ipadx=50, ipady=50)

        ct.CTkLabel(self.mainFrame, text="Welcome to Languagically", font=self.head_font).grid(
            pady=50, row=0, column=0, columnspan=2
        )

        self.iFrame = ct.CTkFrame(self.mainFrame)
        self.iFrame.columnconfigure(0, weight=1)
        self.iFrame.rowconfigure(1, weight=1)
        self.iFrame.grid(padx=50, row=1, column=0, sticky="nw")

        ct.CTkOptionMenu(
            self.iFrame, values=self.availLang, variable=self.iLang, width=500
        ).grid(pady=10)
        self.iText = ct.CTkTextbox(
            self.iFrame, font=self.content_font, height=500, width=500
        ).grid()

        self.oFrame = ct.CTkFrame(self.mainFrame)
        self.oFrame.columnconfigure(0, weight=1)
        self.oFrame.rowconfigure(1, weight=1)
        self.oFrame.grid(padx=50, row=1, column=1, sticky="ne")

        ct.CTkOptionMenu(
            self.oFrame, values=self.availLang, variable=self.oLang, width=500
        ).grid(pady=10)
        self.oText = ct.CTkTextbox(
            self.oFrame, font=self.content_font, height=500, width=500
        ).grid()

        self.translateButton = ct.CTkButton(
            self.mainFrame,
            text="Translate",
            font=self.content_font,
            command=self.translate,
        )

    def translate(self):
        self.reset()
        text = self.text.get()
        lang = self.lang.get()

        translated_text = self.translator.translate(text, dest=LANGCODES[lang.lower()])

        self.translated_text.set(translated_text.text)
        return True

    def reset(self):
        self.translated_text.set("")
        return True
