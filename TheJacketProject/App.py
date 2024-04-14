import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class LaunchView:
    def __init__(self):

        root = create_new_root()
        self.root = root
        self.canvas = tk.Canvas(root, width=335, height=600)
        self.canvas.pack()

        # Create and place widgets
        # Load and display the image
        image_path = "resources/images/open_screen_graphic.png"
        raw_image = Image.open(image_path)
        resized_image = raw_image.resize((335, 600))
        self.image = ImageTk.PhotoImage(resized_image)

        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

        # Create a style for the button
        style = ttk.Style()
        style.configure("Custom.TButton", background="#4358a8",
                        borderwidth=0, borderradius=10)

        self.button = ttk.Button(
          self.root, text="Get Dressed", command=self.go_home,
          width=20, style="Custom.TButton")
        self.button_window = self.canvas.create_window(
          170, 560, window=self.button)

    def go_home(self):
        print("dressed")  # Open the home page view


def main():
    launch_view = LaunchView()  # Show the window
    launch_view.root.mainloop()


def create_new_root():

    root = tk.Tk()
    root.title("The Jacket Project")

    # Set up the window dimensions
    root.geometry("335x600")
    root.resizable(False, False)  # Disable window resizing

    # Set up the window icon
    icon_path = "resources/images/jacket_icon.png"
    icon_image = Image.open(icon_path)
    icon = ImageTk.PhotoImage(icon_image)
    root.iconphoto(False, icon)

    return root


if __name__ == "__main__":
    main()
