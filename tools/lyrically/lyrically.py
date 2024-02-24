import customtkinter as ct
import lyricsgenius
from requests.exceptions import ConnectionError, Timeout
import exceptions

from base import BaseSub


class Lyrically(BaseSub):
    """
    A class that represents the Lyrically tool.

    Attributes:
    - parent (ct.CTk): The parent widget.
    - api_key (str): The API key for the LyricsGenius API.
    - LyricsGenius (lyricsgenius.Genius): The LyricsGenius object.
    - name (ct.StringVar): The variable to store the song name.
    - lyrics (ct.StringVar): The variable to store the lyrics.

    Methods:
    - __init__(self, parent: ct.CTk, api_key: str = None): Initializes the Lyrically tool.
    - getLyrics(self): Retrieves the lyrics of a song.
    - reset(self): Resets the Lyrically tool.
    """

    def __init__(self, parent: ct.CTk, api_key: str = None):
        """
        Initializes the Lyrically tool.

        Parameters:
        - parent (ct.CTk): The parent widget.
        - api_key (str): The API key for the LyricsGenius API.

        Raises:
        - NoAPIKey: If no API key is provided.
        """
        super().__init__(parent, "Lyrically", "tools\\lyrically\\Lyrically.ico")

        if not api_key:
            raise exceptions.NoAPIKey("No API Key provided", parent=self)

        self.LyricsGenius = lyricsgenius.Genius(api_key)
        self.name = ct.StringVar()
        self.lyrics = ct.StringVar()

        ct.CTkLabel(self, text="Lyrically", font=self.head_font).pack()
        ct.CTkLabel(
            self, text="Get the lyrics of your favourite songs!", font=self.tagline_font
        ).pack(ipady=50)

        ct.CTkLabel(self, text="Enter song Name", font=ct.CTkFont(size=20)).pack()
        ct.CTkEntry(
            self,
            placeholder_text="Enter song name",
            textvariable=self.name,
            font=ct.CTkFont(size=20),
        ).pack(pady=10)

        ct.CTkButton(
            self, text="Search", font=ct.CTkFont(size=20), command=self.getLyrics
        ).pack(pady=10)

    def getLyrics(self):
        """Retrieves the lyrics of a song."""
        self.reset()
        name = self.name.get()

        try:
            lyrics = self.LyricsGenius.search_song(name).lyrics
        except AttributeError:
            self.reset()
            return self.messagebox.showerror("Failed", "No lyrics found.", parent=self)
        except ConnectionError:
            return self.messagebox.showerror(
                "Failed", "No Internet Connection.", parent=self
            )
        except Timeout:
            self.reset()
            if self.messagebox.askretrycancel(
                "Failed", "Connection timed out.", parent=self
            ):
                return self.getLyrics()
            return False

        self.lyrics = ct.CTkTextbox(self, font=ct.CTkFont(size=18), height=800)
        self.lyrics.insert("1.0", lyrics)
        self.lyrics.pack(fill="both")
        self.lyrics.configure(state="disabled")
        return True

    def reset(self):
        """Resets the Lyrically tool."""
        try:
            self.lyrics.pack_forget()
        except AttributeError:
            pass
