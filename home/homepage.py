import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

def home(root):
    home_window = tk.Toplevel(root)
    home_window.title("Home")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = screen_width // 2
    window_height = screen_height // 2

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    home_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    home_window.resizable(width=False, height=False)

    def close_window():
        home_window.destroy()
        root.deiconify()

    current_directory = os.path.dirname(os.path.abspath(__file__))

    image_path = os.path.join(current_directory, "mikasha.png")
    image = Image.open(image_path)

    image = image.resize((window_width, window_height), Image.ANTIALIAS)  # Sử dụng Image.ANTIALIAS

    img_tk = ImageTk.PhotoImage(image)

    image_label = ttk.Label(home_window, image=img_tk)
    image_label.place(x=0, y=0)

    back_button = ttk.Button(home_window, text="Quay lại", command=close_window)
    back_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    home(root)
    root.mainloop()
