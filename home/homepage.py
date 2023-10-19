import tkinter as tk
from tkinter import ttk


def home(root):
    home_window = tk.Toplevel(root)
    home_window.title("Home")
    home_window.geometry("1140x820")

    def close_window_2():
        home_window.destroy()  # Đóng cửa sổ 2
        root.deiconify() 
    back_button = ttk.Button(home_window, text="Back", command=close_window_2)
    back_button.pack()

    label = tk.Label(home_window, text="Đây là homepage", font=("Arial", 46))  # Đặt kích thước font là 16
    label.pack(expand=True, fill="both")

 