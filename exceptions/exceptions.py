from tkinter import messagebox


class InvalidLanguage(Exception):
    """
    Exception raised when an invalid language is encountered.

    Attributes:
        type (str): The type of language that is invalid.
    """

    def __init__(self, type: str, parent):
        """
        Initializes a new instance of the InvalidLanguage class.

        Args:
            type (str): The type of language that is invalid.
            parent: The parent widget for displaying the error message.
        """
        self.message = f"Invalid {type} language."
        messagebox.showerror("Error", self.message, parent=parent)
        super().__init__(self.message)


class NoAPIKey(Exception):
    """
    Exception raised when no API key is provided.

    Attributes:
        message (str): The error message.
    """

    def __init__(self, message: str, parent):
        """
        Initializes a new instance of the NoAPIKey class.

        Args:
            message (str): The error message.
            parent: The parent widget for displaying the error message.
        """
        messagebox.showerror("Error", message, parent=parent)
        super().__init__(message)
