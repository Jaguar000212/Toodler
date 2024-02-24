import customtkinter as ct
from googletrans import Translator, LANGUAGES, LANGCODES
from httpcore import ConnectError

from translator.exceptions.exceptions import InvalidLanguage
from base import BaseSub


class TextTranslator(BaseSub):
    def __init__(self, parent: ct.CTk):
        super().__init__(parent, "Translator", "translator\\Translator.ico")

        self.translator = Translator(
            service_urls=[
                "translate.google.com",
            ]
        )
        self.availLang = [lang.capitalize() for lang in LANGUAGES.values()]
        self.iLang = ct.StringVar(value="Auto Detect")
        self.oLang = ct.StringVar(value="Select Language")

        self.mainFrame = ct.CTkFrame(self)
        self.mainFrame.pack(
            expand=True, fill="both", ipadx=50, ipady=50, side="top", anchor="n"
        )

        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.columnconfigure(1, weight=1)

        ct.CTkLabel(
            self.mainFrame, text="Welcome to  Translator", font=self.head_font
        ).grid(pady=50, row=0, column=0, columnspan=2, sticky="n")
        ct.CTkLabel(
            self.mainFrame,
            text="A perfect tool to translate text to any language!",
            font=self.tagline_font,
        ).grid(row=1, column=0, columnspan=2, sticky="n")

        self.iFrame = ct.CTkFrame(self.mainFrame)
        self.iFrame.columnconfigure(0, weight=1)
        self.iFrame.rowconfigure(1, weight=1)
        self.iFrame.grid(pady=50, row=2, column=0, sticky="e")

        ct.CTkLabel(
            self.iFrame, text="Enter text to translate -", font=self.subhead_font
        ).pack()
        ct.CTkOptionMenu(
            self.iFrame, values=self.availLang, variable=self.iLang, width=500
        ).pack(pady=10)
        self.iText = ct.CTkTextbox(
            self.iFrame, font=self.content_font, height=500, width=500
        )
        self.iText.pack()

        self.oFrame = ct.CTkFrame(self.mainFrame)
        self.oFrame.columnconfigure(0, weight=1)
        self.oFrame.rowconfigure(1, weight=1)
        self.oFrame.grid(padx=50, row=2, column=1, sticky="w")

        ct.CTkLabel(self.oFrame, text="Translated text -", font=self.subhead_font).grid(
            row=0, column=0, columnspan=2, sticky="w"
        )
        ct.CTkOptionMenu(
            self.oFrame, values=self.availLang, variable=self.oLang, width=500
        ).grid(pady=10)
        self.oText = ct.CTkTextbox(
            self.oFrame, font=self.content_font, height=500, width=500
        )
        self.oText.grid()

        self.translateButton = ct.CTkButton(
            self.mainFrame,
            text="Translate",
            font=self.content_font,
            command=self.translate,
        ).grid(pady=50, row=3, column=0, columnspan=2)

    def translate(self):
        self.reset()
        itext = self.iText.get("1.0", "end-1c")
        ilang = self.iLang.get()
        olang = self.oLang.get()

        if ilang == "Auto Detect":
            ilang = "auto"
        else:
            try:
                ilang = LANGCODES[ilang.lower()]
            except KeyError:
                raise InvalidLanguage("input")

        if olang in LANGUAGES:
            try:
                olang = LANGCODES[olang.lower()]
            except KeyError:
                raise InvalidLanguage("output")

        try:
            otext = self.translator.translate(itext, olang, ilang)
        except ValueError:
            raise InvalidLanguage("")
        except ConnectError:
            self.messagebox.error("Failed", "Can't Connect to the internet.")

        self.oText.insert("1.0", otext.text)

    def reset(self):
        self.oText.delete("1.0", "end")
        return True
