import tkinter as tk
from tkinter import ttk


class HomePageView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Home Page")

        # Set up the window dimensions (fixed size)
        self.root.geometry("400x600")
        self.root.resizable(False, False)  # Disable window resizing

        # Set up the window icon
        icon_path = "home_icon.png"
        icon_image = tk.PhotoImage(file=icon_path)
        self.root.iconphoto(False, icon_image)

        # Add content to the home page
        label = ttk.Label(self.root, text="Welcome to the Home Page!",
                          font=("Arial", 18))
        label.pack(pady=20)

        # Show the window
        self.root.mainloop()
