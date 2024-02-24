from tkinter import messagebox

class InvalidLanguage(Exception):
    def __init__(self, type: str,):
        self.message = f"Invalid {type} language."
        messagebox.showerror("Error", self.message)
        super().__init__(self.message)